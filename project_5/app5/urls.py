from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:roll>',views.deleteStd,name='delete')
]