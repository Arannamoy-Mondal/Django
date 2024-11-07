from django.shortcuts import render
from . import form 
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

def output(request):
    pass
    tmp=form.contactForm(request.POST)
    if tmp.is_valid(): # check that this form input is valid or invalid
        print(tmp.cleaned_data) # just take raw data no HTML tag
        return render(request,'output.html',{'form':tmp})
