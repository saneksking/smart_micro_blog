from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from posts.models import Post, Comment, Grade
from posts.forms import CreatePostForm
from smart.get_ip_master import IpMaster

def posts(request):
    post_list = Post.objects.filter(status=True)
    paginator = Paginator(post_list, 5)
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
            author=author or 'Гость',
            text=new_comment,
            post_id=post.id,
        )
        comment.save()
        return redirect(reverse('posts:post_detail', args=(post.id,)))
    paginator = Paginator(comment_list, 5)
    comment = request.GET.get('page')
    objects = paginator.get_page(comment)
    context = {
        'post': post,
        'objects': objects,
    }
    return render(request, 'posts/post_detail.html', context)


def post_grade_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    ip = IpMaster.get_ip(request=request)
    grade = Grade.objects.filter(post_id=post.id, ip=ip, grade_status=True).exists()
    if grade:
        return redirect(reverse('posts:post_detail', args=(post.id,)))
    else:
        create_grade = Grade.objects.create(
            post_id=post.id,
            grade_status=True,
            ip=ip,
        )
        create_grade.save()
        return redirect(reverse('posts:post_detail', args=(post.id,)))


def post_grade_dislike(request, post_id):
    post_id = get_object_or_404(Post, id=post_id)
    ip = IpMaster.get_ip(request=request)
    grade = Grade.objects.filter(post_id=post_id.id, ip=ip, grade_status=False).exists()
    if grade:
        return redirect(reverse('posts:post_detail', args=(post_id.id,)))
    else:
        create_grade = Grade.objects.create(
            post_id=post_id.id,
            grade_status=False,
            ip=ip,
        )
        create_grade.save()
        return redirect(reverse('posts:post_detail', args=(post_id.id,)))


def post_create(request):
    form = CreatePostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('posts:posts'))
    context = {
        'form': form,
    }
    return render(request, 'posts/post_create.html', context)
