from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import loginform, addblogform, addpostform, signupform
from django.contrib.auth.decorators import login_required
from .models import Posts,Blog
from django.contrib.auth import authenticate, login, logout




# Create your views here.
def home(request):
    posts = Posts.objects.order_by('-datetime_modified')
    return render(request , "posts/home.html" , {'posts' : posts})

def login_site(request):
    if not request.user.is_authenticated():
    #     redirect('/')
        if request.method=='POST':

            form=loginform(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                userobj = User.objects.get(email = email)
                user = authenticate(username = userobj.username , password = password)
                if user is not None:
                    login(request, user)
                    return redirect("/")
                else:
                    return redirect("/login")
        else:
            form = loginform()
        
        return render(request,'forms/login.html',{'form':form,})
    else:
        return redirect('/')

def signup(request):
    form = signupform(request.POST)
    
    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect('/') 

    else:
        form= signupform()
    
    return render(request, 'forms/signup.html', {'form': form,})

####login required####

@login_required
def addpost(request):
    if request.method=='POST':
    
        form = addpostform(request.POST)
    
        if form.is_valid():
            Posts.objects.create(
                author=request.user,
                title=form.cleaned_data['title'],
                url=form.cleaned_data['url'],
                description=form.cleaned_data['description'],
            )
            return redirect("/")
    
    else:
        form = addpostform()
    
    return render(request,'forms/addp.html',{'form':form,})

@login_required
def blogs(request):
    blogs = Blog.objects.order_by('-datetime_added')
    return render(request,'posts/blogs.html',{'blogs':blogs,})

@login_required
def add_b(request):
    # print('hell1')
    if request.method == 'POST':
        form = addblogform(request.POST)
        if form.is_valid():
            # form.save()
            Blog.objects.create(
                author = request.user,
                blogtitle = form.cleaned_data['blogtitle'],
                content = form.cleaned_data['content'],
            )
            # print("Hello")
            return redirect('/blogs')
    else:
        form = addblogform()
        # print("form", form)
    return render(request,'forms/addb.html',{'form':form,})
    
@login_required
def delete_b(request,pk):
    Blog.objects.get(pk = pk).delete()
    return redirect('/blogs/')


# @login_required
# def delete_post(request,pk):
#     Post.objects.get(pk=pk,user=request.user).delete()
#     redirect('myposts/')

@login_required
def edit_b(request,pk):
    blog=Blog.objects.get(pk = pk)
    if request.method=='POST':
        form=addblogform(request.POST)
        if form.is_valid():    
            author = request.user
            blog.blogtitle = form.cleaned_data['blogtitle']
            blog.content = form.cleaned_data['content']
            blog.save()
            return redirect('/blogs')
    else:
        form = addblogform(initial={'blogtitle': blog.blogtitle,'content':blog.content,})
    return render(request,"forms/addb.html",{'form':form,})

@login_required
def edit_p(request,pk):
    post=Posts.objects.get(pk = pk)
    if request.method=='POST':
        form=addpostform(request.POST)
        if form.is_valid():    
            # form=addpostform(request.POST)
            author = request.user
            post.title = form.cleaned_data['title']
            post.description = form.cleaned_data['description']
            post.url = form.cleaned_data['url']
            post.save()
            return redirect('/')
    else:
        form = addpostform(initial={'title':post.title,'description':post.description,'url':post.url})
    return render(request,"forms/addp.html",{'form':form,})

@login_required
def delete_p(request,pk):
    # Posts.objects.get(pk = pk, user = request.user).delete()
    Posts.objects.get(pk = pk).delete()
    return redirect('/')       

@login_required
def logout_req(request):
    logout(request)
    return redirect("/")