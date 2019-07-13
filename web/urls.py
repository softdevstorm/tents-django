from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/<int:gallery_id>/', views.gallery, name='gallery')
]