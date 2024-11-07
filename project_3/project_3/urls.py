from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('app/',include('app3.urls'),name='app'),
    path('about/<int:id>/',views.aboutPage,name='about'),
    path('contact/',views.contact,name='contact')
]
