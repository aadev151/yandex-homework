from django import forms

from rating.models import Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = (Rating.score.field.name,)
        widgets = {
            Rating.score.field.name: forms.Select(
                attrs={'class': 'form-control'}
            )
        }
