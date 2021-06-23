from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm


def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST)
        #If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()

            #Redirect to Home
            return HttpResponseRedirect('/')

        else:
            #No Show Error
            return HttpResponseRedirect(form.errors.as_json())

    # Get all posts, limit = 20
    posts = Post.objects.all()[:20]

    # Show
    return render(request, 'posts.html',
                  {'posts': posts})


def delete(request, id):
    # find post
    print('hello world')
    post = Post.objects.get(id = id)
    post.delete()
    return HttpResponseRedirect('/')
    
def edit(request, id):
     post = Post.objects.get(id = id)
     print(post)
     if request.method == 'POST':
         form = PostForm(request.POST, instance=post)
         if form.is_valid():
             form.save()
             return HttpResponseRedirect('/')
         else:
             return HttpResponseRedirect(form.errors.as_json())
     else:
    # Show editting screen
        form = PostForm
        return render(request, 'edit.html',
        {'post': post, 'form': form})

def like(request, id):
    # find post
    post = Post.objects.get(id = id)
    new_likecount=post.like_count +1 
    post.like_count=new_likecount
    print(post.like_count)
    post.save()
    return HttpResponseRedirect('/')
           
