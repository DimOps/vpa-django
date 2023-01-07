from django.utils.timezone import now


from django.db import models

from vpa.models import Vehicle


class MaintenanceRecord(models.Model):

    MAINTENANCE_MAIN = 'Maintenance'
    MAINTENANCE_REPAIR = 'Repair'
    MAINTENANCE_ENHANCEMENT = 'Enhancement'

    MAINTENANCE_REASONS = (
        (MAINTENANCE_MAIN, 'Maintenance'),
        (MAINTENANCE_REPAIR, 'Repair'),
        (MAINTENANCE_ENHANCEMENT, 'Enhancement'),
    )

    _id = models.AutoField(primary_key=True)
    reason = models.TextField(max_length=11, choices=MAINTENANCE_REASONS, blank=True)
    title = models.CharField(max_length=50, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)


class MaintenanceRecordDetails(models.Model):
    _id = models.AutoField(primary_key=True)
    part_name = models.CharField(max_length=30, blank=True)
    brand = models.CharField(max_length=30, null=True, blank=True)
    volume = models.IntegerField(default=1, blank=True)
    date_performed = models.DateField(default=now, blank=True)
    per_item = models.BooleanField(default=False, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True)
    comment = models.CharField(max_length=30, null=True, blank=True)
    next_due = models.DateField(null=True, blank=True)
    maintenance_record = models.ForeignKey(MaintenanceRecord, on_delete=models.CASCADE)


class VehicleCare(models.Model):
    _id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=True)
    scheduled_for = models.DateTimeField(blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)


class VehicleCareDetails(models.Model):
    _id = models.AutoField(primary_key=True)
    duration = models.CharField(max_length=30, blank=True)
    place = models.CharField(max_length=30, blank=True)
    cost = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True)
    comment = models.TextField(max_length=200, null=True, blank=True)
    vehicle_care = models.ForeignKey(VehicleCare, on_delete=models.CASCADE)


class ToFix(models.Model):
    SECTION_CHOICE_CHASSIS = 'Chassis'
    SECTION_CHOICE_EXTERIOR = 'Exterior'
    SECTION_CHOICE_INTERIOR = 'Interior'
    SECTION_CHOICE_TUNING = 'Tuning'

    SECTIONS_CHOICES = (
        (SECTION_CHOICE_CHASSIS, 'Chassis'),
        (SECTION_CHOICE_EXTERIOR, 'Exterior'),
        (SECTION_CHOICE_INTERIOR, 'Interior'),
        (SECTION_CHOICE_TUNING, 'Tuning'),
    )

    _id = models.AutoField(primary_key=True)
    area_to_fix = models.CharField(max_length=8,
                                   choices=SECTIONS_CHOICES,
                                   default='',
                                   blank=True)
    title = models.CharField(max_length=50, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)


class ToFixDetails(models.Model):
    _id = models.AutoField(primary_key=True)
    place = models.CharField(max_length=30, blank=True)
    estimated_cost = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True)
    comment = models.TextField(max_length=200, null=True, blank=True)
    to_fix = models.ForeignKey(ToFix, on_delete=models.CASCADE)


class Notes(models.Model):
    _id = models.AutoField(primary_key=True)
    note = models.TextField(max_length=300, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

