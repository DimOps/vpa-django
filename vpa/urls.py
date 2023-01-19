from django.urls import path
from vpa.views.vehicles import (ListUserVehiclesView,
                                SingleUserView,
                                SingleCarDetailsView,
                                )

from vpa.views.vehicle_add_ons import (MaintenanceRecordsView,
                                       VehicleCareView,
                                       ToFixView,
                                       VehicleNotesView,)

urlpatterns = (
    path('<int:owner_id>/', SingleUserView.as_view(), name='user-all-vehicles'),
    path('<int:owner_id>/vehicles/', ListUserVehiclesView.as_view(), name='all-vehicles'),
    path('<int:owner_id>/vehicles/<int:v_id>/details/', SingleCarDetailsView.as_view(), name='vehicle-details'),
    path('<int:owner_id>/vehicles/<int:v_id>/record/', MaintenanceRecordsView.as_view(), name='vehicle-record'),
    path('<int:owner_id>/vehicles/<int:v_id>/vehicle-care/', VehicleCareView.as_view(), name='vehicle-care'),
    path('<int:owner_id>/vehicles/<int:v_id>/to-fix/', ToFixView.as_view(), name='vehicle-to-fix'),
    path('<int:owner_id>/vehicles/<int:_id>/notes/', VehicleNotesView.as_view(), name='vehicle-notes'),
)
