from django import forms


class contactForm(forms.Form):  # inherit from forms.Form
    name=forms.CharField() # field of field
    email=forms.EmailField()
    contact=forms.CharField()
    age=forms.IntegerField()
    birthday=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    CHOICE=[('B','BMW'),('M','Mercedez'),('T','Toyota')]
    vehicle=forms.ChoiceField(choices=CHOICE)
    dateTimeField=forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))