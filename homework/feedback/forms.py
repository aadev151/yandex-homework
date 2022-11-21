from django import forms
from feedback.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [Feedback.text.field.name, ]
        widgets = {
            Feedback.text.field.name: forms.Textarea(
                attrs={'class': 'form-control'}
            )
        }
