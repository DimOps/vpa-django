from rest_framework import generics as views
from vpa.models.vehicle_notes import (MaintenanceRecord,
                                      VehicleCare,
                                      ToFix,
                                      Notes,
                                      )

from vpa.serializers.vehicle_add_ons_serializers import (MaintenanceListSerializer,
                                                         CareListSerializer,
                                                         ToFixListSerializer,
                                                         NotesListSerializer,
                                                         )


class MaintenanceRecordsView(views.ListAPIView):
    queryset = MaintenanceRecord.objects.all()
    serializer_class = MaintenanceListSerializer

    def get_queryset(self):
        self.lookup_url_kwarg = 'v_id'
        queryset = self.queryset.filter(vehicle__owner__user_id__exact=self.kwargs['owner_id'])\
                                .filter(vehicle_id__exact=self.kwargs['v_id'])
        return queryset.all()


class VehicleCareView(views.ListCreateAPIView):
    queryset = VehicleCare.objects.all()
    serializer_class = CareListSerializer

    def get_queryset(self):
        self.lookup_url_kwarg = 'v_id'
        queryset = self.queryset.filter(vehicle__owner___id__exact=self.kwargs['u_id']) \
            .filter(vehicle_id__exact=self.kwargs['v_id'])
        return queryset.all()


class ToFixView(views.ListCreateAPIView):
    queryset = ToFix.objects.all()
    serializer_class = ToFixListSerializer

    def get_queryset(self):
        self.lookup_url_kwarg = 'v_id'
        queryset = self.queryset.filter(vehicle__owner___id__exact=self.kwargs['u_id']) \
            .filter(vehicle_id__exact=self.kwargs['v_id'])
        return queryset.all()


class VehicleNotesView(views.ListCreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesListSerializer

    def get_queryset(self):
        self.lookup_url_kwarg = 'v_id'
        queryset = self.queryset.filter(vehicle__owner___id__exact=self.kwargs['u_id']) \
            .filter(vehicle_id__exact=self.kwargs['v_id'])
        return queryset.all()