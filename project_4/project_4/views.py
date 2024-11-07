from django.shortcuts import render


def home(request):
    print(request.GET)
    return render(request,'home.html')

def aboutPage(request):
    print(request.GET)
    return render(request,'about.html')

def contactPage(request):
    print(request.GET)
    return render(request,'contact.html')