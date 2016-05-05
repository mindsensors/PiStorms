#!/usr/bin/env python

from PiStorms import PiStorms
import sys, subprocess, json
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
    m = ["HW/SW Updater", "You are not connected to Internet.",
      "Internet connection required"]
    psm.screen.askQuestion(m,["OK"])
    sys.exit(-1)

print "running both_update.py"

m = ["HW/SW Updater", "Not Yet Implemented.",
  "Please contact mindsensors support",
  "for instructions",
  "",
  "support@mindsensors.com" ]
psm.screen.askQuestion(m,["OK"])
sys.exit(-1)
