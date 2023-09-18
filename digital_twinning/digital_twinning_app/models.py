from django.db import models

class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    acceleration_x = models.FloatField()
    acceleration_y = models.FloatField()
    acceleration_z = models.FloatField()
    gyroscope_x = models.FloatField()
    gyroscope_y = models.FloatField()
    gyroscope_z = models.FloatField()
    magnetometer_x = models.FloatField()
    magnetometer_y = models.FloatField()
    magnetometer_z = models.FloatField()

    def __str__(self):
        return f"Sensor Data at {self.timestamp}"
