from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
    return render(request, 'blog/post_list.html')


def post_list2(request):
    return HttpResponse('post_list2')
