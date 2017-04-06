from PiStorms import PiStorms
import MsDevices
import time

psm = PiStorms()
irt = MsDevices.IRThermometer(psm.BAS1)

while (True):
    #print "vendor:", irt.GetVendorName()
    #time.sleep(0.1)
    #print "device:", irt.GetDeviceId()
    #time.sleep(0.1)
    #print "Target (celsius):", irt.readTargetCelsius()
    #time.sleep(0.1)
    #print "Ambient (celsius):", irt.readAmbientCelsius()
    #time.sleep(1)
    print "Target (fahr):", irt.readTargetFahr()
    time.sleep(0.1)
    print "Ambient (fahr):", irt.readAmbientFahr()
    time.sleep(1)
    print ""
