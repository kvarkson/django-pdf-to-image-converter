from django import forms

class PdfUploadForm(forms.Form):
    pdf_file = forms.FileField(
        label='Select a pdf file',
    )