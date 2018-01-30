from django.contrib.auth import models
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post, PostTrash


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


def post_detail(requst, pk):
    try:
        post = Post.objects.get(pk=pk)
    except:
        return redirect('/')
    return render(requst, 'blog/post_detail.html', {"post":post})


def post_del(requst, pk):
    post = Post.objects.get(pk=pk)
    author = post.author.pk
    title = post.title
    content = post.content
    created_date = post.created_date
    published_date = post.published_date
    post.delete()

    # author = models.IntegerField()
    # title = models.CharField(max_length=200)
    # content = models.TextField(blank=True)
    # created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)
    t = PostTrash(author=author, title=title, content=content, created_date=created_date, published_date=published_date)
    t.save()

    return redirect('/list')


def trash_list(request):
    posts = PostTrash.objects.all().order_by('-created_date')
    context = {
        'posts': posts,
    }
    return render(
        request=request,
        template_name='blog/trash_list.html',
        context=context
    )


def trash_detail(requst, pk):
    try:
        post = PostTrash.objects.get(pk=pk)
    except:
        return redirect('trash/list')
    return render(requst, 'blog/trash_detail.html', {"post":post})


def trash_rollback(requst, pk):
    trash = PostTrash.objects.get(pk=pk)
    author = models.User.objects.get(pk=trash.author)
    title = trash.title
    content = trash.content
    created_date = trash.created_date
    published_date = trash.published_date
    trash.delete()

    # author = models.IntegerField()
    # title = models.CharField(max_length=200)
    # content = models.TextField(blank=True)
    # created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)
    p = Post(author=author, title=title, content=content, created_date=created_date, published_date=published_date)
    p.save()

    return redirect('/trash/list')
