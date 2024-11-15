# Built in Login and Signup form of django
```py
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
```

```html
{% extends 'base.html' %}
{% load crispy_forms_tags %}
{% block title %}Sign Up{% endblock %}
{% block content %}
<h1 style="text-align: center;">Home</h1>
<form action="" method="post">
    <!-- {{form|crispy}} -->
     {% csrf_token %}
     {% for fm in form %}
      {{fm.label_tag}}
      {{fm}}
      {{ fm.errors|striptags }}
     {% endfor %}
     <button class="btn btn-warning">Submit</button>
</form>
{% endblock %}
```

`More about widget and attrs`

```py
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
class RegisterForm(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'id':'required'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
```

