from django.db import models

class PdfFile(models.Model):
    pdf_file = models.FileField(upload_to='pdfs/%Y/%m/%d')