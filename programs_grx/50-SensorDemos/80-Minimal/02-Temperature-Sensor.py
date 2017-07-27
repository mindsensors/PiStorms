from GroveDevices import Grove_Temperature_Sensor
temperatureSensor = Grove_Temperature_Sensor("BAA1")
print temperatureSensor.temperature()
print Grove_Temperature_Sensor.CtoF(temperatureSensor.temperature())
