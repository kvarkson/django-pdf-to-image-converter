django-pdf-to-image-converter
=============================

####The app is solving the following issues:

1. Upload a pdf file
2. Convert the file to series of images (for each page)
3. Compress the images to an archive

Inspired by [minimal-django-file-upload-example](https://github.com/doph/minimal-django-file-upload-example)

#Install
You are going to need to install the following dependencies:

1. [ImageMagic](http://www.imagemagick.org/script/index.php)
2. [Ghostscript](http://www.ghostscript.com) (if you do not have one installed)
3. [Freetype](http://www.freetype.org) (it should be on your system but you better check)
4. Django: <code>pip install django</code>
5. Wand (python bind for ImageMagic): <code>pip install wand</code>
6. PyPDF2: <code>pip install PyPDF2</code>

#Usage

Just got to terminal and run:
<code>python manage.py syncdb</code>
and
<code>python manage.py runserver</code> and be happy.

#License
The MIT License

Copyright (c) 2013 Stas Gorodnichenko

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.