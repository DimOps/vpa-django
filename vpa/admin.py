from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from vpa.models.vehicle import Vehicle, VehicleDetails


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    pass


@admin.register(VehicleDetails)
class VehicleDetailsAdmin(admin.ModelAdmin):
    pass
