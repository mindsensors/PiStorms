#!/usr/bin/env python
#
# Copyright (c) 2015 mindsensors.com
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
#mindsensors.com invests time and resources providing this open source code, 
#please support mindsensors.com  by purchasing products from mindsensors.com!
#Learn more product option visit us @  http://www.mindsensors.com/
#
# History:
# Date            Author            Comments
# 10/02/15    Deepak            Initial authoring.

import urllib, json
import commands
from datetime import datetime, timedelta
import time

version_json_file = '/var/tmp/ps_versions.json'
sw_version_file = '/home/pi/PiStorms/.version'
hw_version_file = '/var/tmp/.hw_version'
link = 'http://pistorms.mindsensors.com/versions.php'

cmd = 'cat /proc/cpuinfo | grep Serial | cut -d":" -f2 |awk \'{$1=$1};1\''
serial = commands.getstatusoutput(cmd)[1]

try:
    f = open(version_json_file, 'r')
    data = json.loads(f.read())
    s = data['status']
    d = data['date']
    f.close()
except:
    #no local json
    s = ""
if ( s == "Never" ):
    exit(0)

if ( s == "Later" ):
    #
    # defer for 9 hours since user's decision.
    #
    last_time = datetime.strptime(d, "%Y:%m:%d:%H:%M")
    td = timedelta(hours=9)
    update_time = last_time + td
    if ( datetime.now() < update_time ):
        exit(0)
    # wait for a day since last check

# find sw version on this pi.
try:
    f = open(sw_version_file, 'r')
    sw_version = f.read()
    sw_version = sw_version.strip()
    f.close()
except:
    sw_version = "0.000"

# find hw version on this pi.
try:
    f = open(hw_version_file, 'r')
    hw_version = f.read()
    hw_version = hw_version.strip()
    f.close()
except:
    hw_version = "0.000"

#
# connect to server and get the message
# and save the json file.
#

link2 = link+"?serial="+str(serial)+"&sw_ver="+str(sw_version)+"&hw_ver="+str(hw_version) 
try:
    h = urllib.urlopen(link2)
    new_json = json.loads(h.readline())
    f = open(version_json_file, 'w')
    #
    # Compare the versions from json and values read from disk files,
    # and if update is required, write as such in the json file.
    #
    update_required = 0
    if ( sw_version < new_json['sw_ver'] ):
        update_required = 1

    if ( hw_version < new_json['hw_ver'] ):
        if ( update_required == 1 ):
            update_required = 4
        else:
            update_required = 2

    if (update_required == 1):
            upd = "software"

    if (update_required == 2):
            upd = "hardware"

    if (update_required == 4):
            upd = "both"

    if (update_required == 0):
            upd = "none"

    new_json['update'] = upd
    json.dump(new_json, f)
    f.close()
except:
    #print "connection failed, exiting"
    exit()



