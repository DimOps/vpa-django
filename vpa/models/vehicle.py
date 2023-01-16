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
    owner = models.ForeignKey(User, related_name='owner_vehicles', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        repr_string = f'{self.type} {self.brand} {self.model} {self.owner}'
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

    _id = models.AutoField(primary_key=True, blank=True)
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
    vehicle = models.ForeignKey(Vehicle, related_name='vehicle_details', default=1, on_delete=models.CASCADE)


class Chassis(models.Model):
    _id = models.AutoField(primary_key=True, blank=True)
    feature = models.CharField(max_length=30, blank=True)
    feature_value = models.CharField(max_length=20, null=True, blank=True)
    details = models.ForeignKey(Vehicle, related_name='chassis_details', default=1, on_delete=models.CASCADE)


class Exterior(models.Model):
    _id = models.AutoField(primary_key=True, blank=True)
    feature = models.CharField(max_length=30, blank=True)
    feature_value = models.CharField(max_length=20, null=True, blank=True)
    details = models.ForeignKey(Vehicle, related_name='exterior_details', default=1, on_delete=models.CASCADE)


class Interior(models.Model):
    _id = models.AutoField(primary_key=True, blank=True)
    feature = models.CharField(max_length=30, blank=True)
    feature_value = models.CharField(max_length=20, null=True, blank=True)
    details = models.ForeignKey(Vehicle, related_name='interior_details', default=1, on_delete=models.CASCADE)


class Tuning(models.Model):
    _id = models.AutoField(primary_key=True, blank=True)
    feature = models.CharField(max_length=30, blank=True)
    feature_value = models.CharField(max_length=20, null=True, blank=True)
    details = models.ForeignKey(Vehicle, related_name='tuning_details', default=1, on_delete=models.CASCADE)
