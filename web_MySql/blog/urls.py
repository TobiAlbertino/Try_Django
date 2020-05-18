from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^post/(?P<slugInput>[\w-]+)', views.detailPost),
    re_path(r'^category/(?P<categoryInput>[\w-]+)', views.categoryPost),

    #re_path(r'^berita/$', views.berita),
    #re_path(r'^blog/$', views.blog),
    #re_path(r'^jurnal/$', views.jurnal),
    #re_path(r'^(?P<categoryInput>[\w-]+)/$', views.categoryPost),
    #re_path(r'^post/(?P<slugInput>[\w-]+)/$', views.singlePost),

]