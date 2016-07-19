<?php
/*
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
# Date         Author          Comments
# July 2016    Roman Bohuk     Initial Authoring 
*/

include "api/config.php";

if (!isset($_SESSION['logged_in']) || !$_SESSION['logged_in']) {
    header('Location: ./login.php');
}


?><!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>PiStorms Web Interface</title>
  <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
  <link rel="stylesheet" href="assets/bootstrap.min.css">  <!-- Font Awesome -->
  <link rel="stylesheet" href="assets/font-awesome.min.css">
  <link rel="stylesheet" href="assets/AdminLTE.min.css">
  <link rel="stylesheet" href="assets/pnotify.min.css">
  <link rel="stylesheet" href="assets/skin-red.min.css">
  <link rel="stylesheet" href="assets/slider.css">
  <style>
    .btn-sq {
      width: 50px !important;
      height: 50px !important;
      font-size: 24px;
    }
  </style>
  <style type="text/css" media="screen">
    #editor { 
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        height: 600px;
    }
    td {
        vertical-align: middle !important;
    }
</style>
  <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
  <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
  <!--[if lt IE 9]>
  <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
  <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
  <![endif]-->
</head>
<body class="hold-transition skin-red sidebar-mini">
<div class="wrapper">
  <header class="main-header">
    <a href="./" class="logo">
      <span class="logo-mini"><b>PS</b></span>
      <span class="logo-lg"><b>PiStorms</b> Web</span>
    </a>
    <nav class="navbar navbar-static-top">
      <a href="#" class="sidebar-toggle" data-toggle="offcanvas" role="button">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </a>

      <div class="navbar-custom-menu">
        <ul class="nav navbar-nav">
          <li>
            <a href="./logout.php">Logout&nbsp;&nbsp;<i class="fa fa-sign-out"></i></a>
          </li>
        </ul>
      </div>
    </nav>
  </header>

  <?php
    include_once("./components/nav.php");
  ?>

  <div class="content-wrapper">
  
    <section class="content">
      <div class="row">
        <div class="col-md-6 col-lg-4">
          <div class="box box-danger">
            <div class="box-header">
              <h3 class="box-title">Your Programs</h3>
            </div>
            <div class="box-body" id="programs_list">
              <div class="text-center"><h4><i class="fa fa-refresh fa-spin"></i>&nbsp;&nbsp;Fetching</h4></div>
            </div>
          </div>
        </div>
        
        <div class="col-md-6 col-lg-8">
          <div class="box box-danger">
            <div class="box-header">
              <h3 class="box-title">Edit Code</h3>
            </div>
            <div class="box-body">

            </div>
          </div>
        </div>
        
        <div class="col-md-6 col-lg-8">
          <div class="box">
            <div class="box-body" style="height:600px">
               <div id="editor">#!/usr/bin/env python
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
# Date         Author          Comments
# July 2016    Roman Bohuk     Initial Authoring 

from datetime import timedelta  
from flask import Flask, make_response, request, current_app  
from functools import update_wrapper
import os

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
with open(message_file, "r") as data_file:
    message_text = data_file.read()
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
    with open(os.path.join(home_folder, ".version"), "r") as f:
        return f.read()

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
    os.system("sudo psm_shutdown -r now")
    return "1"

@app.route("/shutdown", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def shutdown():
    os.system("sudo psm_shutdown -h now")
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
            print led, red, blue, green
            psc.led(int(led),red,green,blue)
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

@app.route("/readrecording", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def readrecording():
    v = disp.readRecordingCount()
    if v == "" or len(v) != 2 or (v[0] != "-" and not v[0].isdigit()): return "Not recording"
    out = ""
    if v[0] == "-": out = "Recording frames indefinitely"
    else: out = "Recording " + v[0] + " frames more"
    
    if v[1] == "1": out += " with the background image"
    else: out += " without the background image"
    
    return out

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
    print "Start Checking"
    ps = os.popen('ps -ef').read().split("\n")
    for i in ps:
        print "__"+i
        if "MSBrowser.py" in i:
            print "End Checking Y"
            return "1"
    print "End Checking"
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

@app.route("/calibrate", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def calibrate():
    stopbrowser()
    os.system("python " + os.path.join(home_folder, "01-Calibrate.py"))
    return "1"
    
@app.route("/getapacheerrors", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def getapacheerrors():
    return os.popen('tail /var/log/apache2/error.log -n 25').read()

@app.route("/getmessage", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def getmessage():
    return messages["message"]

@app.route("/markmessageread", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def markmessageread():
    messages["status"] = "Read"
    f = open(message_file, 'w+')
    json.dump(messages, f)
    f.close()
    return "1"

@app.route("/getmessagejson", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
def getmessagejson():
    return message_text

if __name__ == "__main__":
    app.run("0.0.0.0", 3141, threaded=True)</div>
            </div>
          </div>
        </div>
        
      </div>

    </section>
  </div>

<?php include_once("./components/footer.php"); ?>

</div>

<script src="assets/jquery.min.js"></script>
<script src="assets/bootstrap.min.js"></script>
<script type="text/javascript" src="assets/app.min.js"></script>
<script type="text/javascript" src="assets/pnotify.min.js"></script>
<script type="text/javascript" src="assets/jquery.slimscroll.min.js"></script>
<script type="text/javascript" src="assets/bootstrap-slider.min.js"></script>

<script src="assets/ace/ace.js"></script>
<script>
    var editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.getSession().setMode("ace/mode/python");
</script>
<script>
PNotify.prototype.options.styling = "bootstrap3";
PNotify.prototype.options.delay = 3000;

function notify(tt,tx,tp) {
    new PNotify({
        title: tt,
        text: tx,
        type: tp,
        icon: false
    });
}

var api = "http://<?=$_SERVER['SERVER_NAME']?>:3141/";

var tbl = '<table class="table table-striped">\
                <tr>\
                  <th class="text-center">Type</th>\
                  <th class="text-center">Name</th>\
                  <th class="text-center">Actions</th>\
                </tr>';

var row = '<tr>\
                  <td class="text-center"><img src="assets/&&ft&&.png" alt="object" style="height:40px"></img></td>\
                  <td class="text-center"><b>&&fn&&</b></td>\
                  <td class="text-center"><button class="btn btn-flat btn-success btn-sm"><i class="fa fa-pencil-square-o" aria-hidden="true"></i></button><button class="btn btn-flat btn-danger btn-sm"><i class="fa fa-trash" aria-hidden="true"></i></button></td>\
                </tr>';
                
$.get(api + "getprograms", function(data){
    data = $.parseJSON(data);
    table = tbl;
    for (var i = 0; i < data.length; i++) {
        table += row.replace("&&ft&&", data[i][2] == "py" ? "python" : "folder").replace("&&fn&&",data[i][0]);
    }
    table += "</table>";
    $("#programs_list").html(table);
    $("#programs_list").addClass("no-padding");
});


$("#srwb").click(function(){$.get(api+"startrecording/withBg", function(data){});notify("Success","Started taking frames with background","success");});
$("#stpr").click(function(){$.get(api+"stoprecording", function(data){});notify("Success","Stopped recording","success");});
$("#chkr").click(function(){$.get(api+"readrecording", function(data){notify("Result",data,"success");});});
$("#clar").click(function(){
    if (confirm("Are you sure you want to permanently remove all screenshots?")) {
        $.get(api+"clearimages", function(data){notify("Result","Images cleared","success");});
    }
});
</script>

</body>
</html>