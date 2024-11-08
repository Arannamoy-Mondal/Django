<h1 class="heading"></h1>
<ol class="topic-container" id="topic">
        <li class="topic" style="color: white;font-size: 1.5rem;"><a href="#csrfToken">CSRF Token</a></li>
        <li class="topic" style="color: white;font-size: 1.5rem;"><a href="#getPostMethod">Get Post Method</a></li>
        <li class="topic" style="color: white;font-size: 1.5rem;"><a href="#builtInFromOfDjango">Built in form of django</a></li>
        <li class="topic" style="color: white;font-size: 1.5rem;"><a href="#apiForm">API Form</a></li>
        <li style="font-size: 1.5rem;"><a href="#crispyForm">Crispy Form</a></li>
        <li style="font-size: 1.5rem;"><a href="#djangoFormArgument">Django Form Argument</a></li>
        <li style="font-size: 1.5rem;"><a href="#formValidation">Form Validation</a></li>
        <li style="font-size: 1.5rem;"><a href="#builtInValidators">Buit in form validator of django</a></li>
</ol>

<div id="csrfToken">
    <a href="#topic">Topic</a>
    <h1 class="heading">CSRF Token</h1>
    <h3 class="details">Cross Site Request Forgery. It must be added at begining the any form. Check line 4 of this ss.</h3>
    <img src="./static/CodeSS/csrfToken-1.png" alt="">
</div>

<div id="getPostMethod">
    <a href="#topic">Topic</a>
    <h1>Get Post</h1>
    <h3>Generally, get method does not use because of it's vulnerability. Post method used to visitors data. Check line 3 of 1st html code and check line 2 of 2nd python code.</h3>
    <img src="./static/CodeSS/getPostMethod-1.png" alt="">
    <img src="./static/CodeSS/getPostMethod2.png" alt="">
    <h3>Task: Show visitor contact data on home page.</h3>
    <h3>Solution:</h3>
    <img src="./static/CodeSS/task-1-html.png" alt="">
    <img src="./static/CodeSS/task-1-views-py.png" alt="">
    <h3>Check line no 2-11 of python code.</h3>
</div>

<div id="builtInFromOfDjango">
    <a href="#topic">Topic</a>
    <h1>Built in form of django</h1>
    <h3>2 type of form. API form and Model Form.</h3>
</div>

<div id="apiForm">
    <a href="#topic">Topic</a>
    <h1>API Form</h1>
    <h3>Python code convert in HTML.</h3>
    <img src="./static/CodeSS/builtInForm-1-py.png" alt="">
    <img src="./static/CodeSS/builtInForm-1-views-py.png" alt="">
    <img src="./static/CodeSS/builtInForm-1-html.png" alt="">
    <h3>Task: Show input data in backend and output.html page.</h3>
    <img src="./static/CodeSS/builtInForm-2-views-py.png" alt="">
    <h2>N.B. If you are unable to solve this please recap Django form topic.</h2>
</div>

<div id="crispyForm">
    <a href="#topic">Topic</a>
    <h1>Crispy Form</h1>
    <h3>You can read from <a href="https://django-crispy-forms.readthedocs.io/en/latest/">here.</a></h3>
    
`Installation command ( use venv for installation):`
    
```txt
pip install crispy-bootstrap5
```
`Add this line inside the INSTALLED_APP of setting.py`

```txt
'crispy_forms',
'crispy_bootstrap5'
```
`Add this line next to INSTALLED_APP of setting.py`

```txt 
CRISPY_ALLOWED_TEMPLATE_PACK="bootstrap5"
CRISPY_TEMPLATE_PACK='bootstrap5'
```

`HTML Code:`
    <img src="./static/CodeSS/crispyForm-1-html.png" alt="">
</div>

<div id="djangoFormArgument">
    <a href="#topic">Topic</a>
    <h1>Django Form Argument</h1>
    <h3>Using widget can use html attribute.</h3>

`Syntax of widget:` <br>
`widget=form.dataType(attrs={'attribute_name_of_html':'attribute_value'})` <br>
`Sample code of widget for dateTime:` <br>
`dateTimeField=forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))`

`Understanding:dataType means DateTimeField`
<img src="./static/CodeSS/builtInForm-3-widget.png" alt="">
<h3>For more visit, <a href="https://medium.com/@aman_adastra/day-24-of-100-days-of-django-form-field-arguments-in-django-7175990ca7aa">Medium</a>
    <a href="https://www.geeksforgeeks.org/django-form-build-in-fields-argument/">,GFG</a></h3>
</div>

<div id="formValidation">
    <a href="#topic">Topic</a>
    <h1>Form Validation</h1>

`Check 7-11 and 12-17 line.`
    <img src="./static/CodeSS/formValidation-1.png" alt="">

`Check 1-7 line`
    <img src="./static/CodeSS/formValidation-2.png" alt="">
</div>

<div id="builtInValidators">
    <a href="#topic">Topic</a>
    <h1>Buit in form validator of django</h1>
    <h3>Django has some built in validation features. Previous topic of validation done by manually. But we can do this using buit in validator.</h3>
    <h3>We need to import this package.</h3>

`from django.core import validators`
<br>

`Syntax: variableName=forms.charField(validators=[validators.x(condition,message=""),y]), here if variable type is text use charField, if integer use IntegerField,x is contidion type, y is another condition`
<br>

`Some condition sample:`
<br>

`validators.MaxLengthValidator(6,message="At most 6 character"),validators.MinLengthValidator(3,message="At least 3 character")`
<br>

`validators=[validators.MaxValueValidator(52,message="For CEO position your age must be between 20 to 52. "),validators.MinValueValidator(20,message="For CEO position your age must be between 20 to 52. ")`
<br>

`validators.EmailValidator(message="Enter a valid mail")`
<img src="./static/CodeSS/builtInValidators.png" alt="">
</div>