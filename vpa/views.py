from rest_framework.response import Response
from rest_framework.views import APIView

from vpa.models import Vehicle
from vpa.serializers import VehicleSerializer


class ListVehiclesView(APIView):
    def get(self, request):
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response({'Vehicles': serializer.data})