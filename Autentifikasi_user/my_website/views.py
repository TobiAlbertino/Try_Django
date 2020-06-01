from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# view method dengan internal permission check
def index(request):
    context = {
        'page_title' : 'Home',
    }
    template_name = None
    # print(request.user.is_authenticated)
    if request.user.is_authenticated:
        #logika untuk user
        template_name = 'index_user.html'
    else:
        # logika untuk anonymous user
        template_name = 'index_anonymous.html'

    return render(request, template_name, context)

def loginView(request):
    context = {
        'page_title' : 'LOGIN',
    }
    if request.method == 'POST':
        # print(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        # print(user)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')

    if request.method == 'GET':
        if request.user.is_authenticated:
            # logic untuk user
            return redirect('index')
        else:
            #logic untuk anonymous
            return render(request, 'login.html', context)
        
    # username_ucup = 'ucup'
    # password_ucup = 'apaaja123'

    # user = authenticate(request, username=username_ucup, password=password_ucup)
    # print(user)

    # login(request, user)
    # return render(request, 'login.html', context)

@login_required
def logoutView(request):
    context = {
        'page_title' : 'logout',
    }
    if request.method == 'POST':
        # print(request.POST)
        if request.POST['logout'] == 'Submit':
            logout(request)

        return redirect('index')

    return render(request, 'logout.html', context)