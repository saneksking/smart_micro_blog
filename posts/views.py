from django.http import HttpResponse
from django.shortcuts import render


def posts(request):
    return HttpResponse('Страница с постами')
