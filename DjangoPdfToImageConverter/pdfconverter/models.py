# -*- coding: utf-8 -*-
import os

from django.db import models
from django.conf import settings

from PyPDF2 import PdfFileReader
from wand.image import Image

from DjangoPdfToImageConverter.pdfconverter.extra import ContentTypeRestrictedFileField


def make_upload_path(instance, filename):
	"""Generates upload path for FileField"""
	return settings.PDF_OUTPUT_FILES_URL + "/%s" % (filename)


class PdfFile(models.Model):
    pdf_file = ContentTypeRestrictedFileField(
        upload_to=make_upload_path,
        content_types=['application/pdf'],
        max_upload_size=5242880
    )

    def convert_to_png(self):
    	self.__convert_to_img__('png')

    def convert_to_jpg(self):
    	self.__convert_to_img__('jpg')

    def __convert_to_img__(self, format='jpg'):
    	filename = self.pdf_file.name
    	filepath = settings.MEDIA_ROOT + '/' + filename
    	output_dir = filepath + '_' + format + '/'
    	os.mkdir(output_dir)
    	
    	input_file = PdfFileReader(file(filepath, 'rb'))
    	for i in range(input_file.getNumPages()):
			with Image(filename = filepath + '[' + str(i) + ']') as img:
				img.format = format
				img.save(filename = output_dir + str(i) + '.' + format)

