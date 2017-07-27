from GroveDevices import Grove_PIR_Motion_sensor
motionSensor = Grove_PIR_Motion_sensor("BAA1")
print motionSensor.motionDetected()
