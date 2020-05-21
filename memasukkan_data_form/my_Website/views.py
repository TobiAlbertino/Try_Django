from django.shortcuts import render

def index(request):
    context = {
        'page_title' : 'Home Page',
    }
    return render(request, 'index.html', context)