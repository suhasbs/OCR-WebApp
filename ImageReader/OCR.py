import subprocess
import models
from OCRWebApp import settings
import cv2

def checkResolution(path):

	img = cv2.imread(path)
	if(img.shape[0]<500 and img.shape[1]<500):
		width = 500
		height = float(width)/img.shape[0]*img.shape[1]
		res_img = cv2.resize(img, (int(width), int(height)))
		cv2.imwrite(path, res_img)
		print 'resized'



def convertImageToText(path, imgid):

    checkResolution(path)

    a = models.ImageUploads.objects.filter(id=imgid)[0]
    a.status = 2
    a.save()
    # -text = pytesser.image_file_to_string(imageFile, graceful_errors=False)
    output_filename = settings.MEDIA_ROOT+'/Output_Folder/'+path.split('/')[-1].split('.')[0]
    args = ['tesseract', path, output_filename]
    proc = subprocess.Popen(args)
    retcode = proc.wait()
    a = models.ImageUploads.objects.filter(id=imgid)[0]
    a.status = 3
    a.save()