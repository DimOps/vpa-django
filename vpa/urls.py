from django.urls import path
from vpa.views.vehicles import (ListUserVehiclesView,
                                SingleUserView,
                                SingleCarDetailsView,
                                )

from vpa.views.vehicle_add_ons import (MaintenanceRecordView,
                                       VehicleCareView,
                                       ToFixView,
                                       VehicleNotesView,
                                       MaintenanceRecordDetailsView,
                                       VehicleCareDetailsView,
                                       ToFixDetailsView,
                                       )

urlpatterns = (
    path('<int:owner_id>/', SingleUserView.as_view(), name='user-all-vehicles'),
    path('<int:owner_id>/vehicles/', ListUserVehiclesView.as_view(), name='all-vehicles'),
    path('<int:owner_id>/vehicles/<int:v_id>/details/', SingleCarDetailsView.as_view(), name='vehicle-details'),
    path('<int:owner_id>/vehicles/<int:v_id>/record/', MaintenanceRecordView.as_view(), name='vehicle-records'),
    path('<int:owner_id>/vehicles/<int:v_id>/record/<int:mrd_id>/',
         MaintenanceRecordDetailsView.as_view(), name='vehicle-record-details'),
    path('<int:owner_id>/vehicles/<int:v_id>/vehicle-care/', VehicleCareView.as_view(), name='vehicle-care'),
    path('<int:owner_id>/vehicles/<int:v_id>/vehicle-care/<int:vcd_id>/',
         VehicleCareDetailsView.as_view(), name='vehicle-care-details'),
    path('<int:owner_id>/vehicles/<int:v_id>/to-fix/', ToFixView.as_view(), name='vehicle-to-fix'),
    path('<int:owner_id>/vehicles/<int:v_id>/to-fix/<int:tfd_id>/',
         ToFixDetailsView.as_view(), name='vehicle-to-fix-details'),
    path('<int:owner_id>/vehicles/<int:_id>/notes/', VehicleNotesView.as_view(), name='vehicle-notes'),
)
