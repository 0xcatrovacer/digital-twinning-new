from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .models import SensorData
from django.http import JsonResponse
import csv


def read_csv_file(file_path):
    sensor_data_list = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            sensor_data_list.append(row)
    return sensor_data_list

class SensorDataAPI(APIView):
    def post(self, request):
        try:
            
            input_string = request.body.decode("utf-8")

            
            values = input_string.split(" ")

            
            keys = ['acceleration_x', 'acceleration_y', 'acceleration_z', 'gyroscope_x', 'gyroscope_y', 'gyroscope_z', 'magnetometer_x', 'magnetometer_y', 'magnetometer_z']

            
            sensor_data = {key: float(value) for key, value in zip(keys, values)}
        except (ValueError, UnicodeDecodeError):
            return Response({"message": "Invalid sensor data format"}, status=status.HTTP_400_BAD_REQUEST)

        if not sensor_data:
            return Response({"message": "No sensor data received"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            SensorData.objects.create(**sensor_data)  # Store the sensor data in the database
            return Response({"message": "Sensor data received and saved successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": f"Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def sensor_data_page(request):
    sensor_data = SensorData.objects.first()
    context = {
        'sensor_data': sensor_data,
    }
    return render(request, 'digital_twinning_app/sensor_data.html', context)


current_row = 0

# For serving the JSON data
def api_sensor_data(request):
    global current_row
    sensor_data_list = read_csv_file('./digital_twinning_app/static/data/output_data.csv')

    if current_row >= len(sensor_data_list):
        current_row = 0

    data = sensor_data_list[current_row]
    current_row += 1

    return JsonResponse(data)
