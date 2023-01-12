from rest_framework import generics as views
from vpa.models.vehicle import Vehicle
from vpa.models.user import User
from vpa.serializers.vehicle_serializers import VehicleListSerializer, VehicleSerializer, UsersListSerializer, \
    UserModelSerializer


class ListUserVehiclesView(views.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleListSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)

    def get_queryset(self):
        queryset = self.queryset.filter(owner__user_id=self.kwargs['pk'])
        return queryset.all()


class SingleCarView(views.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class SingleUserView(views.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
