from rest_framework import generics as views
from rest_framework.generics import get_object_or_404

from vpa.models.vehicle_notes import (MaintenanceRecord,
                                      VehicleCare,
                                      ToFix,
                                      Notes,
                                      MaintenanceRecordDetails,
                                      )

from vpa.serializers.vehicle_add_ons_serializers import (MaintenanceListSerializer,
                                                         CareListSerializer,
                                                         ToFixListSerializer,
                                                         NotesListSerializer,
                                                         MaintenanceDetailsSerializer,
                                                         )


class MaintenanceRecordView(views.ListCreateAPIView):
    queryset = MaintenanceRecord.objects.all()
    serializer_class = MaintenanceListSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)

    def get_queryset(self):
        self.lookup_url_kwarg = 'v_id'
        queryset = self.queryset.filter(vehicle__owner__user_id=self.kwargs['owner_id'])\
                                .filter(vehicle_id=self.kwargs['v_id'])

        return queryset.all()


class MaintenanceRecordDetailsView(views.RetrieveUpdateDestroyAPIView):
    queryset = MaintenanceRecordDetails.objects.all()
    serializer_class = MaintenanceDetailsSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.multiple_lookup_fields = ('mrd_id',)
    # TODO:
    # restrain the URL
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


class VehicleCareView(views.ListCreateAPIView):
    queryset = VehicleCare.objects.all()
    serializer_class = CareListSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)

    def get_queryset(self):
        self.lookup_url_kwarg = 'v_id'
        queryset = self.queryset.filter(vehicle__owner__user_id=self.kwargs['u_id']) \
            .filter(vehicle_id=self.kwargs['v_id'])
        return queryset.all()


class VehicleCareDetailsView(views.RetrieveUpdateDestroyAPIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.multiple_lookup_fields = ('vcd_id',)

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


class ToFixView(views.ListCreateAPIView):
    queryset = ToFix.objects.all()
    serializer_class = ToFixListSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)

    def get_queryset(self):
        self.lookup_url_kwarg = 'v_id'
        queryset = self.queryset.filter(vehicle__owner__user_id=self.kwargs['u_id']) \
            .filter(vehicle_id=self.kwargs['v_id'])
        return queryset.all()


class ToFixDetailsView(views.RetrieveUpdateDestroyAPIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.multiple_lookup_fields = ('tfd_id',)

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


class VehicleNotesView(views.ListCreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesListSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)

    def get_queryset(self):
        self.lookup_url_kwarg = 'v_id'
        queryset = self.queryset.filter(vehicle__owner__user_id=self.kwargs['u_id']) \
            .filter(vehicle_id=self.kwargs['v_id'])
        return queryset.all()