"""my_Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    # re_path(r'^parameter/(?P<parameter1>[0-9]+)/(?P<parameter2>[0-9]+)$', views.ParameterView.as_view()),
    path('parameter/<int:parameter1>/<int:parameter2>/', views.ParameterView.as_view()),
    path('context/', views.ContextView.as_view()),
    path('default/', views.TemplateView.as_view(template_name='default.html')),
    path('', views.indexView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
]

# 1. membuat class view di views.py, tapi menggunakan template di url
# 2. jika halaman Statis, tidak ada perubahan apapun, maka kita lakukan TemplateView langsung pada urls.py
# 3. membuat views dengan context saja, kita menggunakan class templateview di views.py 
# 4. kita memasukkan parameter kedalam template, dengan menggunakan parameter regex