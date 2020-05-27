from django.urls import path

from .views import (
    ArtikelListView, 
    ArtikelDetailView, 
    ArtikelKategoriListView, 
    ArtikelCreateView, 
    ArtikelManageView,
    ArtikelDeleteView,
    ArtikelUpdateView
)

app_name = 'artikel'
urlpatterns = [
    path('manage/update/<int:pk>/', ArtikelUpdateView.as_view(), name='update'),
    path('manage/delete/<int:pk>/', ArtikelDeleteView.as_view(), name='delete'),
    path('manage/', ArtikelManageView.as_view(), name='manage'),
    path('tambah/', ArtikelCreateView.as_view(), name = 'create'),
    path('kategori/<str:kategori>/<int:page>', ArtikelKategoriListView.as_view(), name='category'),
    path('detail/<slug:slug>', ArtikelDetailView.as_view(), name='detail'),
    path('<int:page>', ArtikelListView.as_view(), name='list'),
]