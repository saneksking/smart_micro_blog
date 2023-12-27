from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from posts.models import Post, Comment


def posts(request):
    post_list = Post.objects.filter(status=True)
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    objects = paginator.get_page(page)
    context = {
        'objects': objects,
    }
    return render(request, 'posts/post_list.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comment_list = Comment.objects.filter(post_id=post.id)
    author = request.POST.get('new_author', None)
    new_comment = request.POST.get('new_comment', None)
    if 'btn' in request.POST:
        comment = Comment.objects.create(
            author=author,
            text=new_comment,
            post_id=post.id,
        )
        comment.save()
        return redirect(reverse('posts:post_detail', args=(post.id,)))
    context = {
        'post': post,
        'comment_list': comment_list,
    }
    return render(request, 'posts/post_detail.html', context)


