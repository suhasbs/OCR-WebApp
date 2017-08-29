import subprocess
import models
from OCRWebApp import settings
def convertImageToText(path, imgid):
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