from django import forms


class contactForm(forms.Form):  # inherit from forms.Form
    name=forms.CharField(label="Name",initial="Your Name",required=True,help_text="Full Name")
    email=forms.EmailField(label="Email",initial="Your Email",required=True,help_text="Enter your email")
    contact=forms.CharField()
    age=forms.IntegerField(required=False) # when required=False it is not necessary to fill up.
    birthday=forms.DateField(widget=forms.DateInput(attrs={'type':'date'})) # 
    CHOICE=[('B','BMW'),('M','Mercedez'),('T','Toyota')]
    vehicle=forms.ChoiceField(choices=CHOICE)
    dateTimeField=forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))