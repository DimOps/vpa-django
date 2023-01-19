from rest_framework import serializers, viewsets
from vpa.models.vehicle import Vehicle, VehicleDetails, Chassis, Tuning, Exterior, Interior
from vpa.models.user import User


class IdAndUsernameOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'username')


class VehicleListSerializer(serializers.ModelSerializer):
    owner = IdAndUsernameOwnerSerializer()

    class Meta:
        model = Vehicle
        fields = ('v_id', 'type', 'brand', 'model', 'model_spec', 'owner')


class VehicleSerializer(serializers.ModelSerializer):
    owner = IdAndUsernameOwnerSerializer()

    class Meta:
        model = Vehicle
        fields = ('v_id', 'type', 'brand', 'model', 'category', 'owner')


class DataVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('v_id', 'brand', 'model', 'model_spec')


class UserModelSerializer(serializers.ModelSerializer):
    owner_vehicles = DataVehicleSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class VehicleChassisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chassis
        fields = '__all__'


class VehicleInteriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interior
        fields = '__all__'


class VehicleExteriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exterior
        fields = '__all__'


class VehicleTuningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuning
        fields = '__all__'

class VehicleDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleDetails
        fields = '__all__'


class VehicleInfoSerializer(serializers.ModelSerializer):
    vehicle_details = VehicleDetailsSerializer(many=True, read_only=True)
    interior_details = VehicleInteriorSerializer(many=True, read_only=True)
    exterior_details = VehicleExteriorSerializer(many=True, read_only=True)
    tuning_details = VehicleTuningSerializer(many=True, read_only=True)
    chassis_details = VehicleChassisSerializer(many=True, read_only=True)

    class Meta:
        model = Vehicle
        fields = '__all__'

