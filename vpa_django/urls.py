from django.contrib import admin
from django.urls import path, include

from vpa.views.profile import RegisterProfile

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include('vpa.urls')),
    path('register/', RegisterProfile.as_view(), name='register'),
)
