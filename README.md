# Django

# Introduction:
```
4 type of request. Generally. called CRUD operation. (Create, Read, Update, Database)
1. Get (For get anything. Read operation)
2. Post (For create. Create operation)
3. Update (For edit anything. Update operation)
4. Delete (For delete anything. Delete operation)
```

# Create virtual environment for python in ubuntu:

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
ls my_env
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

# Django Template Language ( DTL ):