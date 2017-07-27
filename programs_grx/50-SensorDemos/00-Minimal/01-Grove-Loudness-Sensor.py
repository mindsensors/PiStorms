from GroveDevices import Grove_Loudness_Sensor
loudnessSensor = Grove_Loudness_Sensor("BAA1")
print loudnessSensor.detectSound()
