import os

from django.db import models
from django.conf import settings

from PyPDF2 import PdfFileReader
from wand.image import Image


def make_upload_path(instance, filename):
	"""Generates upload path for FileField"""
	return settings.PDF_OUTPUT_FILES + "/%s" % (filename)


class PdfFile(models.Model):
    pdf_file = models.FileField(upload_to=make_upload_path)

    def convert_to_img(self):
    	filename = self.pdf_file.name
    	print 'filename: ' + filename
    	filepath = self.pdf_file.url
    	print 'filepath:' + filepath
    	output_dir = filepath + '_images/'
    	print 'output_dir:' + output_dir
    	os.mkdir(output_dir)
    	
    	input_file = PdfFileReader(file(filename, 'rb'))
    	for i in range(input_file.getNumPages()):
			with Image(filename = filepath + '[' + str(i) + ']') as img:
				img.save(filename = output_dir + str(i) + '.jpg')

