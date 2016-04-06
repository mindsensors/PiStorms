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

json_file = '/var/tmp/ps_data.json'
link = 'http://pistorms.mindsensors.com/messenger.php'

cmd = 'cat /proc/cpuinfo | grep Serial | cut -d":" -f2 |awk \'{$1=$1};1\''

serial = commands.getstatusoutput(cmd)[1]

#
# connect to server and get the message
#
link2 = link + "?serial="+str(serial)
try:
    h = urllib.urlopen(link2)
    new_json = json.loads(h.readline())
except:
    #print "connection failed, exiting"
    exit()

# open the local file and read the message to comapre
try:
    f = open(json_file, 'r')
    data = json.loads(f.read())
    m = data['message']
    s = data['status']
    f.close()
except:
    #no local json
    m = ""

# compare the messages:
# remove the white spaces, and see if the message received from server is empty
# if the message is not empty, and if it is different than previous one 
#  then save that new message to local file.
if ( new_json['message'].strip() ):
    if ( m != new_json['message']):
        #print "saving..."
        f = open(json_file, 'w')
        json.dump(new_json, f)
        f.close()
