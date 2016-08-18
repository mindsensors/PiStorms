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
    exit();
}

?><!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="theme-color" content="#DD4B39">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>PiStorms Web Interface</title>
  <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
  <link rel="stylesheet" href="assets/bootstrap.min.css">  <!-- Font Awesome -->
  <link rel="stylesheet" href="assets/font-awesome.min.css">
  <link rel="stylesheet" href="assets/AdminLTE.min.css">
  <link rel="stylesheet" href="assets/pnotify.min.css">
  <link rel="stylesheet" href="assets/skin-red.min.css">
  <link rel="stylesheet" href="assets/jquery.minicolors.css">
  <link rel="stylesheet" href="assets/slider.css">
  <link href="assets/bootstrap-toggle.min.css" rel="stylesheet">
  <style>
    .btn-sq {
      width: 50px !important;
      height: 50px !important;
      font-size: 24px;
    }
    .btn-settings {
        margin: 5px;
    }
    .front {
        background: url(assets/top.png) !important;
        background-size: contain !important;
        opacity: 1 !important;
        z-score: 100 !important;
        height: 85% !important;
        width: 85% !important;
        margin-left: -54.4px !important;
        margin-top: -54.4px !important;
    }
    .back {
        background: url(assets/bottom.png) !important;
        background-size: contain !important;
        opacity: 1 !important;
        z-score: 100 !important;
    }
    .nipple {
        opacity: 1 !important;
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
        
        <div class="col-md-4 col-sm-6 col-xs-12">
          <div class="box box-danger">
            <div class="box-header">
              <h3 class="box-title"><span data-toggle="tooltip" title="Please connect the right motor to BANK A M1 socket and the left motor to BANK A M2 socket" aria-hidden="true">Control Motors&nbsp;&nbsp;<i class="fa fa-question-circle"></i></span></h3>
            </div>
            <div class="box-body">
                <div style="height:250px; vertical-align:middle;text-align: center" class="text-center"><div style="height:250px;width:250px;display:inline-block" id="static"></div></div>
            </div>
            <div class="box-footer text-center">
                Stopping Action:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="checkbox" checked data-toggle="toggle" data-size="small" data-onstyle="primary" data-offstyle="danger" data-width="70" data-on="Float" data-off="Brake" id="stopcheck">
                <!--<button type="button" id="brake_btn" class="btn btn-danger btn-flat btn-settings"><i class="fa fa-stop" aria-hidden="true"></i>&nbsp;&nbsp;Brake</button>
                <button type="button" id="float_btn" class="btn btn-danger btn-flat btn-settings"><i class="fa fa-pause" aria-hidden="true"></i>&nbsp;&nbsp;Float</button>-->
            </div>
          </div>
        </div>
        <!--
        <div class="col-md-4 col-sm-6 col-xs-12">
          <div class="box box-danger">
            <div class="box-header">
              <h3 class="box-title">Control Motors</h3>
            </div>
            <div class="box-body">
                <div class="row">
                    <div class="col-xs-12 text-center"><button class="btn btn-success btn-flat btn-square btn-sq"><i class="fa fa-arrow-up" aria-hidden="true"></i></button></div>
                    <div class="col-xs-12 text-center"><button class="btn btn-success btn-flat btn-square btn-sq"><i class="fa fa-arrow-left" aria-hidden="true"></i></button><button class="btn btn-danger btn-flat btn-square btn-sq"><i class="fa fa-stop-circle-o" aria-hidden="true"></i></button><button class="btn btn-success btn-flat btn-square btn-sq"><i class="fa fa-arrow-right" aria-hidden="true"></i></button></div>
                    <div class="col-xs-12 text-center"><button class="btn btn-success btn-flat btn-square btn-sq"><i class="fa fa-arrow-down" aria-hidden="true"></i></button></div>
                </div>
            </div>
          </div>
        </div>
        -->
        <div class="col-md-4 col-sm-6 col-xs-12">
          <div class="box box-danger">
            <div class="box-header">
              <h3 class="box-title">Bank A LED</h3>
            </div>
            <div class="box-body">
                  <input id="red_c1" type="text" value="" class="slider form-control" data-slider-min="0" data-slider-max="255" data-slider-step="1" data-slider-value="127" data-slider-orientation="horizontal" data-slider-selection="before" data-slider-tooltip="show" data-slider-id="red">

                  <input id="green_c1" type="text" value="" class="slider form-control" data-slider-min="0" data-slider-max="255" data-slider-step="1" data-slider-value="127" data-slider-orientation="horizontal" data-slider-selection="before" data-slider-tooltip="show" data-slider-id="green">

                  <input id="blue_c1" type="text" value="" class="slider form-control" data-slider-min="0" data-slider-max="255" data-slider-step="1" data-slider-value="127" data-slider-orientation="horizontal" data-slider-selection="before" data-slider-tooltip="show" data-slider-id="blue">
                  
                  <div class="form-group">
                    <input type="text" id="color1" class="form-control demo" value="#7F7F7F">
                  </div>
                  <div class="text-center"><button class="btn btn-flat btn-danger" style="margin-top:5px" onclick="led(1)">Go!</button></div>
            </div>
          </div>
        </div>
        
        <div class="col-md-4 col-sm-6 col-xs-12">
          <div class="box box-danger">
            <div class="box-header">
              <h3 class="box-title">Bank B LED</h3>
            </div>
            <div class="box-body">
                  <input id="red_c2" type="text" value="" class="slider form-control" data-slider-min="0" data-slider-max="255" data-slider-step="1" data-slider-value="127" data-slider-orientation="horizontal" data-slider-selection="before" data-slider-tooltip="show" data-slider-id="red">

                  <input id="green_c2" type="text" value="" class="slider form-control" data-slider-min="0" data-slider-max="255" data-slider-step="1" data-slider-value="127" data-slider-orientation="horizontal" data-slider-selection="before" data-slider-tooltip="show" data-slider-id="green">

                  <input id="blue_c2" type="text" value="" class="slider form-control" data-slider-min="0" data-slider-max="255" data-slider-step="1" data-slider-value="127" data-slider-orientation="horizontal" data-slider-selection="before" data-slider-tooltip="show" data-slider-id="blue">
                  
                  <div class="form-group">
                    <input type="text" id="color2" class="form-control demo" value="#7F7F7F">
                  </div>
                  
                  <div class="text-center"><button class="btn btn-flat btn-danger" style="margin-top:5px" onclick="led(2)">Go!</button></div>
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
<script type="text/javascript" src="assets/jquery.minicolors.min.js"></script>
<script src="assets/bootstrap-toggle.min.js"></script>

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

function led(n) {
    $.post(api+"led", {led: n,red: $("#red_c"+n).val(),blue: $("#blue_c"+n).val(),green: $("#green_c"+n).val()}, function(data){
        console.log(data);
    });
}

$('#red_c1').slider({});
$('#blue_c1').slider({});
$('#green_c1').slider({});
$('#red_c2').slider({});
$('#blue_c2').slider({});
$('#green_c2').slider({});

function update_slider_1() {
    var hex = rgbToHex($('#red_c1').slider('getValue'), $('#green_c1').slider('getValue'), $('#blue_c1').slider('getValue'));    
    $('#color1').minicolors('value', hex);
}

function update_slider_2() {
    var hex = rgbToHex($('#red_c2').slider('getValue'), $('#green_c2').slider('getValue'), $('#blue_c2').slider('getValue'));    
    $('#color2').minicolors('value', hex);
}

$('#red_c1').change(function() {update_slider_1();});
$('#blue_c1').change(function() {update_slider_1();});
$('#green_c1').change(function() {update_slider_1();});

$('#red_c2').change(function() {update_slider_2();});
$('#blue_c2').change(function() {update_slider_2();});
$('#green_c2').change(function() {update_slider_2();});

$("#brake_btn").click(function(){$.get(api+"brakemotors", function(data){});});
$("#float_btn").click(function(){$.get(api+"floatmotors", function(data){});});

// http://stackoverflow.com/a/5624139/3600428
function componentToHex(c) {
    var hex = c.toString(16);
    return hex.length == 1 ? "0" + hex : hex;
}
function rgbToHex(r, g, b) {
    return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
}
function hexToRgb(hex) {
    var shorthandRegex = /^#?([a-f\d])([a-f\d])([a-f\d])$/i;
    hex = hex.replace(shorthandRegex, function(m, r, g, b) {
        return r + r + g + g + b + b;
    });
    var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16)
    } : null;
}


$('#color1').minicolors({
  theme: 'bootstrap',
  change: function(hex) {
    if(!hex) return;
    var rgb = hexToRgb(hex);
    $("#red_c1").slider('setValue', rgb.r);
    $("#blue_c1").slider('setValue', rgb.b);
    $("#green_c1").slider('setValue', rgb.g);
  }
});

$('#color2').minicolors({
  theme: 'bootstrap',
  change: function(hex) {
    if(!hex) return;
    var rgb = hexToRgb(hex);
    $("#red_c2").slider('setValue', rgb.r);
    $("#blue_c2").slider('setValue', rgb.b);
    $("#green_c2").slider('setValue', rgb.g);
  }
});
</script>

<script src="./assets/nipple.js"></script>
<script>
    
    function n(minObserver,maxObserved,minNeeded,maxNeeded,value) {
        return (maxNeeded-minNeeded)/(maxObserved)*(value-maxObserved)+maxNeeded;
    }
    
    var manager = nipplejs.create({
        zone: document.getElementById('static'),
        mode: 'static',
        position: {left: '50%', top: '50%'},
        color: 'green',
        size: 128,
        catchDistance: 10
    });
    
    var movecnt = 0;
    
    var lt = 0;
    manager.on('move dir start end', function (evt, data) {
      var r = 0;
      var l = 0;
      if (data.distance) {
        var d = data.angle.degree;
        //console.log(d + " " + data.distance);
        if (d >= 0 && d < 90) {
            var rm = n(0,90,-127,127,d);
            var lm = 127;
            r = rm / 64 * data.distance;
            l = lm / 64 * data.distance;
        } else if (d >= 90 && d < 180) {
            var rm = 127;
            var lm = n(0,90,127,-127,d-90);
            r = rm / 64 * data.distance;
            l = lm / 64 * data.distance;
        } else if (d >= 180 && d < 270) {
            var rm = -127;
            var lm = d < 225 ? n(0,45,-127,0,d-180) : n(0,45,0,-127,d-225);
            r = rm / 64 * data.distance;
            l = lm / 64 * data.distance;
        } else {
            var rm = d < 315 ? n(0,45,-127,0,d-270) : n(0,45,0,-127,d-315);
            var lm = -127;
            r = rm / 64 * data.distance;
            l = lm / 64 * data.distance;
        }
      }
      if (movecnt > 1 && (new Date().getTime() / 1000 - lt > 0.3 || evt.type == "end") && evt.type != "start") {
        if (evt.type != "end") {
            $.post(api+"setmotorspeed", {right: Math.round(r), left: Math.round(l), stop: $("#stopcheck").is(':checked') ? "float" : "brake"}, function(result) {
              //console.log(r + " " + l);
            });
        } else {
            $.get(api+ ($("#stopcheck").is(':checked') ? "floatmotors" : "brakemotors"), function(data){});
            $.get(api+ ($("#stopcheck").is(':checked') ? "floatmotors" : "brakemotors"), function(data){});
            $.get(api+ ($("#stopcheck").is(':checked') ? "floatmotors" : "brakemotors"), function(data){});
        }
        if (evt.type != "start") {
          lt = new Date().getTime() / 1000;
        }
      }
      if (evt.type == "end") {
        movecnt = 0;
      }
      if (evt.type == "move") {
          movecnt ++;
      }
    });

</script>

</body>
</html>
