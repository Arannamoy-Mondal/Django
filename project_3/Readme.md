<h1 style="text-align:center;font-size:2.5rem;color:white" class="heading">Part-3 contains:</h1>
<ol>
        <li style="color: white;font-size: 1.5rem;">Static files</li>
        <li style="color: white;font-size: 1.5rem;">CSS framework adding</li>
        <li style="color: white;font-size: 1.5rem;">URL Tag</li>
        <li style="color: white;font-size: 1.5rem;">Template Inheritance</li>
</ol>
<hr>
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

<h1 class="heading">URL Tag:</h1>
<h3 class="details"></h3>
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

<!-- Template for readme -->
<!-- 
<h1 class="heading"></h1>
<ol class="topic-container">
        <li class="topic" style="color: white;font-size: 1.5rem;">Topic Name</li>
        <li class="topic" style="color: white;font-size: 1.5rem;">Topic Name</li>
        <li class="topic" style="color: white;font-size: 1.5rem;">Topic Name</li>
        <li class="topic" style="color: white;font-size: 1.5rem;">Topic Name</li>
</ol>
<h1 class="heading"></h1>
<h3 class="details"></h3>
<h1 class="heading"></h1>
<h3 class="details"></h3>
 -->