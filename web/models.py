from django.db import models


# Create your models here.
class Gallery(models.Model):
    gallery_title = models.CharField(max_length=200, null=True, blank=False)
    gallery_image = models.ImageField(upload_to='gallery', null=True, blank=False)

    class Meta:
        db_table = 'gallery'

    def __str__(self):
        """TODO: Docstring for __repr__.
        :returns: TODO
        """
        return self.gallery_title


class Photo(models.Model):
    name = models.CharField(max_length=400, blank=False, default='')
    photo = models.ImageField(upload_to='gallery/photos/', null=True, blank=False)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    class Meta:
        db_table = 'gallery_photo'

    def __str__(self):
        """TODO: Docstring for __repr__.
        :returns: TODO
        """
        return self.name
