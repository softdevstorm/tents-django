from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/<int:gallery_id>/', views.gallery, name='gallery'),
    path('change-photo', views.change_photo, name='change_photo'),
    path('delete-photo', views.delete_photo, name='delete_photo'),
    path('add-new-photo', views.add_new_photo, name='add_new_photo'),
]