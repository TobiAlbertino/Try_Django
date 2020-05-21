from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    contex = {
        'judul' : 'Kelas Terbuka',
        'subjudul' : 'Blog',
        'kontributor' : 'Mario ucup',
        'banner' : 'blog/img/banner_blog.png',
        'app_css' : 'blog/css/style.css',
    }
    return render(request, 'blog/index.html', contex)

def recent(request):
    return HttpResponse('<h1>ini adalah recent post </h1>')

def news(request):
    contex = {
        'judul' : 'News',
        'kontributor' : 'Otong',
    }
    return render(request, 'blog/index.html', contex)
    
def cerita(request):
    contex = {
        'judul' : 'Cerita',
        'kontributor' : 'sandra bulogs',
    }
    return render(request, 'blog/index.html', contex)