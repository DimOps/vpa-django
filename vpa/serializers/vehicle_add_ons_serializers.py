from rest_framework import serializers


from vpa.models.vehicle_notes import MaintenanceRecord, VehicleCare, ToFix, Notes

from vpa.serializers.vehicle_serializers import VehicleSerializer


class MaintenanceListSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()

    class Meta:
        model = MaintenanceRecord
        fields = '__all__'


class CareListSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()

    class Meta:
        model = VehicleCare
        fields = '__all__'


class ToFixListSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()

    class Meta:
        model = ToFix
        fields = '__all__'


class NotesListSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()

    class Meta:
        model = Notes
        fields = '__all__'
