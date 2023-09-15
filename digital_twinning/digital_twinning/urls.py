from django.contrib import admin
from django.urls import path, include
from digital_twinning_app import views
from digital_twinning_app.views import SensorDataAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.sensor_data_page, name='root'),
    path('sensor_data/', views.sensor_data_page, name='sensor_data_page'),
    path('api/sensor_data/', views.api_sensor_data, name='api_sensor_data')
]