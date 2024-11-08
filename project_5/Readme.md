<div id="topic">
    <h1>Topic:</h1>
    <li><a href="#orm">ORM</a></li>
    <li><a href="#migration">Migration</a></li>
    <li><a href="#dbBrowser">Show Model Data Using VS code and DB browser</a></li>
    <li><a href="#superUser">Super User</a></li>
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

class Person(models.Model): # inherit from models.Model
    name=models.CharField(max_length=15)
    age=models.IntegerField()


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