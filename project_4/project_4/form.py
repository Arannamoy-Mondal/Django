from django import forms


class contactForm(forms.Form):  # inherit from forms.Form
    name=forms.CharField(label="Name",initial="Your Name",required=True,help_text="Full Name",widget=forms.TextInput(attrs={'placeholder':'Enter your name:'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Enter email'}),required=True)
    contact=forms.CharField()
    age=forms.IntegerField(required=False,disabled=True) # when required=False it is not necessary to fill up and disabled true means user not able not fill up.
    birthday=forms.DateField(widget=forms.DateInput(attrs={'type':'date'})) # 
    CHOICE=[('B','BMW'),('M','Mercedez'),('T','Toyota')]
    vehicle=forms.ChoiceField(choices=CHOICE)
    forRadioButton=forms.ChoiceField(choices=CHOICE,widget=forms.RadioSelect)
    dateTimeField=forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'})) 
    message=forms.CharField(widget=forms.Textarea) # for create text area
    CHOICES=[('M','Mercedez'),('S','Scania'),('V','Volvo')]
    vehicles=forms.MultipleChoiceField(label='For multiple choice',choices=CHOICES)
    forCheckBox=forms.MultipleChoiceField(label='For check box',choices=CHOICES,widget=forms.CheckboxSelectMultiple) # for checkbox