from django.urls import path,include
from . import views
urlpatterns = [
    path('courses/',views.courses),
    path('',views.app_1)
]
