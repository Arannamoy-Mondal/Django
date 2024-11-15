from django.shortcuts import render,redirect
from . import models
# Create your views here.

def home(request):
    student1 = models.student.objects.all()
    print(student1)
    return render(request,'home.html',{'data':student1})

def deleteStd(request,roll):
    student1=models.student.objects.get(pk=roll).delete()
    return redirect('homez')