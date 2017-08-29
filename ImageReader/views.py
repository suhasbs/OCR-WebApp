# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from forms import ImageUploadsForm
from .models import ImageUploads
import thread
from OCRWebApp import settings
import OCR
# Create your views here.
def index(request):
	return render(request, 'ImageReader/index.html')

@csrf_exempt
def upload(request):
	print request.FILES
	form = ImageUploadsForm(request.POST, request.FILES)
	if form.is_valid():
	        print 'valid form'
	        rec_im = form.save(commit=True)
	        rec_im.filename = rec_im.img.url.split('/')[-1]
	        rec_im.status = 1
	        print rec_im.img.url
	        rec_im.save()
	response = {'recieved':1 ,'id':rec_im.id}
	path = rec_im.img.url[1:]	
	thread.start_new_thread(OCR.convertImageToText, (path,rec_im.id))
	return JsonResponse(response)

def get_data(request, imgid):
	imgfile = ImageUploads.objects.filter(id=imgid)[0]
	if imgfile.status != 3:
		return JsonResponse({'success':False})

	output = settings.MEDIA_ROOT+'/Output_Folder/'+imgfile.filename.split('.')[0]+'.txt'
	with open(output, 'r') as myfile:
		data=myfile.read()#.replace('\n', '')

	return JsonResponse({'success':True, 'data':data})