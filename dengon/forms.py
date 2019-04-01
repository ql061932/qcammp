from django import forms

class dengonForm(forms.Form):
    #nameTo
    nameTo = forms.CharField(
        label='nameTo',
        max_length=50,
        required=True,
        widget=forms.TextInput()
    )
    #nameFrom
    nameFrom = forms.CharField(
        label='nameFrom',
        max_length=50,
        required=True,
        widget=forms.TextInput()
    )
    #nameTakenBy
    nameFrom = forms.CharField(
        label='nameTakenBy',
        max_length=50,
        required=True,
        widget=forms.TextInput()
    )
