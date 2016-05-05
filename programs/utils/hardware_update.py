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
    m = ["Hardware Updater", "You are not connected to Internet.",
      "Internet connection required"]
    psm.screen.askQuestion(m,["OK"])
    sys.exit(-1)

print "running hardware_update.py"

m = ["Hardware Updater", "Not Yet Implemented.",
  "Please refer to blog for manual steps:",
  "",
  "http://www.mindsensors.com/blog" ]
psm.screen.askQuestion(m,["OK"])
sys.exit(-1)
