# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
from myride.models import *
from django import forms


def home(request):
    return render(request,'home.html')

#-----------------------------driver registration
#model form for registration
class regForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ["type","plate_num","max_passenger","special_info"]
        widgets = {
            "type": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter car type"}),
            "plate_num": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter plate number"}),
            "max_passenger": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter maximum passengers"}),
            "special_info": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter any special info you would let others know"})
        }

def registration(request):
    if request.method=="GET":
        form = regForm()
        return render(request,'registration.html',{"form":form})
    #POST
    form = regForm(data=request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        lastVehicle = Vehicle.objects.last()
        if not lastVehicle:
            obj.vehicle_id = 1
        else:
            obj.vehicle_id = lastVehicle.vehicle_id+1
        obj.save()
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!save foreign key in user
        return render(request,'driverRegSuccess.html')
    else:
        return render(request,'registration.html',{"form":form})
#-------------------------------------driver reg end

def storeInfo(request):

    return HttpResponse()

#-----------------------------Sign up
#model form for sign up
class signupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name","user_name","password"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter name"}),
            "user_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter user name"}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter password"})
        }
    def clean(self):
        if self.is_valid():
            cleaned_data = self.cleaned_data
            username = self.cleaned_data['user_name']
            checkUser = User.objects.filter(user_name=username)
            if checkUser:
                raise forms.ValidationError('Username already exists.')
            return cleaned_data

def signup(request):
    if request.method=="GET":
        form = signupForm()
        return render(request,'signup.html',{"form":form})
    #POST
    form = signupForm(data=request.POST)
    if form.is_valid():
        form.clean()
        obj = form.save(commit=False)
        lastUser = User.objects.last()
        if not lastUser:
            obj.user_id = 1
        else:
            obj.user_id = lastUser.user_id+1
        obj.save()
        return render(request,'regSuccess.html')
    else:
        return render(request,'signup.html',{"form":form})
#----------------------------------sign up ends

def login(request):
    if request.method=="GET":
        return render(request, "login.html")
    username = request.POST.get("user")
    password = request.POST.get("pwd")
    if username == "vcm" and password == "charlene":
        return HttpResponse("Log in Success") #render dashboard
    else:
        return render(request,'login.html', {"err_msg":"Incorrect username or password"})

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    #return HttpResponse()

def dashboard(request):
    return render(request,"dashboard.html")

#-----------------------------------need owner id!!!!!!, time stamp need bootstrap
#model form for registration
class rideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ["destination","arrival_timestamp","num_passengers","vehicle_type","special_req"]
        widgets = {
            "destination": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your destination"}),
            "arrival_timestamp": forms.DateTimeInput(attrs={"class": "form-control", "placeholder": "Enter an arrival time. Format: YYYY-MM-DD HH:MM:SS or MM/DD/YY HH:MM"}),
            "num_passengers": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter number of passengers"}),
            "vehicle_type": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter a vehicle type that you wish"}),
            "special_req": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter any special info you would let others know"})
        }

def riderequest(request):
    if request.method=="GET":
        form = rideForm()
        return render(request,'rideRequest.html',{"form":form})
    #POST
    form = rideForm(data=request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        lastRide = Ride.objects.last()
        if not lastRide:
            obj.ride_id = 1
        else:
            obj.ride_id = lastRide.ride_id+1
        #!!!!!!!!!!!!also need owner id
        obj.save()
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!save foreign key in user and more
        return render(request,'rideRequestSuccess.html')
    else:
        return render(request,'rideRequest.html',{"form":form})



