from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('signUp/',views.signUp,name='signUp'),
    path('login/',views.logIn,name='logIn'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logOut,name='logOut'),
    path('changePassword/',views.passChange,name='changePassword'),
    path('changePasswordWithoutOldPassword/',views.passChangeWithOutOldPassWord,name='changePasswordWithoutOldPassword'),
    path('editData/',views.editUserData,name='editData')
]