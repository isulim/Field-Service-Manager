from django.urls import path
from Devices.views import HospitalListView, HospitalDetailView, DeviceDetailView, \
    DeviceListView, ManufacturerListView, ManufacturerDetailView, DeviceTypeListView, DeviceTypeDetailView
urlpatterns = [
    path('hospital/', HospitalListView.as_view(), name='hospital-list'),
    path('hospital/<int:pk>/', HospitalDetailView.as_view(), name='hospital-detail'),
    path('device/', DeviceListView.as_view(), name='device-list'),
    path('device/<pk>/', DeviceDetailView.as_view(), name='device-detail'),
    path('type/', DeviceTypeListView.as_view(), name='type-list'),
    path('type/<int:pk>', DeviceTypeDetailView.as_view(), name='type-detail'),
    path('manufacturer/', ManufacturerListView.as_view(), name='manufacturer-list'),
    path('manufacturer/<int:pk>', ManufacturerDetailView.as_view(), name='manufacturer-detail'),
]
