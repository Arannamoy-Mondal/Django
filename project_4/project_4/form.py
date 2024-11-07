from django import forms


class contactForm(forms.Form):  # inherit from forms.Form
    name=forms.CharField() # field of field
    email=forms.CharField()
    contact=forms.CharField()
    