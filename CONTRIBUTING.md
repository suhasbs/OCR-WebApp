Setting Up the Project


I. Installing Tesseract and Leptonica Libraries:
	

This project uses the latest version of Tesseract(4.00.00 alpha), which is available in the official GitHub Repository and Leptonica(1.74.4). Please follow these steps to set up these libraries on your Linux Systems. Leptonica has to be compiled from source for newer versions. 

Step 1: Install libraries required for Tesseract and Leptonica
sudo apt-get install python-distutils-extra tesseract-ocr tesseract-ocr-eng libopencv-dev libtesseract-dev libleptonica-dev python-all-dev swig libcv-dev python-opencv python-numpy python-setuptools build-essential subversion
sudo apt-get install autoconf automake libtool
sudo apt-get install libpng12-dev libjpeg62-dev libtiff4-dev zlib1g-dev

Step 2: Download Leptonica	
wget http://www.leptonica.com/source/leptonica-1.74.1.4.tar.gz 

Step 3: Unpack and build downloaded Leptonica archive:
tar xvf leptonica-1.74.tar.gz
cd leptonica-1.74
./configure
make
sudo make install

Step 4: Install Tesseract over Leptonica
git clone https://github.com/tesseract-ocr/tesseract.git
cd tesseract
sudo apt-get install autoconf-archive
./autogen.sh
./configure --enable-debug
LDFLAGS="-L/usr/local/lib" CFLAGS="-I/usr/local/include" make
sudo make install
sudo ldconfig

Step 5: You can check tesseract version by typing tesseract -v in a terminal. If all steps were successful, it should look something like this:
tesseract 4.00.00alpha-241-g6f83ba0
leptonica-1.74.1
libjpeg 8d (libjpeg-turbo 1.3.0) : libpng 1.2.50 : libtiff 4.0.3 : zlib 1.2.8
Found AVX
Found SSE

Step 6: Download eng.traineddata from 
https://github.com/tesseract-ocr/tessdata/blob/master/eng.traineddata copy it to the folder
/usr/local/share/tessdata/


  

