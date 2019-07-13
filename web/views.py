from django.shortcuts import render
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