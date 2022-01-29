
from .views import SignUpView

from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView # n ew

from django.http import HttpResponse

from myride import views

urlpatterns = [
    path('registration/',views.registration, name='register'),
    path('signup/', views.signup, name='signup'),
    #path('signup/', SignUpView.as_view(template_name='registration/signup.html'), name='signup'),
    path('', views.home, name='home'),
    path('login/',views.login,name='login'),
    path('save/',views.storeInfo,name='storeInfo'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('riderequest/',views.riderequest,name='ridereq'),
]
