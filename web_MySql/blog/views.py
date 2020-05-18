from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Post

def index(request):
    # query
    posts = Post.objects.all()
    #print(posts)
    categories = Post.objects.values('category').distinct()
    contex = {
        'title' : 'Blog',
        'heading' : 'Blog di myWebsite',
        'category' : 'ALL',
        'Categories' : categories,
        'Posts' : posts,
        'content' : 'ini adalah halaman Blog',
    }
    return render(request,'blog/index.html', contex)

def categoryPost(request, categoryInput):
    # query
    posts = Post.objects.filter(category=categoryInput)
    #print(posts)
    categories = Post.objects.values('category').distinct()
    #print(categories)
    contex = {
        'title' : 'Home Blog',
        'heading' : 'Blog di myWebsite',
        'category' : 'ALL',
        'Categories' : categories,
        'Posts' : posts,
        'content' : 'tampilkan berdasarkan category',
    }
    return render(request,'blog/category.html',contex)

def detailPost(request, slugInput):
    # query
    posts = Post.objects.all().get(slug=slugInput)
    #print(posts)
    categories = Post.objects.values('category').distinct()
    contex = {
        'title' : 'Blog',
        'heading' : 'Blog di myWebsite',
        'category' : 'ALL',
        'Categories' : categories,
        'Posts' : posts,
        'content' : 'ini adalah halaman Blog',
    }
    return render(request,'blog/detail.html',contex)

def jurnal(request):
    # query
    posts = Post.objects.filter(category='jurnal')
    contex = {
        'title' : 'Blog',
        'heading' : 'Blog di myWebsite',
        'category' : 'jurnal',
        'Posts' : posts,
    }
    return render(request,'blog/index.html', contex)

def berita(request):
    # query
    posts = Post.objects.filter(category='berita')
    contex = {
        'title' : 'Blog',
        'heading' : 'Blog di myWebsite',
        'category' : 'berita',
        'Posts' : posts,
    }
    return render(request,'blog/index.html', contex)

def blog(request):
    # query
    posts = Post.objects.filter(category='blog')
    contex = {
        'title' : 'Blog',
        'heading' : 'Blog di myWebsite',
        'category' : 'blog',
        'Posts' : posts,
    }

    return render(request,'blog/index.html', contex)

#def categoryPost(request, categoryInput):
    #post = Post.objects.filter(category = categoryInput)
    #return HttpResponse("category Post");

def singlePost(request, slugInput):
    posts = Post.objects.get(slug=slugInput)

    judul =     "<h1>{}</h1>".format(posts.judul)
    body =      "<p>{}</p>".format(posts.body)
    category =  "<p>{}</p>".format(posts.category)
    slug =  "<p>{}</p>".format(posts.slug)

    return HttpResponse(judul + body + category + slug)