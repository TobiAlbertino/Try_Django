from django.urls import path, re_path
from . import views

app_name = 'sosmed'

urlpatterns = [
    # re_path(r'^delete/(?P<delete_id>[0-9]+)$', views.delete, name='delete'),
    # re_path(r'^update/(?P<update_id>[0-9]+)$', views.update, name='update'),
    # path('delete/<int:delete_id>/', views.delete, name='delete'),
    path('delete/<int:delete_id>/', views.SosmedDeleteView.as_view(), name='delete'),
    path('update/<int:update_id>/', views.SosmedFormView.as_view(mode = 'update'), name='update'),
    path('create/', views.SosmedFormView.as_view(mode = 'create'), name='create'),
    # path('', views.list, name='list'),
    path('', views.SosmedListView.as_view(), name='list'),

]