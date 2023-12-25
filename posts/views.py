from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from posts.models import Post


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
    context = {
        'post': post,
    }
    return render(request, 'posts/post_detail.html', context)
