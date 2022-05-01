from django import forms
from ckeditor.widgets import CKEditorWidget


class ArticuloFormulario(forms.Form):
    titulo=forms.CharField(max_length=60)
    abstract=forms.CharField(max_length=280)
    articulo=forms.CharField(widget = CKEditorWidget())