from .models import Video,Hall
from django import forms

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['url']
        labels = {'url':'Youtube Url'}

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=255,label='Search for Videos')
