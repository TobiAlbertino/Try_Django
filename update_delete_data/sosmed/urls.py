from django.urls import path, re_path
from . import views

app_name = 'Instagram'

urlpatterns = [
    re_path(r'^delete/(?P<delete_id>[0-9]+)$', views.delete, name='delete'),
    re_path(r'^update/(?P<update_id>[0-9]+)$', views.update, name='update'),
    # path('delete/<int:delete_id>/', views.delete, name='delete'),
    # path('update/<int:update_id>/', views.update, name='update'),
    path('create/', views.create, name='create'),
    path('', views.list, name='list'),

]