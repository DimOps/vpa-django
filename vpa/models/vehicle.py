from django.db import models

from vpa.models import User


class Vehicle(models.Model):
    VEHICLE_CHOICE_CAR = 'Car'
    VEHICLE_CHOICE_VAN = 'Van'
    VEHICLE_CHOICE_BIKE = 'Bike'
    VEHICLE_CHOICE_TRUCK = 'Truck'

    VEHICLES_CHOICES = (
        (VEHICLE_CHOICE_CAR, 'Car'),
        (VEHICLE_CHOICE_VAN, 'Van'),
        (VEHICLE_CHOICE_BIKE, 'Bike'),
        (VEHICLE_CHOICE_TRUCK, 'Truck'),
    )

    _id = models.AutoField(primary_key=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    type = models.CharField(max_length=5, choices=VEHICLES_CHOICES,
                            default=VEHICLE_CHOICE_CAR,
                            blank=True)
    brand = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=50,  blank=True)
    model_spec = models.CharField(max_length=50, null=True, blank=True)
    owner = models.ForeignKey(User, related_name='VEHICLES', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        repr_string = f'{self.type} {self.model} {self.model_spec} {self.owner}'
        return repr_string

class VehicleDetails(models.Model):

    TRANSMISSION_CHOICE_MANUAL = 'Manual'
    TRANSMISSION_CHOICE_SEMI = 'Semi-Automatic'
    TRANSMISSION_CHOICE_AUTO = 'Automatic'

    TRANSMISSION_CHOICES = (
        (TRANSMISSION_CHOICE_MANUAL, 'Manual'),
        (TRANSMISSION_CHOICE_SEMI, 'Semi-Automatic'),
        (TRANSMISSION_CHOICE_AUTO, 'Automatic'),
    )

    DRIVE_CHOICE_FRONT = 'Front-Wheel-Drive'
    DRIVE_CHOICE_REAR = 'Rear-Wheel-Drive'
    DRIVE_CHOICE_ALL = 'All-Wheel-Drive'

    DRIVE_CHOICES = (
        (DRIVE_CHOICE_FRONT, 'Front-Wheel-Drive'),
        (DRIVE_CHOICE_REAR, 'Rear-Wheel-Drive'),
        (DRIVE_CHOICE_ALL, 'All-Wheel-Drive'),
    )

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

    horsepower = models.IntegerField(null=True, blank=True)
    transmission = models.CharField(max_length=14,
                                    choices=TRANSMISSION_CHOICES,
                                    default=TRANSMISSION_CHOICE_AUTO,
                                    blank=True)
    drive = models.CharField(max_length=17,
                             choices=DRIVE_CHOICES,
                             default=DRIVE_CHOICE_FRONT,
                             blank=True)
    engine = models.CharField(max_length=50, null=True, blank=True)
    engine_type = models.CharField(max_length=50, null=True, blank=True)
    engine_spec = models.CharField(max_length=50, null=True, blank=True)
    add_ons = models.CharField(max_length=8,
                               choices=SECTIONS_CHOICES,
                               default='',
                               blank=True)
    chassis = models.BooleanField(default=False, blank=True)
    exterior = models.BooleanField(default=False, blank=True)
    interior = models.BooleanField(default=False, blank=True)
    tuning = models.BooleanField(default=False, blank=True)
    car = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


class Chassis(models.Model):
    feature = models.CharField(max_length=30, blank=True)
    feature_value = models.CharField(max_length=20, null=True, blank=True)
    car = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


class Exterior(models.Model):
    feature = models.CharField(max_length=30, blank=True)
    feature_value = models.CharField(max_length=20, null=True, blank=True)
    car = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


class Interior(models.Model):
    feature = models.CharField(max_length=30, blank=True)
    feature_value = models.CharField(max_length=20, null=True, blank=True)
    car = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


class Tuning(models.Model):
    feature = models.CharField(max_length=30, blank=True)
    feature_value = models.CharField(max_length=20, null=True, blank=True)
    car = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
