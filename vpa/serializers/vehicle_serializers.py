from django.contrib.auth.models import User
from rest_framework import serializers
from vpa.models.vehicle import Vehicle, VehicleDetails, Chassis, Tuning, Exterior, Interior


class IdAndUsernameOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class VehicleListSerializer(serializers.ModelSerializer):
    owner = User

    class Meta:
        model = Vehicle
        fields = ('v_id', 'type', 'brand', 'model', 'model_spec', 'owner')

    def create(self, validated_data):
        pk = self.context['request'].path.split('/')[1]

        if pk != validated_data['owner'].user_id:
            raise Exception('This user cannot create on behalf of someone else')
        return Vehicle.objects.create(**validated_data)


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

