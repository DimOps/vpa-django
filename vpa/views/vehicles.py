from rest_framework import generics as views
from vpa.models.vehicle import Vehicle, VehicleDetails
from vpa.models.user import User
from vpa.serializers.vehicle_serializers import (VehicleListSerializer,
                                                 VehicleSerializer,
                                                 UserModelSerializer,
                                                 VehicleDetailsSerializer,)


class ListUserVehiclesView(views.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleListSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)

    def get_queryset(self):
        queryset = self.queryset.filter(owner___id=self.kwargs['u_id'])
        return queryset.all()


class SingleCarView(views.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)

    def get_queryset(self):
        self.lookup_url_kwarg = 'v_id'
        queryset = self.queryset\
            .filter(owner_id=self.kwargs['u_id'])\
            .filter(_id__exact=self.kwargs['v_id'])
        return queryset.all()


class SingleUserView(views.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class SingleCarDetailsView(views.RetrieveUpdateDestroyAPIView):
    queryset = VehicleDetails.objects.all()
    serializer_class = VehicleDetailsSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)

    def get_queryset(self):
        self.lookup_url_kwarg = 'v_id'
        queryset = self.queryset.filter(_id__exact=self.kwargs['v_id'])
        return queryset.all()
