from django.shortcuts import render
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