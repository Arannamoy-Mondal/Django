<div id="topic">
    <h1>Topic:</h1>
    <li><a href="#orm">ORM</a></li>
    <li><a href="#migration">Migration</a></li>
    <li><a href="#dbBrowser">Show Model Data Using VS code and DB browser</a></li>
    <li><a href="#superUser">Super User</a></li>
    <li><a href="#modelCreate">Show model backend to frontend</a></li>
</div>

<div id="orm">
    <h1>ORM</h1>
    <h3>ORM means Object Relational Mapper. ORM interacts with SQLite, MySQL, PostgreSQL, OracleDB.
        ORM converts python class to SQL. So, developer does not need to write SQL code. Django provides db.sqlite3 automatically.
        Here, django automatically create a primary key. 
    </h3>
    
`Sample code:`

```py

from django.db import models

# Create your models here.

class student(models.Model):
      name=models.CharField(max_length=20)
      roll=models.IntegerField(primary_key=True)
      address=models.TextField()
      age=models.IntegerField(default=0)
      def __str__(self):
        return f"Name: {self.name}, Roll: {self.roll}, Age: {self.age}, Address: {self.address}"

```
</div>

<div id="migration">
    <a href="#topic">Topic</a>
    <h1>Migration</h1>
    <h3>Migration is the process of converting python class to database.Command 1 convert python to sql and Command 2 convert in database.</h3>

`Command-1:` `python manage.py makemigrations`
<br>

`Command-2:` `python manage.py migrate`

</div>

<div id="dbBrowser">
    <a href="#topic">Topic</a>
    <h1>Show Model Data Using VS code and DB browser</h1>
    <h3>SQLite, SQLiteViewer  from vscode extension. DBbrowser from chrome.</h3>
    <h3>DBBrower:
        Open Database from your source.
    </h3>
</div>

<div id="superUser">
    <a href="#topic">Topic</a>
    <h1>Super User:</h1>
    <h3>Super user is necessary to log in admin panel. Create super user using this command. </h3>
    
`Command:` `python manage.py createsuperuser`
</div>

<div id="modelCreate">
    <a href="#topic">Topic</a>
    <h1>Show model backend to frontend</h1>
    <h3>Add data table backend to frontend</h3>

`views.py`

```py
from django.shortcuts import render,redirect
from . import models
# Create your views here.

def home(request):
    student1 = models.student.objects.all()
    print(student1)
    return render(request,'home.html',{'data':student1})

def deleteStd(request,roll):
    student1=models.student.objects.get(pk=roll).delete()
    return redirect('home')

```

`urls.py`

```py
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:roll>',views.deleteStd,name='delete')
]
```
`home.html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title></title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous"
    />
  </head>
  <body>
    Okay
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Roll</th>
          <th scope="col">Name</th>
          <th scope="col">Age</th>
          <th scope="col">Address</th>
          <th scope="col">Action</th>
        </tr>
      </thead>
      <tbody>
        {% if data %} 
        {% for id in data %}
         <tr>
            <td>{{id.roll}}</td>
            <td>{{id.name}}</td>
            <td>{{id.age}}</td>
            <td>{{id.address}}</td>
            <td><button class="btn btn-danger"><a href="{% url 'delete' id.roll %}" class="text-light">Delete</a></button></td>
          </tr>
      
         {% endfor %} 
         {% else %}
        <h3>No data avialable</h3>
        {% endif %}
      </tbody>
    </table>
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```


</div>