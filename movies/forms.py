from django import forms
from .models import Genre, Movie

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'genre']