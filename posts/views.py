from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post


def posts(request):
    post_list = Post.objects.filter(status=True)
    context = {
        'post_list': post_list,
    }
    return render(request, 'posts/post_list.html', context)


def post_detail(request, post_id):
    return HttpResponse('Страница определённого поста')
