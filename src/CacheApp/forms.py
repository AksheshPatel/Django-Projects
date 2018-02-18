from django import forms
from .models import Word#,Findmeaning

class WordForm(forms.ModelForm):

    class Meta:
        model = Word
        fields = [
                "word_name",
                ]

# class WordMeaningForm(forms.ModelForm):

#     class Meta:
#         model = Word
#         fields = [
#                 "word_name",
#                 "word_meaning"
#                 ]