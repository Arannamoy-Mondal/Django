<h2 style="text-align:center;font-size:2.5rem;color:white">Part-2 contains:</h2>
<ol style="background: white;">
        <li style="color: black;font-size: 1.5rem;">Render templates globally</li>
        <li style="color: black;font-size: 1.5rem;">Render templates from app</li>
        <li style="color: black;font-size: 1.5rem;">Render templates from inner folder</li>
        <li style="color: black;font-size: 1.5rem;">Context</li>
        <li style="color: black;font-size: 1.5rem;">Django Template Language (DTL)</li>
        <li style="color: black;font-size: 1.5rem;">DTL Filtering</li>
</ol>
<hr>
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