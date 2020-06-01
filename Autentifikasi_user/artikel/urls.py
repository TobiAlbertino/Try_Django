from django.urls import path
from .views import artikelIndexView, artikeAddView, artikeAddView2, otongView

app_name = 'artikel'
urlpatterns = [
    path('otong/', otongView, name='otong'),
    path('add2/', artikeAddView2, name='add2'),
    path('add/', artikeAddView, name='add'),
    path('', artikelIndexView, name='index'),
]