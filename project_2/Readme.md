<h1 style="text-align:center;font-size:2.5rem;color:white">Part-2 contains:</h1>
<ol style="background: white;">
        <li style="color: black;font-size: 1.5rem;">Render templates globally</li>
        <li style="color: black;font-size: 1.5rem;">Render templates from app</li>
        <li style="color: black;font-size: 1.5rem;">Context</li>
        <li style="color: black;font-size: 1.5rem;">Django Template Language (DTL)</li>
        <li style="color: black;font-size: 1.5rem;">DTL Filtering</li>
</ol>
<hr>
<h1>(1+2). Render templates from globally and from app:</h1>
<h3>You can render globally or in django app.</h3>
<h2>For globally:</h2>
<h3> At first need to create a folder named templates in root folder.Then, create html file as usual. Then, need to edit inner folder settings.py. Add global folder name in `DIRS`. If the global folder name is templates then, need to change it "DIRS"=["templates"] </h3>
<h3>Just change in views function:</h3>

```py
'DIRS': ['templates'],
```

```py
from django.shortcuts import render
def index(request):
    return render(request,'file.html')
```

<h2>For app:</h2>
<h3>At first need to create a folder named templates in app folder. Then create a folder in this templates folder. Then, create html file as usual. Now, it ready for render.</h3>

```py
from django.shortcuts import render
def index(request):
    return render(request,'file.html')
```

<h1>(3+4). Context and DTL: </h1>
<h2>Context means backend to frontend</h2>
<h3>For context, take a dictionary input in views.py. Then return it. For print value use {{value}} and others {% for loop %}</h3>
<h3>Sample code:</h3>

```py
from django.shortcuts import render

def index(request):
    data={
        "name":"Hello World","age":20,"address":"Annapolis, Maryland","fullName":['Macbook air m1']
    }
    return render(request,'index.html',data)
```

```html
<!-- value -->
<h2>{{name}}</h2>
<h3>{{fullName}}</h3>
<h3>{{address}}</h3>

<!-- conditional statement -->

{% if age >= 20 %}
<h3>Your get driving license</h3>
{% else %}
<h3>You do not get driving license</h3>
{% endif %}

<!-- This conditional statement are case sensitive. So, it must be written in python sytle -->
```

<h1>DTL Filtering:</h1>
<h2>join filtering:</h2> 
<h3>it concates a list of string. Example: a=["Hello","Hi","Bye"]. After using join filter it returns "Hello Hi Bye" in frontend html.</h3>
```html
   {{list}}
    <!-- Join function it concates a list of string. This is a case sensitive function  -->
    <h3>{{list|join:" "}}</h3> 
```
<h2>Date time filter:</h2>

`Python Code:`

```py
import datetime
"time":datetime.datetime.now()
```

`HTML Code:`

```HTML
<h3>{{time| date:"D d M Y"}}</h3>
```

<h2>Empty string filter:</h2>

`Python Code:`

```py
"empty":""
```

`HTML Code:`

```HTML
<h3>{{empty|default:"an empty string"}}</h3>
```

<h2>cut filter:</h2>
<h3>cut filter remove the space or specific character from the string. Syntax: {{value|cut:"specificCharacter"}}</h3>
```HTML
<h3>{{"Pythona isa funa."|cut:"a" }}</h3>
```
<h2>Length filter:</h2>
<h3>It returns string length.</h3>

```html 
<h3>{{"value"|length}}</h3>
```

<h2>Timesince filter:</h2>
<h3>It works like post time of youtube, facebook</h3>
```html
```

<h2>Truncate characters filter:</h2>
<h3><h3>

```py
from django.shortcuts import render
import datetime
def index(request):
    data={
        "name":"Hello World","age":20,"address":"Annapolis, Maryland","fullName":['Macbook air m1'],
        "list":["Hello","Hi","Bye"],"time":datetime.datetime.now(),"empty":"","truncate":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsa corporis quae, fugiat, ex inventore tenetur"
        +"delectus culpa placeat quibusdam incidunt rerum. Natus facilis ipsam velit aspernatur, temporibus error"
        +"provident ipsum!"
    }
    return render(request,'index.html',data)
```
```html
<h3>{{truncate|truncatechars:4}}</h3>
```

<h2>Truncate word filter:</h2>

```py
from django.shortcuts import render
import datetime
def index(request):
    data={
        "name":"Hello World","age":20,"address":"Annapolis, Maryland","fullName":['Macbook air m1'],
        "list":["Hello","Hi","Bye"],"time":datetime.datetime.now(),"empty":"","truncate":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsa corporis quae, fugiat, ex inventore tenetur"
        +"delectus culpa placeat quibusdam incidunt rerum. Natus facilis ipsam velit aspernatur, temporibus error"
        +"provident ipsum!"
    }
    return render(request,'index.html',data)
```
```html
<h3>{{truncate|truncatewords:4}}</h3>
```
<h3>For explore more <a href="https://earthly.dev/blog/django-template-filters/">https://earthly.dev/</a>, <a href="https://www.geeksforgeeks.org/django-template-filters/">GFG</a>, 
<a href="https://www.w3schools.com/django/">W3School</a>
