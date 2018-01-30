from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
    response = '<html><body><h1>Post List</h1><p>post 목록을 보여줄 예정입니다.</p></body></html>'
    return HttpResponse(response)


def post_list2(request):
    return HttpResponse('post_list2')
