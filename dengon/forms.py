from django import forms

class dengonForm(forms.Form):
    #to
    nameTo = forms.CharField(
        label='nameTo',
        max_length=50,
        required=True,
        widget=forms.TextInput()
    )
