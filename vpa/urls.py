from django.urls import path
from vpa.views.vehicles import (ListUserVehiclesView,
                                SingleCarView,
                                SingleUserView,
                                SingleCarDetailsView,)

from vpa.views.vehicle_add_ons import (MaintenanceRecordsView,
                                       VehicleCareView,
                                       ToFixView,
                                       VehicleNotesView,)

urlpatterns = (
    path('<int:pk>/', SingleUserView.as_view(), name='user-all-vehicles'),
    path('<int:u_id>/vehicles/', ListUserVehiclesView.as_view(), name='all-vehicles'),
    path('<int:u_id>/vehicles/<int:v_id>/', SingleCarView.as_view(), name='single-user-vehicles'),
    path('<int:u_id>/vehicles/<int:v_id>/details/', SingleCarDetailsView.as_view(), name='vehicle-details'),
    # path('<int:u_id>/vehicles/<int:v_id>/record/', MaintenanceRecordsView.as_view(), name='single-user-car'),
    # path('<int:u_id>/vehicles/<int:v_id>/vehicle-care/', VehicleCareView.as_view(), name='single-user-car'),
    # path('<int:u_id>/vehicles/<int:v_id>/to-fix/', ToFixView.as_view(), name='single-user-car'),
    # path('<int:u_id>/vehicles/<int:v_id>/notes/', VehicleNotesView.as_view(), name='single-user-vehicle'),
)
