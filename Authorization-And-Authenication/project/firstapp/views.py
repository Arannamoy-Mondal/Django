# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
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
            # print(form1.cleaned_data)
            return redirect('logIn')
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
    

def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form1=form.EditForm(request.POST, instance=request.user)
            if form1.is_valid():
                messages.success(request, 'Account updated successfully')
                form1.save()
        else:
            form1 = form.EditForm(instance=request.user)
        return render(request, './profile.html', {'form': form1})
    else:
        return redirect('signup')


def logOut(req):
    logout(req)
    return redirect('home')

def passChange(req):
    if not req.user.is_authenticated:
        return redirect('logIn')
    if req.method=='POST':
        form1=PasswordChangeForm(user=req.user,data=req.POST)
        if form1.is_valid():
            form1.save()
            update_session_auth_hash(req,form1.user)
            return redirect('logOut')
    else:
        form1=PasswordChangeForm(req)
    return render(req,'changePassword.html',{'form':form1})

def passChangeWithOutOldPassWord(req):
    if not req.user.is_authenticated:
        return redirect('logIn')
    if req.method=='POST':
        form1=SetPasswordForm(user=req.user,data=req.POST)
        if form1.is_valid():
            form1.save()
            update_session_auth_hash(req,form1.user)
            return redirect('logOut')
    else:
        form1=SetPasswordForm(req)
    return render(req,'changePassword.html',{'form':form1})


def editUserData(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form1 =form.EditForm(request.POST, instance=request.user)
            if form1.is_valid():
                messages.success(request, 'Account updated successfully')
                form1.save()
                print(form1.cleaned_data)
        else:
            form1 = form.EditForm()
        return render(request, './profile.html', {'form': form1})
    else:
        return redirect('signup')