# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from DjangoPdfToImageConverter.pdfconverter.forms import PdfUploadForm
from DjangoPdfToImageConverter.pdfconverter.models import PdfFile

def index(request):
    # Handle file upload
    if request.method == 'POST':
        form = PdfUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_pdf = PdfFile(pdf_file = request.FILES['pdf_file'])
            new_pdf.save()

            # convert to jpg file after uploading
            # if you don't pass parameters then the images
            # will have the actual size
            new_pdf.convert_to_jpg()

            # convert to png file after uploading
            # if you need to resize the image just call specify it's size
            # like new_pdf.convert_to_png(200, 400) 
            # will return 200x400 px image
            new_pdf.convert_to_png(200, 400)

            return HttpResponseRedirect(reverse('DjangoPdfToImageConverter.pdfconverter.views.index'))
    else:
        form = PdfUploadForm()

    pdf_files = PdfFile.objects.all()

    return render_to_response(
        'index.html',
        {'pdf_files': pdf_files, 'form': form},
        context_instance=RequestContext(request)
    )