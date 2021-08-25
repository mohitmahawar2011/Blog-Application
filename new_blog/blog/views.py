from django.shortcuts import render,redirect
from .models import Category,Blog
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .form import BlogForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):

    context = {'blogs':Blog.objects.all()}
    return render(request,'home.html',context)

def get_blog(request,id):
    context = {}
    try:
        blog_obj = Blog.objects.get(id=id)
        context['blog'] = blog_obj
    except Exception as e:
        print(e)

    return render(request,'detail_blog.html',context)

@login_required(login_url='/login/')
def show_all_blog(request):
    context = {'blogs': Blog.objects.filter(user= request.user)}
    return render(request,'show_all_blog.html',context)

@login_required(login_url='/login/')
def create_blog(request):
    context = {'form':BlogForm,'category': Category.objects.all()}
    # print(context['category'])
    if request.method == 'POST':
        form = BlogForm(request.POST)
        category = request.POST.get('category')
        title = request.POST.get('title')
        banner_image = request.FILES['banner_image']

        if form.is_valid():
            content = form.cleaned_data['content']

            Blog.objects.create(
                title = title,
                content = content,
                category = Category.objects.get(id=category),
                user = request.user,
                banner_image = banner_image
            )
            messages.success(request,'Your Blog Created...')
            return redirect('/create-blog/')

    return render(request,'create_blog.html',context)

@login_required(login_url='/login/')
def update_blog(request,id):
    context = {'category': Category.objects.all()}
    blog_obj = Blog.objects.get(id = id)
    if blog_obj.user != request.user:
        return redirect('/')
    initial_dict = {'content': blog_obj.content}
    form = BlogForm(initial=initial_dict)

    context['form'] = form
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            category = request.POST.get('category')
            title = request.POST.get('title')
            # banner_image = request.FILES['banner_image']


            if form.is_valid():
                content = form.cleaned_data['content']

                blog_obj = Blog.objects.get(id = id)
                blog_obj.title = title
                blog_obj.content = content
                blog_obj.category = Category.objects.get(id=category)
                # if banner_image:
                #     blog_obj.banner_image = banner_image
                blog_obj.save()
                messages.success(request,'Your Blog Updated...')
                return redirect('/create-blog/')


        # context['form'] = form
        # context['blog_obj'] = blog_obj

    except Exception as e:
        print(e)
    context['blog_obj'] = blog_obj
    return render(request,'update_blog.html',context)

@login_required(login_url='/login/')
def delete_blog(request,id):
    blog_obj = Blog.objects.get(id=id)
    if blog_obj.user != request.user:
        return redirect('/')
    blog_obj.delete()
    return redirect('/show-all-blog/')

def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username)
        if not user_obj.exists():
            messages.success(request, 'User not Found')
            return redirect('/login/')

        user_obj = authenticate(username=username,password=password)

        if not user_obj:
            messages.success(request, 'Invalid Cerdentials')
            return redirect('/login/')

        login(request,user_obj)
        return redirect('/')

    return render(request,'login.html')

def register_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username)
        if user_obj.exists():
            messages.success(request,'Username is taken')
            return redirect('/register/')

        user_obj = User.objects.filter(email=email)
        if user_obj.exists():
            messages.success(request, 'Email is taken')
            return redirect('/register/')

        user_obj = User(username=username,email=email)
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request, 'Your Account is Created...')
        return redirect('/login/')

    return render(request,'register.html')


def logout_attempt(request):
    logout(request)
    return redirect('/')

def about_page(request):
    return render(request,'about.html')