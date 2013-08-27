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

            return HttpResponseRedirect(reverse('DjangoPdfToImageConverter.pdfconverter.views.index'))
    else:
        form = PdfUploadForm()

    pdf_files = PdfFile.objects.all()

    return render_to_response(
        'index.html',
        {'pdf_files': pdf_files, 'form': form},
        context_instance=RequestContext(request)
    )