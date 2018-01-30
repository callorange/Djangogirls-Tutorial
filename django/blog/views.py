from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    html = '''
    '''
    return render(
        request=request,
        template_name='blog/post_list.html',
        context=context
    )
    # return render(request, 'blog/post_list.html', context)


def post_list2(request):
    return render(request, 'blog/notfound.html')


def post_detail(requst):
    return render(requst, 'blog/post_detail.html')
