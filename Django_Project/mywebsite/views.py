from django.http import HttpResponse
from django.shortcuts import render

#method view
def index(request):
    contex = {
    'judul' : 'Selamat datang',
    'subjudul' : 'Kelas Terbuka',
    'kontributor' : 'Tobi',
    'banner' : 'img/banner_home.png',
    'nav': [
            ['/', 'Home'],
            ['/about', 'About'],
            ['/blog', 'Blog'],
            ['/contact', 'Contact']
        ]
    
    }
    return render(request, 'index.html', contex)