"""FieldServiceManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ServiceJobs.views import HospitalListView, HospitalDetailView, DeviceDetailView, \
    DeviceListView, DeviceManufacturerListView, DeviceByTypeListView, DeviceTypesList, \
    DeviceManufacturersList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hospital/', HospitalListView.as_view(), name='hospital-list'),
    path('hospital/<int:pk>/', HospitalDetailView.as_view(), name='hospital-detail'),
    path('device/', DeviceListView.as_view(), name='device-list'),
    path('device/<int:pk>/', DeviceDetailView.as_view(), name='device-detail'),
    path('device/type/', DeviceTypesList.as_view(), name='device-types'),
    path('device/type/<int:devtype>', DeviceByTypeListView.as_view(), name='device-by-type-list'),
    path('device/manufacturer/', DeviceManufacturersList.as_view(), name='device-manufacturers'),
    path('device/manufacturer/<int:manufacturer>', DeviceManufacturerListView.as_view(), name='device-by-manufacturer-list'),
]
