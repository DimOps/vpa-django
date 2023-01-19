from rest_framework import serializers


from vpa.models.vehicle_notes import (MaintenanceRecord,
                                      VehicleCare,
                                      ToFix,
                                      Notes,
                                      MaintenanceRecordDetails,
                                      VehicleCareDetails,
                                      ToFixDetails
                                      )


class MaintenanceListSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaintenanceRecord
        fields = '__all__'


class MaintenanceDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaintenanceRecordDetails
        fields = '__all__'


class CareListSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleCare
        fields = '__all__'


class CareDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleCareDetails
        fields = '__all__'


class ToFixListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToFix
        fields = '__all__'


class ToFixDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToFixDetails
        fields = '__all__'


class NotesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notes
        fields = '__all__'
