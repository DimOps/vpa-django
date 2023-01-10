from rest_framework import serializers
from vpa.models.vehicle import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['type', 'brand', 'model']

