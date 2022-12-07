from django import forms

from rating.models import Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('score',)
        widgets = {'score': forms.Select(attrs={'class': 'form-control'})}
