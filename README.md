django-pdf-to-image-converter
=============================

The app is solving the following issues:
1. Upload a pdf file.
2. Convert the file to series of images (for each page).
3. Compress the images to an archive.

#Install
You are going to need to install the following dependencies:

1. [Ghostscript](http://www.ghostscript.com) (if you do not have one installed)
2. [Freetype](http://www.freetype.org) (it should be on your system but you better check)
3. Django: <code>pip install django</code>
4. Wand (python bind for ImageMagic): <code>pip install wand</code>

#Usage

Just <code> python manage.py runserver</code> and be happy.