from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    """
    ImageForm that handles uploaded image
    """

    class Meta:
        model = Image
        fields = ("image",)