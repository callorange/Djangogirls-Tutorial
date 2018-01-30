from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post


def post_list(request):
    posts = Post.objects.all().order_by('-created_date')
    context = {
        'posts': posts,
    }
    return render(
        request=request,
        template_name='blog/post_list.html',
        context=context
    )
    # return render(request, 'blog/post_list.html', context)


def post_list2(request):
    return render(request, 'blog/notfound.html')


def post_detail(requst, pk):
    try:
        post = Post.objects.get(pk=pk)
    except:
        return redirect('/')
    return render(requst, 'blog/post_detail.html', {"post":post})
