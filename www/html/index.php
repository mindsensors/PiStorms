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
  <title>Dashboard | PiStorms Web Interface</title>
  <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
  <link rel="stylesheet" href="assets/bootstrap.min.css">  <!-- Font Awesome -->
  <link rel="stylesheet" href="assets/font-awesome.min.css">
  <link rel="stylesheet" href="assets/AdminLTE.min.css">
  <link rel="stylesheet" href="assets/pnotify.min.css">
  <link rel="stylesheet" href="assets/skin-red.min.css">
  <link rel="stylesheet" href="assets/slider.css">
  <style>
    .btn-settings {
        margin:5px;
    }

    #needs-update-tooltip {
        cursor: pointer;
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
              <h3 class="box-title">About Device</h3>
            </div>
            <div class="box-footer no-padding">
              <ul class="nav nav-stacked">
                <li><a>Device: <b><span class="device_id"><i class="fa fa-refresh fa-spin"></i>&nbsp;&nbsp;Fetching</span></b></a></li>
                <li><a>Software Version: <b><span class="software_version"><i class="fa fa-refresh fa-spin"></i>&nbsp;&nbsp;Fetching</span></b> <?php echo ($updates == "both" || $updates == "software") ? $needsupdate : ($updates == "loading" ? "" : $uptodate); ?></a></li>
                <li><a>Firmware Version: <b><span class="firmware_version"><i class="fa fa-refresh fa-spin"></i>&nbsp;&nbsp;Fetching</span></b> <?php echo ($updates == "both" || $updates == "hardware") ? $needsupdate : ($updates == "loading" ? "" : $uptodate); ?></a></li>
                <li><a>Hostname: <b><?php echo gethostname();?></b></a></li>
                <li><a>eth0: <b><span class="eth0_ip"><i class="fa fa-refresh fa-spin"></i>&nbsp;&nbsp;Fetching</span></b></a></li>
                <li><a>wlan0: <b><span class="wlan0_ip"><i class="fa fa-refresh fa-spin"></i>&nbsp;&nbsp;Fetching</span></b></a></li>
              </ul>
            </div>
          </div>
        </div>


        <div class="col-md-4 col-sm-6 col-xs-12">
          <div class="info-box bg-green" id="battery-box">
            <span class="info-box-icon"><i class="fa fa-battery-4 fa-rotate-270" id="battery-symbol"></i></span>

            <div class="info-box-content">
              <span class="info-box-text">Battery</span>
              <span class="info-box-number"><span class="battery_v"><i class="fa fa-refresh fa-spin"></i></span>&nbsp;&nbsp;V</span>

              <span class="progress-description" id="battery-text">
                Well Charged
              </span>
            </div>
          </div>
        </div>
        <div class="col-md-4 col-sm-6 col-xs-12">
          <div class="box box-danger">
            <div class="box-header with-border">
              <h3 class="box-title">System</h3>

              <div class="box-tools pull-right">
                <button type="button" class="btn btn-box-tool" data-widget="collapse"><i class="fa fa-minus"></i>
                </button>
              </div>
            </div>
            <div class="box-body text-center">
              <button type="button" id="shut_btn" class="btn btn-danger btn-flat btn-settings"><i class="fa fa-power-off" aria-hidden="true"></i>&nbsp;&nbsp;Shutdown</button> <button type="button" id="rebt_btn" class="btn btn-primary btn-flat btn-settings"><i class="fa fa-repeat" aria-hidden="true"></i>&nbsp;&nbsp;Reboot</button>
              <br>
              <button type="button" id="stop_br" class="btn btn-warning btn-flat btn-settings"><i class="fa fa-desktop" aria-hidden="true"></i>&nbsp;&nbsp;Stop Browser</button> <button type="button" id="start_br" class="btn btn-primary btn-flat btn-success"><i class="fa fa-desktop" aria-hidden="true"></i>&nbsp;&nbsp;Start Browser</button>
              <br>
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
<script>
$('[data-toggle="tooltip"]').tooltip();

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

$.get(api+"software", function(data){
    $(".software_version").html(data);
});

$.get(api+"device", function(data){
    $(".device_id").html(data);
});

$.get(api+"eth0", function(data){
    $(".eth0_ip").html(data);
});

$.get(api+"wlan0", function(data){
    $(".wlan0_ip").html(data);
});

function update_voltage() {
    $.get(api+"battery", function(data){
        $(".battery_v").html(data);
        update_battery_box(parseFloat(data));
    });
    setTimeout(update_voltage,3000);
}

var battery_status = {
    0: ["Critical","red"], // 6.5
    1: ["Very Low","yellow"], // 6.9
    2: ["Low","yellow"], // 7.3
    3: ["Normal","green"], // 7.7
    4: ["Well Charged","green"] // 8.1
}
function update_battery_box(volt) {
    var tier = Math.floor((volt - 6.5) / 0.4);
    tier = tier < 0 ? 0 : tier > 4 ? 4 : tier;
    for (var i = 0; i <= 4; i++) {
        $("#battery-box").removeClass("bg-" + battery_status[i][1]);
        $("#battery-symbol").removeClass("fa-battery-" + i);
    }
    $("#battery-text").html(battery_status[tier][0]);
    $("#battery-box").addClass("bg-" + battery_status[tier][1]);
    $("#battery-symbol").addClass("fa-battery-" + tier);
}
update_voltage();

function redirectShutdown() {window.location = "./shutdown.php";}
function redirectRestart() {window.location = "./reboot.php";}
$("#shut_btn").click(function(){
	$.get(api+"shutdown", function(data){});
	notify("Success","Shutdown Signal Sent","success");
	window.setTimeout(redirectShutdown, 1000);
});
$("#rebt_btn").click(function(){
	$.get(api+"reboot", function(data){});
	notify("Success","Restart Signal Sent","success");
	window.setTimeout(redirectRestart, 1000);
});
$("#stop_br").click(function(){$.get(api+"stopbrowser", function(data){});notify("Success","Signal to stop browser sent","success");});
$("#start_br").click(function(){$.get(api+"startbrowser", function(data){});notify("Success","Signal to start browser sent","success");});

$("#needs-update-tooltip").click(function() {
    window.open("https://github.com/mindsensors/PiStorms");
});
</script>

</body>
</html>
