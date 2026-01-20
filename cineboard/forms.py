# movies/forms.py
from django import forms
from .models import Movie

class MovieCreateForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["title", "description", "genres", "release_date"]  # нет rating и tags
        widgets = {
            "release_date": forms.DateInput(attrs={"type": "date"}),
        }