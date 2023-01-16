from rest_framework import serializers
from vpa.models.vehicle import Vehicle
from vpa.models.user import User


class IdAndUsernameOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'username')


class VehicleListSerializer(serializers.ModelSerializer):
    owner = IdAndUsernameOwnerSerializer()

    class Meta:
        model = Vehicle
        fields = ('_id', 'type', 'brand', 'model', 'model_spec', 'owner')


class VehicleSerializer(serializers.ModelSerializer):
    owner = IdAndUsernameOwnerSerializer()

    class Meta:
        model = Vehicle
        fields = ('_id', 'type', 'brand', 'model', 'owner')


class DataVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('_id', 'brand', 'model', 'model_spec')


class UserModelSerializer(serializers.ModelSerializer):
    owner_vehicles = DataVehicleSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'


