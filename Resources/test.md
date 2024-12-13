<div id="emailSetUp">
    <li><a href="#topic">Topic</a></li>
<h1>Email Sending</h1>
<h3>Please read this part carefully because it is one of the most vulnerable part of backend side. You must secure this.</h3>
<p>Manage Your Google -> Account -> Data&Security ->  Two Factor Authentication -> App Password</p>
<p>Create a .env type file</p>

`Command for env`

```txt
pip install django-environ
```

`.env`

`setting.py`

```py
import environ
BASE_DIR = Path(__file__).resolve().parent.parent
env=environ.Env()
```

```txt
EMAIL=yourMailAddress
EMAIL_PASSWORD=yourAppPassword
```

`setting.py:`

```py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env(EMAIL)      #sender's email-id (your email id)
EMAIL_HOST_PASSWORD = env(EMAIL_PASSWORD)  #password associated with above email-id (app password)
```

</div>


<div id="deploy">
    <li><a href="#topic">Topic</a></li>
<h1>Deploy and hosting a dynamic web</h1>
<h3>You can use <a href="https://render.com/">OnRender</a>, <a href="">Vercel</a> as your wish</h3>
<h3>But we need all dependecies of project. It is better select all dependecies without version. Just compy past this command and get all dependencies. <a href="https://stackoverflow.com/questions/64322829/is-there-any-way-to-get-the-installed-modules-without-version-info-with-pip">For more</a></h3>


`requirements.txt need for both (OnRender and Vercel)`


```txt
pip freeze | python -c "for p in __import__('sys').stdin: print(p.split('=')[0])" > requirements.txt
```

<h3><strong>For OnRender:</strong></h3>
<p>Create an account with github or gitlab or bitbucket. New -> Web Services.</p>

`Select start command:`


```txt
python manage.py runserver 0.0.0.0:80
```


<h3><strong>For Vercel:</strong></h3>
<p>Same as Onrender. Choose git repository</p>

`settings.py`

```py
DEBUG=True

ALLOWED_HOSTS = ["127.0.0.1", ".vercel.app"]

STATIC_ROOT=BASE_DIR/'staticfiles'
WSGI_APPLICATION = 'project.wsgi.app'
```
 
<p>Create a vercel.json file root directory</p>

`vercel.json`

```json
{
    "builds": [{
      "src": "projectName/wsgi.py",
      "use": "@vercel/python",
      "config": { "maxLambdaSize": "15mb", "runtime": "python3.11.3" }
    }],
    "routes": [
      {
        "src": "/(.*)",
        "dest": "projectName/wsgi.py"
      }
    ]
}
```

`wsgi.py`

```py
app=application
```

<p>After completing all previous step run this command</p>

`Command`

```
python manage.py collectstatic
```

<p>After running previous command an  new folder created named staticfiles</p>
</div>



<div id="postgresSQLOnCloud">
    <li><a href="#topic">Topic</a></li>
<h1>PostgreSQL on Superbase:</h1>
<p>Login and Signup same as OnRender. Choose a password for your database or generate a password.
   Go to Left Panel -> Project-settings -> Configuration -> Database -> Connect (From Navigation bar) -> Connection String -> Python ( Select From Type )
   -> Remember NAME, USERNAME, PASSWORD, HOST, PORT 
</p>
<p>Two extenal package needed. These are <a href="https://pypi.org/project/psycopg2-binary/">psycopg2-binary</a> and <a href="https://pypi.org/project/whitenoise/">whitenoise</a></p>

`Command for psycopg2-binary and whitenoise`

```txt
pip install psycopg2-binary
pip install whitenoise
```

`When two package installation done needed some change in settings.py`

`settings.py`
```py
MIDDLEWARE = [
    # ...
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ...
]
```


`settings.py`

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres', # changename from superbase
        'USER': 'masteruser', # changename from superbase
        'PASSWORD': '12345678', # changename from superbase
        'HOST': 'w3-django-project.cdxmgq9zqqlr.us-east-1.rds.amazonaws.com', # changename from superbase
        'PORT': '5432' # changename from superbase
    }
}

```

</div>


<div id="profile">
    <li><a href="#topic">Topic</a></li>
<h1>Gitignore</h1>
<h3>Gitignore is a built in feature of git which ignore that files are mentioned in .gitignore file.</h3>
</div>


