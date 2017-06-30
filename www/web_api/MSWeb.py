#!/usr/bin/env python
#
# Copyright (c) 2016 mindsensors.com
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
# Date              Author          Comments
# July 2016         Roman Bohuk     Initial Authoring
# December 2016     Roman Bohuk     Added functionality to rename files

from datetime import timedelta, date
from flask import Flask, make_response, request, current_app
from functools import update_wrapper
import os
import shutil

# http://flask.pocoo.org/snippets/56/
def crossdomain(origin=None, methods=None, headers=None, max_age=21600, attach_to_all=True, automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

# http://stackoverflow.com/a/6803714/3600428
def dirTraversal(file_name, current_directory):
    requested_path = os.path.relpath(file_name, start=current_directory)
    requested_path = os.path.abspath(requested_path)
    common_prefix = os.path.commonprefix([requested_path, current_directory])
    return common_prefix != current_directory


app = Flask(__name__)

from PiStormsCom import PiStormsCom
psc = PiStormsCom()

import MS_ILI9341
import Adafruit_GPIO.SPI as SPI
disp = MS_ILI9341.ILI9341(24, rst=25, spi=SPI.SpiDev(0,0,max_speed_hz=64000000))

import socket,fcntl,struct
def get_ip_address(ifname):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15])
        )[20:24])
    except:
        return "not present"


import json
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("/usr/local/mindsensors/conf/msdev.cfg")
home_folder = config.get("msdev","homefolder")

message_file = '/var/tmp/ps_data.json'
messages = {"date": "", "status": "None", "message": "none"}
message_text = '{"date": "", "status": "None", "message": "none"}'
try:
    with open(message_file, "r") as data_file:
        message_text = data_file.read()
except: message_text = '{"date": "", "status": "None", "message": "none"}'

messages = json.loads(message_text)
@app.route("/")
def index():
    return "PiStorms Web API"

@app.route("/firmware", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def firmware():
    return str(psc.GetFirmwareVersion())

@app.route("/software", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def software():
    try:
        with open(os.path.join(home_folder, ".version"), "r") as f:
            return f.read()
    except: return "Undefined"

@app.route("/device", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def device():
    return str(psc.GetDeviceId())

@app.route("/eth0", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def eth0():
    return get_ip_address('eth0')

@app.route("/wlan0", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def wlan0():
    return get_ip_address('wlan0')

@app.route("/battery", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def battery():
    return str(psc.battVoltage())

@app.route("/reboot", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def reboot():
    os.system("sleep 1; sudo psm_shutdown -r now")
    return "1"

@app.route("/shutdown", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def shutdown():
    os.system("sleep 1; sudo psm_shutdown -h now")
    return "1"

@app.route("/led", methods=['GET', 'OPTIONS', 'POST'])
@crossdomain(origin='*')
def led():
    if request.method == 'POST':
        led = request.form['led']
        red = request.form['red']
        blue = request.form['blue']
        green = request.form['green']
        if led in ['1','2'] and red.isdigit() and blue.isdigit() and green.isdigit():
            red = int(red) % 256
            blue = int(blue) % 256
            green = int(green) % 256
            psc.led(int(led),red,green,blue)
    return "1"

@app.route("/starttouchrecording", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def starttouchrecording():
    disp.startTouchRecording("-")
    return "1"

@app.route("/startrecording", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def startrecording():
    disp.startRecording("-", includeBg=False)
    return "1"

@app.route("/startrecording/withBg", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def startrecordingwithBg():
    disp.startRecording("-",includeBg=True)
    return "1"

@app.route("/stoprecording", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def stoprecording():
    disp.stopRecording()
    return "1"

@app.route("/stoptouchrecording", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def stoptouchrecording():
    disp.stopTouchRecording()
    return "1"

@app.route("/readrecording", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def readrecording():
    return str(int(disp.isTakingFrames(disp.readRecordingCount()[0])))

@app.route("/readrecordingtouch", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def readrecordingtouch():
    return str(int(disp.isTakingFrames(disp.readTouchRecordingCount()[0])))

@app.route("/clearimages", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def clearimages():
    folder = '/var/tmp/ps_images'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        if os.path.isfile(file_path):
            os.system("sudo rm " + file_path)
    return "1"

@app.route("/stopbrowser", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def stopbrowser():
    disp.display()
    os.system("sudo /etc/init.d/MSBrowser.sh stop")
    return "1"

def browserrunning():
    ps = os.popen('ps -ef').read().split("\n")
    for i in ps:
        if "MSBrowser.py" in i:
            return "1"
    return "0"

@app.route("/startbrowser", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def startbrowser():
    if browserrunning() == "1":
        print "Browser Already Running"
        return "0"
    os.system("sudo /etc/init.d/MSBrowser.sh start")
    print "Started Browser"
    return "1"

@app.route("/getapacheerrors", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def getapacheerrors():
    return os.popen('cat /var/log/apache2/error.log').read()

@app.route("/getmessage", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def getmessage():
    return messages["message"]

@app.route("/markmessageread", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def markmessageread():
    messages["status"] = "Read"
    try:
        f = open(message_file, 'w+')
        json.dump(messages, f)
        f.close()
    except: return "0"
    return "1"

@app.route("/getmessagejson", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def getmessagejson():
    return message_text

@app.route("/getprograms", methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def getprograms():
    files = os.listdir(os.path.join(home_folder, "programs", request.form["path"]))

    if not request.form["path"].startswith(os.path.abspath(os.path.join(home_folder, "programs"))+'/'): return "0"

    out = []
    for i in files:
        dir = os.path.join(home_folder, "programs", request.form["path"], i)
        typ = ""
        if os.path.isdir(dir): typ = "folder"
        elif os.path.isfile(dir): typ = os.path.splitext(dir)[1][1::].lower()
        if typ == "py":
            with open(dir) as f:
                c = f.read()
                if ("--BLOCKLY FILE--" in c):
                    typ = "bl"
        if (typ == "folder" or typ == "py" or typ == "bl") and i[:2].isdigit():
            out.append([i,dir,typ])
    out.sort()
    return json.dumps(out)

@app.route("/fetchscript", methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def fetchscript():
    try:
        with open(request.form["path"],"r") as f:
            return f.read()
    except: return "0"

@app.route("/removefile", methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def removefile():
    try:
        if os.path.isfile(request.form["path"]) and request.form["path"].startswith(os.path.abspath(os.path.join(home_folder, "programs"))+'/'):
            os.remove(request.form["path"])
        return "1"
    except: return "0"

@app.route("/removedir", methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def removedir():
    try:
        if os.path.isdir(request.form["path"]) and request.form["path"].startswith(os.path.abspath(os.path.join(home_folder, "programs"))+'/') and os.path.normpath(request.form["path"]) != os.path.normpath(os.path.abspath(os.path.join(home_folder, "programs"))):
            shutil.rmtree(request.form["path"])
        return "1"
    except Exception as e:
        return "0"

copyright = """
# Copyright (c) %i mindsensors.com
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
""" % date.today().year

@app.route("/addobject", methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def addobject():
    try:
        if not (os.path.isdir(request.form["path"]) and request.form["type"] in ["folder","py","bl"] and request.form["path"] and request.form["path"].startswith(os.path.abspath(os.path.join(home_folder, "programs"))+'/')):
            return "0";
        filename = os.path.basename(request.form["filename"].rstrip(os.sep))
        folderpath = os.path.join(request.form["path"], filename)
        if request.form["type"] == "folder":
            if not os.path.exists(folderpath):
                os.makedirs(folderpath)
        if request.form["type"] == "py" or request.form["type"] == "bl":
            if not filename.endswith(".py"): filename += ".py"
            folderpath = os.path.join(request.form["path"], filename)
            with open(folderpath, "w+") as f:
                if request.form["type"] == "bl": f.write('#!/usr/bin/env python\n\n# ATTENTION!\n# Please do not manually edit the contents of this file\n# Only use the web interface for editing\n# Otherwise, the file may no longer be editable using the web interface, or you changes may be lost\n' + copyright + '\n"""\n--BLOCKLY FILE--\n--START BLOCKS--\nPHhtbCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PC94bWw+\ndcb89b3f89fc910d631112bf6140e47513c301e5bcf76a08a1b4d66ab1ca58d3\n--END BLOCKS--\n"""\n\n')
                if request.form["type"] == "py": f.write('#!/usr/bin/env python\n\n')
        os.system("sudo chown -R pi:pi %s" % folderpath)
        return "1"
    except Exception as e:
        return "0"

@app.route("/renameobject", methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def renameobject():
    try:
        if not (os.path.isdir(request.form["path"]) and request.form["path"] and request.form["path"].startswith(os.path.abspath(os.path.join(home_folder, "programs"))+'/')):
            return "0";
        filename = os.path.basename(request.form["filename"].rstrip(os.sep))
        folderpath = os.path.join(request.form["path"], filename)
        filenamenew = os.path.basename(request.form["filenamenew"].rstrip(os.sep))
        folderpathnew = os.path.join(request.form["path"], filenamenew)
        os.renames(folderpath,folderpathnew)
        os.system("sudo chown -R pi:pi %s" % folderpathnew)
        return "1"
    except Exception as e:
        return "0"

@app.route("/savescript", methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def savescript():
    try:
        with open(request.form["path"],"w+") as f:
            f.write(request.form["contents"])
            return "1"
    finally: return "0"

@app.route("/setmotorspeed", methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def setmotorspeed():
    try:
        psc.BAM1.setSpeed(-int(request.form["right"]))
        psc.BAM2.setSpeed(-int(request.form["left"]))
    except Exception as e:
        pass
    return "1"

@app.route("/floatmotors", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def floatmotors():
    psc.BAM1.float()
    psc.BAM2.float()
    return "1"

@app.route("/brakemotors", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def brakemotors():
    psc.BAM1.brake()
    psc.BAM2.brake()
    return "1"

@app.route("/getprogramsdir", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def getprogramsdir():
    return os.path.abspath(os.path.join(home_folder, "programs"))+'/'

if __name__ == "__main__":
    app.run("0.0.0.0", 3141, threaded=True)
