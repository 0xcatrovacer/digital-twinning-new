import requests

# Define the URL of your API endpoint
url = 'http://localhost:8000/api/sensor-data/'  # Update with your actual URL

# Example sensor data as a dictionary (replace with real sensor data)
sensor_data = {
    'acceleration_x': 0.0,
    'acceleration_y': 0.0,
    'acceleration_z': 0.0,
    'gyroscope_x': 0.0,
    'gyroscope_y': 0.0,
    'gyroscope_z': 0.0,
}

values = [str(value).encode('utf-8') for value in sensor_data.values()]

# Convert the values to a space-separated byte string
byte_string = b" ".join(values)


# Send a POST request to your API endpoint with the sensor data
response = requests.post(url, data=byte_string)

# Check the response from the API
if response.status_code == 201:
    print("Sensor data successfully sent and stored.")
elif response.status_code == 400:
    print("Bad request. Check your data format or content.")
else:
    print("Error:", response.status_code)