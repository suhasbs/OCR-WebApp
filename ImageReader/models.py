


from __future__ import unicode_literals

from django.db import models

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    print filename
    return os.path.join('uploaded_images', filename)


def __str__(self):
    return self.filename

# Create your models here.
class ImageUploads(models.Model):
    img = models.ImageField(upload_to=get_file_path, )
    # hocr_file = models.CharField(max_length=100)
    status = models.IntegerField(default=0)
    filename = models.CharField(max_length=50)

    def __str__(self):
        return self.filename


import uuid
import os


