from django.shortcuts import render
from . import form 
from django.core import validators
from django import forms
def home(request):
    print(request.POST)
    if(request.POST):
        name=request.POST.get('userName')
        email=request.POST.get('userEmail')
        contact=request.POST.get('userContact')
        print(name)
        return render(request,'home.html',{'name':name,'email':email,'contact':contact})
    else:
        return render(request,'contact.html')

def aboutPage(request):
    print(request.GET)
    return render(request,'about.html')

def contactPage(request):
    print(request.POST)
    return render(request,'contact.html')

def signUpForms(request):
    return render(request,'signUpForm.html')

def formOfDjango(request):
    print(request.POST)
    tmp=form.contactForm(request.POST)
    return render(request,'builtInFormOfDjango.html',{'form':tmp})

# def output(request):
#     if request.method=='POST':
#        form1=form.logIn(request.POST)
#        password=request.POST.get('password')
#        confpass=request.POST.get('con')
#        print(password)
#        if form1.is_valid():
#            if confpass==password:
#               return render(request,'ouput.html',{'email':request.POST.get('email')})
#            else:
#                raise forms.ValidationError("Wrong Credential")
#     return render(request,'login.html',{'form':form1})
    
def Buit_in_validator_of_django_form(request):
    logInForm=form.logIn(request.POST)
    return render(request,'builtInValidator.html',{'form':logInForm})
        
def logInForm(request):
    form1=form.logIn(request.POST)
    return render(request,'login.html',{'form':form1})

def passwordVerification(request):
    if request.method=='POST':
       form1=form.logIn(request.POST)
       password=request.POST.get('password')
       confpass=request.POST.get('con')
       print(password)
       if form1.is_valid():
           if confpass==password:
              return render(request,'output.html',{'email':request.POST.get('email')})
           else:
               return render(request,'login.html',{'form':form1})
    return render(request,'login.html',{'form':form1})