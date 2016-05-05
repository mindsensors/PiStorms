#!/usr/bin/env python

from PiStorms import PiStorms
import sys, subprocess
import socket

version_json_file = '/var/tmp/ps_versions.json'

psm = PiStorms()
    
def available():
    try:
        socket.setdefaulttimeout(5)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
        return True
    except Exception as e: pass
    return False

opt = str(sys.argv[1])

isConnected = available()
if (isConnected == False):
    m = ["Software Updater", "You are not connected to Internet.",
      "Internet connection required"]
    psm.screen.askQuestion(m,["OK"])
    sys.exit(-1)

print "running software_update.py"

try:
    f = open(version_json_file, 'r')
    data = json.loads(f.read())
    sw_version = data['sw_ver']
    f.close()
except:
    # no local json
	# this can happen on old systems, so upgrade them to 4.000
    sw_version = "4.000"

psm.screen.termPrintAt(3, "Downloading the update")
psm.screen.termPrintAt(4, "Please wait...")

sw_file_name = "PiStorms." + sw_version + ".tar.gz"
cmd = "wget http://www.mindsensors.com/largefiles/updater/" + sw_file_name
subprocess.call(cmd, shell=True)


psm.screen.termPrintAt(3, "Download complete")
psm.screen.termPrintAt(4, "              ")



