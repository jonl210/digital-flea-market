from django import forms

class ImageFieldForm(forms.Form):
    name = forms.CharField()
    imageField = forms.ImageField()
