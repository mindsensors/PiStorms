from GroveDevices import Grove_Air_Quality_Sensor
airQualitySensor = Grove_Air_Quality_Sensor("BAA1")
print airQualitySensor.airQuality()
print airQualitySensor.qualitativeMeasurement()
