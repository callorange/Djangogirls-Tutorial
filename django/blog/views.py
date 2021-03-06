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


def post_del(request, pk):
    if request.method == 'POST':
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


def post_add(request):
    form_err = ''
    if request.method == 'POST':
        if request.POST['title'].strip() == '' or request.POST['content'].strip() == '':
            form_err = "title or content is blank!!"
        else:
            frm = request.POST
            post = Post.objects.create(
                author=request.user,
                title=frm["title"],
                content=frm["content"],
            )
            # return redirect('post-detail', pk=post.pk)
            return redirect(f'/post/{post.pk}')
    return render(request, 'blog/post_add_edit.html', {'form_err': form_err})


def post_edit(request, pk):
    if not Post.objects.filter(pk=pk).exists():
        return redirect('post-list')

    post = Post.objects.get(pk=pk)
    form_err = ''
    if request.method == 'POST':
        if request.POST['title'].strip() == '' or request.POST['content'].strip() == '':
            form_err = "title or content is blank!!"
        elif request.user == post.author:
            post.title = request.POST['title']
            post.content = request.POST['content']
            post.save()
            return redirect('post-detail', pk=pk)
    return render(request, 'blog/post_add_edit.html', {'post': post, 'form_err': form_err})


def trash_list(request):
    posts = PostTrash.objects.using('external').all().order_by('-created_date')
    context = {
        'posts': posts,
    }
    return render(
        request=request,
        template_name='blog/trash_list.html',
        context=context
    )


def trash_detail(request, pk):
    try:
        post = PostTrash.objects.using('external').get(pk=pk)
    except Exception:
        return redirect('trash/list')
    return render(request, 'blog/trash_detail.html', {"post": post})


def trash_rollback(request, pk):
    if request.method == 'POST':
        trash = PostTrash.objects.using('external').get(pk=pk)
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
