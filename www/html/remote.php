<?php
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
# Date      Author      Comments
# June-2016 Roman       Initial development.
#

include "api/config.php";

if (!isset($_SESSION['logged_in']) || !$_SESSION['logged_in']) {
    header('Location: ./login.php');
}

$nf = false;
$software_v = "Unknown";
$file = fopen("/home/pi/PiStorms/.version", "r") or $nf = true;
if (!$nf) {
    $software_v = fread($file,filesize("/home/pi/PiStorms/.version"));
    fclose($file);
}

$versions = '{"update": "both"}';
$file = fopen("/var/tmp/ps_versions.json", "r") or $nf = true;
if (!$nf) {
    $versions = fread($file,filesize("/var/tmp/ps_versions.json"));
    fclose($file);
}
$updates = json_decode($versions, true)["update"];
$uptodate = '<span class="pull-right badge bg-green">Up-to-date</span>';
$needsupdate = '<span class="pull-right badge bg-red">Needs Update!</span>';
?><!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>PiStorms Web Interface</title>
  <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.6/css/bootstrap.min.css">  <!-- Font Awesome -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.5.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.3.3/css/AdminLTE.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/pnotify/3.0.0/pnotify.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.3.3/css/skins/skin-red.min.css">
  <link rel="stylesheet" href="./slider.css">
  <style>
    .btn-sq {
      width: 50px !important;
      height: 50px !important;
      font-size: 24px;
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
    <a href="../../index2.html" class="logo">
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
    include "nav.php";
  ?>

  <div class="content-wrapper">
    <section class="content">

      <div class="row">
        <div class="col-md-4 col-sm-6 col-xs-12">
          <div class="box box-danger">
            <div class="box-header">
              <h3 class="box-title">Control Motors</h3>
            </div>
            <div class="box-body">
                  <h4 style="height:150px" id="static"></h4>
            </div>
          </div>
        </div>
        
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
        
        <div class="col-md-4 col-sm-6 col-xs-12">
          <div class="box box-danger">
            <div class="box-header">
              <h3 class="box-title">Control LED #1</h3>
            </div>
            <div class="box-body">
                  <input id="red_c1" type="text" value="" class="slider form-control" data-slider-min="0" data-slider-max="255" data-slider-step="1" data-slider-value="127" data-slider-orientation="horizontal" data-slider-selection="before" data-slider-tooltip="show" data-slider-id="red">

                  <input id="green_c1" type="text" value="" class="slider form-control" data-slider-min="0" data-slider-max="255" data-slider-step="1" data-slider-value="127" data-slider-orientation="horizontal" data-slider-selection="before" data-slider-tooltip="show" data-slider-id="green">

                  <input id="blue_c1" type="text" value="" class="slider form-control" data-slider-min="0" data-slider-max="255" data-slider-step="1" data-slider-value="127" data-slider-orientation="horizontal" data-slider-selection="before" data-slider-tooltip="show" data-slider-id="blue">
                  
                  <div class="text-center"><button class="btn btn-flat btn-danger" style="margin-top:5px" onclick="led(1)">Go!</button></div>
            </div>
          </div>
        </div>
        
        <div class="col-md-4 col-sm-6 col-xs-12">
          <div class="box box-danger">
            <div class="box-header">
              <h3 class="box-title">Control LED #2</h3>
            </div>
            <div class="box-body">
                  <input id="red_c2" type="text" value="" class="slider form-control" data-slider-min="0" data-slider-max="255" data-slider-step="1" data-slider-value="127" data-slider-orientation="horizontal" data-slider-selection="before" data-slider-tooltip="show" data-slider-id="red">

                  <input id="green_c2" type="text" value="" class="slider form-control" data-slider-min="0" data-slider-max="255" data-slider-step="1" data-slider-value="127" data-slider-orientation="horizontal" data-slider-selection="before" data-slider-tooltip="show" data-slider-id="green">

                  <input id="blue_c2" type="text" value="" class="slider form-control" data-slider-min="0" data-slider-max="255" data-slider-step="1" data-slider-value="127" data-slider-orientation="horizontal" data-slider-selection="before" data-slider-tooltip="show" data-slider-id="blue">
                  
                  <div class="text-center"><button class="btn btn-flat btn-danger" style="margin-top:5px" onclick="led(2)">Go!</button></div>
            </div>
          </div>
        </div>
        
      </div>

    </section>
  </div>

  <footer class="main-footer">
    <div class="pull-right hidden-xs">
      <b>Software Version:</b> <?php echo $software_v; ?> / <b>Hardware Version:</b> <span class="firmware_version"><i class="fa fa-refresh fa-spin"></i> fetching</span>
    </div>
    <strong>PiStorms by <a href="http://mindsensors.com" target="_blank">mindsensors.com</a></strong>
  </footer>

</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.6/js/bootstrap.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.3.3/js/app.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pnotify/3.0.0/pnotify.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jQuery-slimScroll/1.3.8/jquery.slimscroll.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-slider/7.1.0/bootstrap-slider.min.js"></script>

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

$.get(api+"firmware", function(data){
    $(".firmware_version").html(data);
});


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

$("#shut_btn").click(function(){$.get(api+"shutdown", function(data){});notify("Success","Shutdown Signal Sent","success");});
$("#rebt_btn").click(function(){$.get(api+"reboot", function(data){});notify("Success","Restart Signal Sent","success");});
</script>

<script src="nipple.js"></script>
<script>
    var static = nipplejs.create({
        zone: document.getElementById('static'),
        mode: 'static',
        position: {left: '50%', top: '50%'},
        color: 'green'
    });
    
</script>

</body>
</html>
