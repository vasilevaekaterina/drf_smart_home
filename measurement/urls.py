from . import views
from django.urls import path

urlpatterns = [
    path('sensors/', views.SensorListCreateView.as_view(),
         name='sensor-list-create'),
    path('sensors/<int:pk>/', views.SensorRetrieveUpdateView.as_view(),
         name='sensor-detail'),
    path('measurements/', views.MeasurementCreateView.as_view(),
         name='measurement-create'),
]
