from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required


#	Create	your	views	here.

def home(request):
    posts = Post.objects.all()

    return render(request,	'blog/home.html', {'posts':posts})

@login_required(login_url="accounts:login")
def new(request):
    if request.method == "POST":
       title = request.POST['title']
       content = request.POST['content']


       new_post = Post.objects.create(
           title=title,
           content=content,
           author=request.user 
           )
       return redirect('blog:detail', new_post.pk)
  
    return render(request, 'blog/new.html')


@login_required(login_url="accounts:login")
def detail(request,	post_pk):
    post = Post.objects.get(pk=post_pk)
   
    if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(
            post=post,
            content=content
        )
        return redirect('blog:detail', post_pk)

    return render(request, 'blog/detail.html', {'post':post})


@login_required(login_url="accounts:login")
def update(request,	post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
       title = request.POST['title']
       content = request.POST['content']
       Post.objects.filter(pk=post_pk).update(
           title=title,
           content=content,
           author=request.user
       )
       return redirect('blog:detail', post_pk)


    return render(request, 'blog/update.html', {'post':post})


@login_required(login_url="accounts:login")
def delete(request,	post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    
    return redirect('blog:home')


@login_required(login_url="accounts:login")
def deleteComment(request, post_pk, comment_pk):
    comment = Comment.objects.filter(pk=comment_pk)
    comment.delete()
    return redirect('blog:detail', post_pk)
