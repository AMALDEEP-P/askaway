from django import forms
from .models import Answer


class AnswerForm(forms.ModelForm):
    """
    Answer form for creating and editing answers.
    """

    class Meta:
        """
        Meta class for the AnswerForm.
        """

        model = Answer
        fields = ["answer"]
