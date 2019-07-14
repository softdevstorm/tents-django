import os

from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo, Gallery


def index(request):
    gallery_list = Gallery.objects.all()

    context = {
        'gallery_list': gallery_list
    }

    return render(request, 'web/index.html', context=context)


def gallery(request, gallery_id):
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
        os.remove(origin_photo)
        photo.photo = request.FILES.get('image')
        photo.save()
        return HttpResponse({'success': 'success'}, status=200)
