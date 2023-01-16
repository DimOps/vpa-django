from rest_framework import generics as views
from vpa.models.vehicle import Vehicle


class MaintenanceRecordsView(views.ListCreateAPIView):
    pass


class VehicleCareView(views.ListCreateAPIView):
    pass


class ToFixView(views.ListCreateAPIView):
    pass


class VehicleNotesView(views.ListCreateAPIView):
    pass