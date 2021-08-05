from django.core import paginator
from django.shortcuts import redirect, get_object_or_404, render, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog

from django.utils import timezone
from .forms import BlogForm


def home(request):
    blogs = Blog.objects.order_by('-pub_date')
    paginator = Paginator(blogs,3)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    search = request.GET.get('search')
    if search == 'true':
        author = request.GET.get('writer')
        blogs2 = Blog.objects.exclude(writer=author)
        paginator = Paginator(blogs2,3)
        page = request.GET.get('page')
        blogs2 = paginator.get_page(page)
        return render(request,'home.html', {'blogs2':blogs2})
    
    
    return render(request, 'home.html',{'blogs':blogs})

def detail(request,id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html',{'blog':blog})

def new(request):
    form = BlogForm()
    return render(request,'new.html',{'form':form})

def create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        new_blog = form.save(commit = False)
        new_blog.pub_date = timezone.now()
        new_blog.save()
        return redirect('detail',new_blog.id)
    return redirect('home')
def edit(request,id):
    edit_blog = Blog.objects.get(id = id)
    form = BlogForm(instance = edit_blog)
    return render(request,'edit.html',{'blog':edit_blog, 'form':form})

def update(request,id):
    update_blog = Blog.objects.get(id=id)
    form = BlogForm(request.POST, request.FILES,instance = update_blog)
    if form.is_valid():
        update_blog = form.save(commit = False)
        update_blog.pub_date = timezone.now()
        update_blog.save()
        return redirect('detail',update_blog.id)
    return redirect('home')
def delete(request,id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')