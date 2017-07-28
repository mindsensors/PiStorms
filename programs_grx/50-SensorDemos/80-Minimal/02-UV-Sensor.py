from GroveDevices import Grove_UV_Sensor
uvSensor = Grove_UV_Sensor("BAA1")
print uvSensor.intensity()
print uvSensor.UVindex()
