from django.urls import path
from vpa.views import ListUserVehiclesView, SingleCarView, SingleUserView

urlpatterns = (
    path('<int:pk>/', SingleUserView.as_view(), name='user-all-cars'),
    path('<int:pk>/vehicles/', ListUserVehiclesView.as_view(), name='all-cars'),
    path('users/vehicles/<int:pk>/', SingleCarView.as_view(), name='single-car'),
)
