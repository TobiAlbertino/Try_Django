from django.shortcuts import render

# Create your views here.

def index(request):
    contex = {
        'judul' : 'About Judul',
        'subjudul' : 'About',
        'kontributor' : 'Si Otong',
        'banner' : 'about/img/banner_about.png',
        'app_css' : 'about/css/style.css',
    }
    return render(request, 'about/index.html', contex)