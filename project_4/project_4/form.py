from django import forms
from django.core import validators

class contactForm(forms.Form):  # inherit from forms.Form
    name=forms.CharField(label="Name",initial="Your Name",required=True,help_text="Full Name",widget=forms.TextInput(attrs={'placeholder':'Enter your name:'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Enter email'}),required=True)
    def clean_name(self):
        userName=self.cleaned_data['name']
        if len(userName)<6:
            raise forms.ValidationError("Enter atleast 6 character:")
        return userName
    def clean_email(self):
        userEmail=self.cleaned_data['email']
        if '.com' not in userEmail:
            raise forms.ValidationError('Enter .com mail')
        return userEmail 
    

class logIn(forms.Form):
    #name=forms.CharField(validators=[validators.MinLengthValidator(6,message="At least 6 character.")])
    email=forms.CharField(validators=[validators.EmailValidator(message="Enter a valid mail"),validators.MinLengthValidator(8)])
    password=forms.CharField(label='Password',validators=[validators.MaxLengthValidator(6,message="At most 6 character"),validators.MinLengthValidator(3,message="At least 3 character")])
    #age=forms.IntegerField(label='Age',validators=[validators.MaxValueValidator(52,message="For CEO position your age must be between 20 to 52. "),validators.MinValueValidator(20,message="For CEO position your age must be between 20 to 52. ")])
    #file=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'])])
    con=forms.CharField(label="Confirm Password",validators=[validators.MaxLengthValidator(6)])
    # def clean(self):
    #     cleaned_data=super().clean()
    #     valPass=self.cleaned_data['password']
    #     confirmPass=self.cleaned_data['conf']
    #     if valPass!=confirmPass:
    #         raise forms.ValidationError("Password Does Not Match")
        


























    # name=forms.CharField(label="Name",initial="Your Name",required=True,help_text="Full Name",widget=forms.TextInput(attrs={'placeholder':'Enter your name:'}))
    # email=forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Enter email'}),required=True)
    # contact=forms.CharField()
    # age=forms.IntegerField(required=False,disabled=True) # when required=False it is not necessary to fill up and disabled true means user not able not fill up.
    # birthday=forms.DateField(widget=forms.DateInput(attrs={'type':'date'})) # 
    # CHOICE=[('B','BMW'),('M','Mercedez'),('T','Toyota')]
    # vehicle=forms.ChoiceField(choices=CHOICE)
    # forRadioButton=forms.ChoiceField(choices=CHOICE,widget=forms.RadioSelect)
    # dateTimeField=forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'})) 
    # message=forms.CharField(widget=forms.Textarea) # for create text area
    # CHOICES=[('M','Mercedez'),('S','Scania'),('V','Volvo')]
    # vehicles=forms.MultipleChoiceField(label='For multiple choice',choices=CHOICES)
    # forCheckBox=forms.MultipleChoiceField(label='For check box',choices=CHOICES,widget=forms.CheckboxSelectMultiple) # for checkbox