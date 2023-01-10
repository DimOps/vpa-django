from django.urls import path
from vpa.views import ListVehiclesView
urlpatterns = (
    path('', ListVehiclesView.as_view(), name='all-cars'),
)