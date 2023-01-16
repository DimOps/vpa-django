from rest_framework import serializers
from vpa.models.vehicle import Vehicle, VehicleDetails
from vpa.models.user import User


class IdAndUsernameOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('_id', 'username')


class VehicleListSerializer(serializers.ModelSerializer):
    owner = IdAndUsernameOwnerSerializer()

    class Meta:
        model = Vehicle
        fields = ('_id', 'type', 'brand', 'model', 'model_spec', 'owner')


class VehicleSerializer(serializers.ModelSerializer):
    owner = IdAndUsernameOwnerSerializer()

    class Meta:
        model = Vehicle
        # fields = ('_id', 'type', 'brand', 'model', 'owner')
        fields = '__all__'


class DataVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('_id', 'brand', 'model', 'model_spec')


class UserModelSerializer(serializers.ModelSerializer):
    owner_vehicles = DataVehicleSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class VehicleDetailsSerializer(serializers.ModelSerializer):
    vehicle = DataVehicleSerializer()

    class Meta:
        model = VehicleDetails
        fields = '__all__'

