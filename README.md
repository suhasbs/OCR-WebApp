# OCR-WebApp

## About Project
This is a simple client server based Optical Character Recognition Web Appliction written in Django (Python).
This application uses Tesseract Open Source OCR API with Leptonica. 

The features of the applicaton are:
- Image Upload to server
- Run the tesseract API on the image
- Return the text recognised from the image to the user

## Setting Up Project
This has been clearly explained in CONTRIBUTING.md

## Running the Project
- Set up the required environment by installing the libraries mentioned in CONTRIBUTING.md
- Download the source code
- In OCRWebApp/OCRWebApp/settings.py , change the path MEDIA_ROOT to the (path_to_project_directory)/OCRWebApp/media
- Install Django using `pip install django`
- Inside the root folder, run the command `python manage.py runserver`
- Open a Web Browswer and in the address bar, type localhost:8000/imagereader/
- This should display a HTML Page

## Testing the Project
- On successful display of the HTML Page, click Choose File and select an image(preferably JPEG or PNG) with clear text.
- On selecting, the image will be displayed on the browser.
- Then click OCR IMAGE
- The image is uploaded to the server and is OCRed
- The text in the image is displayed next to the image
- Click [here](https://drive.google.com/open?id=0B6pQuwk1uPmHM2VoTmQ4MUJPa1E) for demo

## Limitations
- Presently works only for English language but can be extended to any language by adding traineddata files of different languages
- The image should be of good clarity and text should not be too small
- Works well over images with only text

