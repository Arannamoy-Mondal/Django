# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from .import form
def home(req):
    return render(req,'home.html')
def signUp(req):
    if req.user.is_authenticated:
        return redirect('profile')
    if req.method=='POST':
        form1=form.RegisterForm(req.POST)
        if form1.is_valid():
            # form1.save(commit=False) for not save in database
            messages.success(req,'Successfully')
            form1.save()
            print(form1.cleaned_data)
    else:
        return render(req,'signUp.html',{'form':form.RegisterForm()})
    return render(req,'signUp.html',{'form':form1})


def logIn(req):
    if req.user.is_authenticated:
        return redirect('profile')
    if req.method=='POST':
        form=AuthenticationForm(request=req,data=req.POST)
        if form.is_valid():
            name=form.cleaned_data['username']
            userpassword=form.cleaned_data['password']
            user=authenticate(username=name,password=userpassword)# is user available on database or not
            if user is not None:
                login(req,user)
                return redirect('profile')
            else:
                return render(req,'./login.html',{'form':AuthenticationForm()})
        # else:
            # return render(req,'./login.html',{'form':AuthenticationForm()})
    else:
        form=AuthenticationForm()
    return render(req,'./login.html',{'form':form})
    

def profile(req):
    if req.user.is_authenticated:
       return render(req,'./profile.html',{'user':req.user})
    else:
        return redirect('home')


def logOut(req):
    logout(req)
    return redirect('home')