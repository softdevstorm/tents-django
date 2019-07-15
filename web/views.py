import os

from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from .models import Photo, Gallery


def index(request):
    gallery_list = Gallery.objects.all()

    context = {
        'gallery_list': gallery_list
    }

    return render(request, 'web/index.html', context=context)


def gallery(request):
    render(request, 'web/gallery_content.html')


def gallery_detail(request, gallery_id):
    gallery = Gallery.objects.get(pk=gallery_id)
    photos = gallery.photo_set.all()

    context = {
        'photos': photos
    }

    return render(request, 'web/gallery_content.html', context=context)


def change_photo(request):
    if request.method == 'POST':
        photo_id = int(request.POST.get('photo_id'))
        photo = Photo.objects.get(id=photo_id)
        origin_photo = photo.photo.path
        try:
            os.remove(origin_photo)
        except Exception as e:
            pass
        photo.photo = request.FILES.get('image')
        photo.save()
        return HttpResponse({'success': 'success'}, status=200)


def delete_photo(request):
    if request.method == 'POST':
        photo_id = int(request.POST.get('photo_id'))
        photo = Photo.objects.get(id=photo_id)
        try:
            os.remove(photo.photo.path)
        except Exception as e:
            pass
        photo.delete()
        return HttpResponse({'success': 'success'}, status=200)


def add_new_photo(request):
    if request.method == 'POST':
        gallery_id = int(request.POST.get('gallery_id'))
        gallery = Gallery.objects.filter(id=gallery_id).first()
        photo = Photo.objects.create(
            name=request.POST.get('name'),
            photo=request.FILES.get('image'),
            gallery=gallery
        )

        return HttpResponse({'success': 'success'}, status=200)
