from django.shortcuts import render


def index(request):
    context = {
        'heading' : 'Home ',
        'content' : 'Ini adalah Home',
    }
    return render(request, 'index.html', context)