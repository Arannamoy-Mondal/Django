<h2 style="text-align:center;font-size:2.5rem;color:white">Part-2 contains:</h2>
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

<h1>(3+). Context and DTL: </h1>
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
           <h3>Your get driving license </h3>
    {% else %}
           <h3>You do not get driving license</h3>
    {% endif %}

    <!-- This conditional statement are case sensitive. So, it must be written in python sytle -->
```