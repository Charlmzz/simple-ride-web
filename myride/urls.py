
from .views import SignUpView

from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView # n ew

from django.http import HttpResponse

from myride import views

urlpatterns = [
    path('registration/',views.registration, name='register'),
    path('signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('login/',views.login,name='login'),
    path('save/',views.storeInfo,name='storeInfo'),
    path('depart_list/',views.depart_list,name='departList'),
    path('riderequest/',views.riderequest,name='ridereq'),
    path('settings/',views.dashboard,name='dashboard'),
    path('settings/edit-vehicle/',views.vehicle_edit,name='vehicleEdit'),
    path('settings/edit-user/',views.user_edit,name='userEdit'),
]
