from django.contrib import admin

from vpa.models.user import User
from vpa.models.vehicle import Vehicle


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    pass
