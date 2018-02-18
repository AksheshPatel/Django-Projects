from django import forms
from .models import WordName,WordMeaning

class WordForm(forms.ModelForm):

    class Meta:
        model = WordName
        fields = [
                "word_name",
                ]

class WordMeaningForm(forms.ModelForm):

    class Meta:
        model = WordMeaning
        fields = [
                "w_name",
                "w_meaning"
                ]