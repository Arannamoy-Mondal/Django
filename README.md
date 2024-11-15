# Django Topic:
<ol id="topic">
<li><a href="#introduction">Introduction</a></li>
<li><a href="#venv">Set up environment for django</a></li>
<li><a href="#staticFiles">Static files</a></li>
<li><a href="#cssFrameWorkAdding">CSS framework adding</a></li>
<li><a href="#urlTag">URL Tag</a></li>
<li><a href="#inhetiance">Template Inheritance</a></li>
<li><a href="#csrfToken">CSRF Token</a></li>
<li><a href="#getPostMethod">Get Post Method</a></li>
<li><a href="#builtInFromOfDjango">Built in form of django</a></li>
<li><a href="#apiForm">API Form</a></li>
<li><a href="#crispyForm">Crispy Form</a></li>
<li><a href="#djangoFormArgument">Django Form Argument</a></li>
<li><a href="#formValidation">Form Validation</a></li>
<li><a href="#builtInValidators">Buit in form validator of django</a></li>
<li><a href="#signUp">SignUp</a></li>
<li><a href="#logIn">Login</a></li>
<li><a href="#profile">Profile</a></li>
<li><a href="#logOut">LogOut</a></li>
<li><a href="#PasswordChangeWithoutOldPassword">Password Change Without Old Password</a></li>
<li><a href="#PasswordChangeWithOldPassword">Password Change With Old Password</a></li>
<li><a href="#editProfile">Edit Profile</a></li>
</ol>

<div id="introduction">
    <li><a href="#topic">Topic</a></li>

```txt
4 type of request. Generally. called CRUD operation. (Create, Read, Update, Database)
1. Get (For get anything. Read operation)
2. Post (For create. Create operation)
3. Update (For edit anything. Update operation)
4. Delete (For delete anything. Delete operation)    
```

</div>

<div id="venv">
    <li><a href="#topic">Topic</a></li>

# Create virtual environment for python in ubuntu . For windows search on google.

```txt
sudo apt install -y python3-venv
```
```
cd environments
```
```
python3 -m venv my_env
```
```
ls my_env;
```
```
source my_env/bin/activate
```
```
Issue for ubuntu while installing PyAutoGUI package (N.B. check pyautogui after every command):
```
```txt
echo Display
```
```txt
xhost +SI:localuser:$(whoami)
```
```txt
xhost +local:$(whoami)
```
```txt
sudo apt-get install xvfb
```
```txt
xvfb-run python /home/workstation/Desktop/Test/Project/TestPython/test.py
```
```txt
pip uninstall pyautogui mouseinfo
```
```txt
pip install pyautogui
```

# Django install:
`For install`
```txt
pip install django
```

`For see current version:`
```txt
django-admin --version
```
`For specific version:`
```txt
pip install django==version
```
`For all package list in pip`
```txt
pip list
```

`
For confirm django framework file created successfully run this command and copy paste the ip address in browser
`

```txt
python project1/manage.py runserver
```

`For create project`
```txt
django-admin startproject projectName
```

`For create application`
```txt
django-admin startapp appName
```

`About project folder`
```txt
The most outer folder is called root folder and it has a same name folder which is called inner folder.
Generally outer folder has 5 types of file. These are 
__init__.py ==> considered as python package,
asgi.py ==> asgi.py exists in inner project folder. asynchronus and synchronus,
setting.py ==>settings.py exists in inner project folder. Database Config Information, Template, Installed Application, Validators, mother of django
urls.py ==> contains url with application,
wsgi.py ==> (Web Server Gateway Interface) how a web server communicates with web application, synchronus system
manage.py ==> manage.py exists in root folder. for project specific command line utility. 
```
`About app folder`
```txt
app folder has no built in urls.py.
admin.py ==> for admin
apps.py
models.py ==> for database
test.py ==> for testing
views.py ==> for logical work
```

`For admin login run manage.py as runserver and get an ip address and add /admin  with this url and press enter`

</div>
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

<div id="csrfToken">
    <a href="#topic">Topic</a>
    <h1 class="heading">CSRF Token</h1>
    <h3 class="details">Cross Site Request Forgery. It must be added at begining the any form. Check line 4 of this ss.</h3>
    <img src="./static/CodeSS/csrfToken-1.png" alt="">
</div>

<div id="getPostMethod">
    <a href="#topic">Topic</a>
    <h1>Get Post</h1>
    <h3>Generally, get method does not use because of it's vulnerability. Post method used to visitors data. Check line 3 of 1st html code and check line 2 of 2nd python code.</h3>
    <img src="./static/CodeSS/getPostMethod-1.png" alt="">
    <img src="./static/CodeSS/getPostMethod2.png" alt="">
    <h3>Task: Show visitor contact data on home page.</h3>
    <h3>Solution:</h3>
    <img src="./static/CodeSS/task-1-html.png" alt="">
    <img src="./static/CodeSS/task-1-views-py.png" alt="">
    <h3>Check line no 2-11 of python code.</h3>
</div>

<div id="builtInFromOfDjango">
    <a href="#topic">Topic</a>
    <h1>Built in form of django</h1>
    <h3>2 type of form. API form and Model Form.</h3>
</div>

<div id="apiForm">
    <a href="#topic">Topic</a>
    <h1>API Form</h1>
    <h3>Python code convert in HTML.</h3>
    <img src="./static/CodeSS/builtInForm-1-py.png" alt="">
    <img src="./static/CodeSS/builtInForm-1-views-py.png" alt="">
    <img src="./static/CodeSS/builtInForm-1-html.png" alt="">
    <h3>Task: Show input data in backend and output.html page.</h3>
    <img src="./static/CodeSS/builtInForm-2-views-py.png" alt="">
    <h2>N.B. If you are unable to solve this please recap Django form topic.</h2>
</div>

<div id="crispyForm">
    <a href="#topic">Topic</a>
    <h1>Crispy Form</h1>
    <h3>You can read from <a href="https://django-crispy-forms.readthedocs.io/en/latest/">here.</a></h3>
    
`Installation command ( use venv for installation):`
    
```txt
pip install crispy-bootstrap5
```
`Add this line inside the INSTALLED_APP of setting.py`

```txt
'crispy_forms',
'crispy_bootstrap5'
```
`Add this line next to INSTALLED_APP of setting.py`

```txt 
CRISPY_ALLOWED_TEMPLATE_PACK="bootstrap5"
CRISPY_TEMPLATE_PACK='bootstrap5'
```

`HTML Code:`
    <img src="./static/CodeSS/crispyForm-1-html.png" alt="">
</div>

<div id="djangoFormArgument">
    <a href="#topic">Topic</a>
    <h1>Django Form Argument</h1>
    <h3>Using widget can use html attribute.</h3>

`Syntax of widget:` <br>
`widget=form.dataType(attrs={'attribute_name_of_html':'attribute_value'})` <br>
`Sample code of widget for dateTime:` <br>
`dateTimeField=forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))`

`Understanding:dataType means DateTimeField`
<img src="./static/CodeSS/builtInForm-3-widget.png" alt="">
<h3>For more visit, <a href="https://medium.com/@aman_adastra/day-24-of-100-days-of-django-form-field-arguments-in-django-7175990ca7aa">Medium</a>
    <a href="https://www.geeksforgeeks.org/django-form-build-in-fields-argument/">,GFG</a></h3>
</div>

<div id="formValidation">
    <a href="#topic">Topic</a>
    <h1>Form Validation</h1>

`Check 7-11 and 12-17 line.`
    <img src="./static/CodeSS/formValidation-1.png" alt="">

`Check 1-7 line`
    <img src="./static/CodeSS/formValidation-2.png" alt="">
</div>

<div id="builtInValidators">
    <a href="#topic">Topic</a>
    <h1>Buit in form validator of django</h1>
    <h3>Django has some built in validation features. Previous topic of validation done by manually. But we can do this using buit in validator.</h3>
    <h3>We need to import this package.</h3>

`from django.core import validators`
<br>

`Syntax: variableName=forms.charField(validators=[validators.x(condition,message=""),y]), here if variable type is text use charField, if integer use IntegerField,x is contidion type, y is another condition`
<br>

`Some condition sample:`
<br>

`validators.MaxLengthValidator(6,message="At most 6 character"),validators.MinLengthValidator(3,message="At least 3 character")`
<br>

`validators=[validators.MaxValueValidator(52,message="For CEO position your age must be between 20 to 52. "),validators.MinValueValidator(20,message="For CEO position your age must be between 20 to 52. ")`
<br>

`validators.EmailValidator(message="Enter a valid mail")`
<img src="./static/CodeSS/builtInValidators.png" alt="">
</div>

<div id="staticFiles">
<a href="#topic">Topic</a>
<h1 class="heading">Static files:</h1>
<h3 class="details">Static files can be added in globally or app folder. Must change in settings.py file.</h3>

`Changes code`

```py

STATIC_URL = 'static/'
STATICFILES_DIRS=[BASE_DIR/'static'] 

```
```html
<img src="{% static 'filename.jpeg' %}">
```
</div>
<div id="cssFrameWorkAdding">
<a href="#topic">Topic</a>
<h1 class="heading">CSS framework adding:</h1>
<h3 class="details">Same as static files. Just add CDN link on base.html</h3>

`Changes code`

```py

STATIC_URL = 'static/'
STATICFILES_DIRS=[BASE_DIR/'static'] 

```

```html
<link rel="stylesheet" href="{% static 'stysheet.css' %}">
```
</div>

#

<div id="urlTag">
<a href="#topic">Topic</a>
<h1>URL Tag:</h1>
<h3></h3>

`URL Tagging:`

`Syntax of urls.py:`

<img src="../urlTagging.png">

<h3>In this, ss line no 6,7,8,9 has an extra parameter (name="someThing") must be given and name parameter must be same as double quote name.<code><pre>href="{% url "someThing"  %}"</pre></code></h3>

```html

<a class="nav-link active" aria-current="page" href="{% url 'contact' %}">Contact</a>

```

`urls.py:`

```py

from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('app/',include('app3.urls'),name='app'),
    path('about/',views.aboutPage,name='about'),
    path('contact/',views.contact,name='contact')
]

```

`views.py:`

```py

def aboutPage(request):
    return render(request,'index.html')

```

</div>

#

<div id="passValueInURL">
<a href="#topic">Topic</a>
<h1>Pass Value In URl:</h1>
<h3>Sample: `http://127.0.0.1:8000/about/1/` </h3> 

`urls.py:`

```py

path('about/<int:id>/',views.aboutPage,name='about'),

```   

<hr>

`views.py`

```py

def aboutPage(request,id):
    return render(request,'index.html',{'id':id})

```

`base.html`

```
<a class="nav-link" href="{% url 'about' id=1 %}">About</a>

```

</div>

#

<div id="inhetiance">
<a href="#topic">Topic</a>
<h1 class="heading">Template Inheritance:</h1>
<h3 class="details">Two type of templates. 1. Parent templates (base.html), 2. Child templates.</h3>

`Sample code of base.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    {% block content %}
       Here, child template content will be written
    {% endblock %}
</body>
</html>
```

`Sample code of child templplate`

```html
{% extends 'base.html' %}
{% block content %}

<h1> Hello Django </h1>

{% endblock %}
```
</div>