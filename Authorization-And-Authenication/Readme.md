<ol id="topic">
<li><a href="#signUp">SignUp</a></li>
<li><a href="#logIn">Login</a></li>
<li><a href="#profile">Profile</a></li>
<li><a href="#logOut">LogOut</a></li>
<li><a href="#PasswordChangeWithoutOldPassword">Password Change Without Old Password</a></li>
<li><a href="#PasswordChangeWithOldPassword">Password Change With Old Password</a></li>
<li><a href="#editProfile">Edit Profile</a></li>
</ol>


<div id="signUp">
    <li><a href="#topic">Topic</a></li>

```py

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

```
</div>

<div id="logIn">
    <li><a href="#topic">Topic</a></li>

```py
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
```
</div>

<div id="profile">
    <li><a href="#topic">Topic</a></li>

```py
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
```

</div>


<div id="logOut">
    <li><a href="#topic">Topic</a></li>

```py
    def logOut(req):
    logout(req)
    return redirect('home')
```

</div>

<div id="PasswordChangeWithOldPassword">
    <li><a href="#topic">Topic</a></li>

```py
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
```

</div>

<div id="PasswordChangeWithoutOldPassword">
    <li><a href="#topic">Topic</a></li>

```py
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
```

</div>

<div id="editProfile">
    <li><a href="#topic">Topic</a></li>

```py
    def editUserData(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form1 =form.EditForm(request.POST,instance=request.user)
            if form1.is_valid():
                messages.success(request, 'Account updated successfully')
                form1.save()
                return redirect('profile')
        else:
            form1 = form.EditForm(instance=request.user)
            return render(request, './editForm.html', {'form': form1})
    else:
        return redirect('signup')
```

</div>