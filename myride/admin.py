from django.contrib import admin

# Register your models here.
from .models import User, Ride, Vehicle, Sharer

admin.site.register(User)
admin.site.register(Ride)
admin.site.register(Vehicle)
admin.site.register(Sharer)

