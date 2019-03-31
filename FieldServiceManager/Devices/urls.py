from django.urls import path
from Devices.views import HospitalListView, HospitalDetailView, DeviceListView, DeviceDetailView, \
    DeviceTypeListView, DeviceTypeDetailView, ManufacturerListView, ManufacturerDetailView, \
    CaretakerListView, CaretakerDetailView, HospitalCreateView, DeviceCreateView, \
    CaretakerCreateView

urlpatterns = [
    path('hospital/', HospitalListView.as_view(), name='hospital-list'),
    path('hospital/<int:pk>/', HospitalDetailView.as_view(), name='hospital-detail'),
    path('hospital/create/', HospitalCreateView.as_view(), name='hospital-create'),
    path('device/', DeviceListView.as_view(), name='device-list'),
    path('device/<int:pk>/', DeviceDetailView.as_view(), name='device-detail'),
    path('device/create/', DeviceCreateView.as_view(), name='device-create'),
    path('type/', DeviceTypeListView.as_view(), name='type-list'),
    path('type/<int:pk>/', DeviceTypeDetailView.as_view(), name='type-detail'),
    path('manufacturer/', ManufacturerListView.as_view(), name='manufacturer-list'),
    path('manufacturer/<int:pk>/', ManufacturerDetailView.as_view(), name='manufacturer-detail'),
    path('caretaker/', CaretakerListView.as_view(), name='caretaker-list'),
    path('caretaker/<int:pk>/', CaretakerDetailView.as_view(), name='caretaker-detail'),
    path('caretaker/create/', CaretakerCreateView.as_view(), name='caretaker-create'),
]
