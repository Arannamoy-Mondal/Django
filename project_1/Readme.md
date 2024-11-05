<p>
How to open admin page?
Ans: just run `python manage.py runserver` and hit enter and get an ip address like `127.0.0.1:8000`. Copy and paste the ip address on browser. The screen will show congratulations meeage.
<hr>
How to open contact page?
Ans: 
Step-1: create a new file name `views.py` in inner project folder.
Step-2: create a function named view. 
Step-3: Then open `urls.py`.
Step-4: from . import views
Step-5: path('contact/',views.contact)

`File: views.py`

```py  
def contact(request):
    pass
```

`File: urls.py`

```py
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/',views.contact)
]
```
<hr>
Practice: How to open home page?
Practice: How to open home page default? It means when you enter the link it redirect home page.

</p>