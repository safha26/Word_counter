from django import forms

class TextInputForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows':15, 'cols':50, 'placeholder': 'Enter your text here'}),label='')