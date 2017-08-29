from django.forms import ModelForm

from .models import ImageUploads

class ImageUploadsForm(ModelForm):
    class Meta:
        model = ImageUploads
        #fields = '__all__'
        fields = ('img',)
