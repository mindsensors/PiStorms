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
# May 2017     Seth Tenembaum  Remove login requirement
*/

include "api/config.php";

?><!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="theme-color" content="#DD4B39">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>Remote Control | PiStorms Web Interface</title>
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
    #static {
        height: 250px;
        width: 250px;
        display: inline-block;
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
              <h3 class="box-title">Control Motors <i class="fa fa-question-circle" style="margin-left: 5px;" data-toggle="tooltip" data-placement="bottom" data-html="true" title="On a PiStorms, please connect the right motor to BAM1 and the left motor to BAM2 socket.<br><br>On a PiStorms-GRX, connect the right servo BAS1 and the left servo to BBS1." aria-hidden="true"></i></h3>
            </div>
            <div class="box-body">
                <div id="static"></div>
            </div>
            <div class="box-footer text-center">
                <span style="margin-right: 16px;" data-toggle="tooltip" title="Only applicable on the PiStorms, not the PiStorms-GRX">Stopping Action:</span><input type="checkbox" checked data-toggle="toggle" data-size="small" data-onstyle="primary" data-offstyle="danger" data-width="70" data-on="Float" data-off="Brake" id="stopcheck">
            </div>
          </div>
        </div>

        <div class="col-md-4 col-sm-6 col-xs-12">
          <div class="box box-danger">
            <div class="box-header">
              <h3 class="box-title">Bank A LED</h3>
            </div>
            <div class="box-body">
              <input id="red1" type="text" value="" class="slider form-control" data-slider-min="0" data-slider-max="255" data-slider-step="1" data-slider-value="127" data-slider-orientation="horizontal" data-slider-selection="before" data-slider-tooltip="show" data-slider-id="red">
              <input id="green1" type="text" value="" class="slider form-control" data-slider-min="0" data-slider-max="255" data-slider-step="1" data-slider-value="127" data-slider-orientation="horizontal" data-slider-selection="before" data-slider-tooltip="show" data-slider-id="green">
              <input id="blue1" type="text" value="" class="slider form-control" data-slider-min="0" data-slider-max="255" data-slider-step="1" data-slider-value="127" data-slider-orientation="horizontal" data-slider-selection="before" data-slider-tooltip="show" data-slider-id="blue">
              <div class="form-group">
                <input type="text" id="color1" class="form-control demo" value="#7F7F7F">
              </div>
              <div class="text-center">
                <button class="btn btn-flat btn-danger" style="margin-top:5px" onclick="led(1)">Go!</button>
              </div>
            </div>
          </div>
        </div>

        <div class="col-md-4 col-sm-6 col-xs-12">
          <div class="box box-danger">
            <div class="box-header">
              <h3 class="box-title">Bank B LED</h3>
            </div>
            <div class="box-body">
              <input id="red2" type="text" value="" class="slider form-control" data-slider-min="0" data-slider-max="255" data-slider-step="1" data-slider-value="127" data-slider-orientation="horizontal" data-slider-selection="before" data-slider-tooltip="show" data-slider-id="red">
              <input id="green2" type="text" value="" class="slider form-control" data-slider-min="0" data-slider-max="255" data-slider-step="1" data-slider-value="127" data-slider-orientation="horizontal" data-slider-selection="before" data-slider-tooltip="show" data-slider-id="green">
              <input id="blue2" type="text" value="" class="slider form-control" data-slider-min="0" data-slider-max="255" data-slider-step="1" data-slider-value="127" data-slider-orientation="horizontal" data-slider-selection="before" data-slider-tooltip="show" data-slider-id="blue">
              <div class="form-group">
                <input type="text" id="color2" class="form-control demo" value="#7F7F7F">
              </div>
              <div class="text-center">
                <button class="btn btn-flat btn-danger" style="margin-top:5px" onclick="led(2)">Go!</button>
              </div>
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
    $.post(api+'led', {
        led: n,
        red: $('#red'+n).val(),
        blue: $('#blue'+n).val(),
        green: $('#green'+n).val()
    });
}

$('#red1').slider();
$('#blue1').slider();
$('#green1').slider();
$('#red2').slider();
$('#blue2').slider();
$('#green2').slider();

$('#color1').minicolors({theme: 'bootstrap'});
$('#color2').minicolors({theme: 'bootstrap'});

$('#red1').change(update_slider_1);
$('#blue1').change(update_slider_1);
$('#green1').change(update_slider_1);

$('#red2').change(update_slider_2);
$('#blue2').change(update_slider_2);
$('#green2').change(update_slider_2);

function update_slider_1() {
    var hex = rgbToHex($('#red1').slider('getValue'), $('#green1').slider('getValue'), $('#blue1').slider('getValue'));
    $('#color1').minicolors('value', hex);
}

function update_slider_2() {
    var hex = rgbToHex($('#red2').slider('getValue'), $('#green2').slider('getValue'), $('#blue2').slider('getValue'));
    $('#color2').minicolors('value', hex);
}

// http://stackoverflow.com/a/5624139/3600428
function rgbToHex(r, g, b) {
    function componentToHex(c) {
        var hex = c.toString(16);
        return hex.length == 1 ? '0' + hex : hex;
    }
    return '#' + componentToHex(r) + componentToHex(g) + componentToHex(b);
}
</script>

<script src="./assets/nipple.js"></script>
<script>
    var manager = nipplejs.create({
        zone: document.getElementById('static'),
        mode: 'static',
        position: {left: '50%', top: '50%'},
        color: 'green',
        size: 128
    });

    var lastMoveTime = new Date().getTime();
    //var watchdog = null;
    manager.on('move', function (evt, data) {
        if (new Date().getTime()-lastMoveTime > 300) {
            lastMoveTime = new Date().getTime();
            //if (watchdog) clearTimeout(watchdog);
            //watchdog = setTimeout($.get.bind(null, api+'brakemotors'), 1000);

            var d = data.angle.radian;
            var l = Math.sin(d + Math.PI/4) / Math.sin(Math.PI/4);
            var r = Math.sin(d - Math.PI/4) / Math.sin(Math.PI/4);
            if (Math.abs(l) > 1) l = Math.sign(l);
            if (Math.abs(r) > 1) r = Math.sign(r);
            var f = Math.min(data.force, 1);
            l = Math.round(l*f*100);
            r = Math.round(r*f*100);
            $.post(api+"setmotorspeed", {right: r, left: l});
        }
    });

    manager.on('end', function(evt, data) {
        if ($('#stopcheck').is(':checked'))
            $.get(api+'floatmotors');
        else
            $.get(api+'brakemotors');
    });
</script>

</body>
</html>
