from rest_framework import generics as views
from rest_framework.generics import get_object_or_404

from vpa.models.vehicle import Vehicle
from vpa.models.user import User
from vpa.serializers.vehicle_serializers import (VehicleListSerializer,
                                                 UserModelSerializer,
                                                 VehicleInfoSerializer,
                                                 )


class SingleUserView(views.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'owner_id'
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class ListUserVehiclesView(views.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleListSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)

    def get_queryset(self):
        queryset = self.queryset.filter(owner__user_id=self.kwargs['owner_id'])
        return queryset.all()


class SingleCarDetailsView(views.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleInfoSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.multiple_lookup_fields = ('owner_id', 'v_id')

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)

    def get_object(self):
        queryset = self.get_queryset()
        filters = {}
        for field in self.multiple_lookup_fields:
            filters[field] = self.kwargs[field]

        obj = get_object_or_404(queryset, **filters)
        self.check_object_permissions(self.request, obj)
        return obj
