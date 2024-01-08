from django import forms

class InputForm(forms.Form):
    firstname = forms.CharField(max_length=25)
    lastname = forms.CharField(max_length=25)
    city = forms.CharField(max_length=20)