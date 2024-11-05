from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def global1(request):
    return render(request,'index.html')