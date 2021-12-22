from django import forms
from core.models import Shortener

class ShortenerForm(forms.ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(attrs={'id': 'long_url', 'placeholder': 'Enter your URL', 'class': 'form-control'}))

    class Meta:
        model = Shortener
        fields = ['long_url']