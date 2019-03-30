from django.urls import path
from Devices.views import HospitalListView, HospitalDetailView, DeviceListView, DeviceDetailView, \
    DeviceTypeListView, DeviceTypeDetailView, ManufacturerListView, ManufacturerDetailView, \
    CaretakerListView, CaretakerDetailView

urlpatterns = [
    path('hospital/', HospitalListView.as_view(), name='hospital-list'),
    path('hospital/<int:pk>/', HospitalDetailView.as_view(), name='hospital-detail'),
    path('device/', DeviceListView.as_view(), name='device-list'),
    path('device/<pk>/', DeviceDetailView.as_view(), name='device-detail'),
    path('type/', DeviceTypeListView.as_view(), name='type-list'),
    path('type/<int:pk>/', DeviceTypeDetailView.as_view(), name='type-detail'),
    path('manufacturer/', ManufacturerListView.as_view(), name='manufacturer-list'),
    path('manufacturer/<int:pk>/', ManufacturerDetailView.as_view(), name='manufacturer-detail'),
    path('caretaker/', CaretakerListView.as_view(), name='caretaker-list'),
    path('caretaker/<int:pk>/', CaretakerDetailView.as_view(), name='caretaker-detail')
]
