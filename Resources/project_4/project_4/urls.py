from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("app4.urls")),
    path('home/',views.home,name='home'),
    path('about/',views.aboutPage,name='about'),
    path('contact/',views.contactPage,name='contact'),
    path('signUpForms/',views.signUpForms,name='signUpForms'),
    path('formOfDjango/',views.formOfDjango,name='formOfDjango'),
    path('output',views.passwordVerification,name='output'),
    path('Buit_in_validator_of_django_form/',views.Buit_in_validator_of_django_form,name='builtInValidator'),
    path('login/',views.logInForm,name='login')
]
