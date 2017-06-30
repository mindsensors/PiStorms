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
  <title>Screenshots | PiStorms Web Interface</title>
  <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
  <link rel="stylesheet" href="assets/bootstrap.min.css">  <!-- Font Awesome -->
  <link rel="stylesheet" href="assets/font-awesome.min.css">
  <link rel="stylesheet" href="assets/AdminLTE.min.css">
  <link rel="stylesheet" href="assets/pnotify.min.css">
  <link rel="stylesheet" href="assets/skin-red.min.css">
  <link rel="stylesheet" href="assets/slider.css">
  <link href="assets/bootstrap-toggle.min.css" rel="stylesheet">
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
        <div class="col-xs-12">
          <div class="box box-danger">
            <div class="box-header">
              <h3 class="box-title">Take Screenshots</h3>
            </div>
            <div class="box-body">
               <button id="srwb" style="margin:5px" class="btn btn-flat btn-danger"><i class="fa fa-play"></i>&nbsp;&nbsp;Start Recording Screenshots</button>
               <button id="stpr" style="margin:5px" class="btn btn-flat btn-danger"><i class="fa fa-stop"></i>&nbsp;&nbsp;Stop Recording Screenshots</button>
               <button id="clar" style="margin:5px" class="btn btn-flat btn-warning"><i class="fa fa-ban"></i>&nbsp;&nbsp;Clear Screenshots</button>
               <!--<br>
               <button id="srwbt" style="margin:5px" class="btn btn-flat btn-success"><i class="fa fa-play"></i>&nbsp;&nbsp;Start Recording Touch Locations</button>
               <button id="stprt" style="margin:5px" class="btn btn-flat btn-success"><i class="fa fa-stop"></i>&nbsp;&nbsp;Stop Recording Touch Locations</button>-->
               <br>
               <div id="touchdiv" style="margin:5px;display:none"><b>Record Touch Locations:</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="checkbox" checked data-toggle="toggle" data-size="small" data-onstyle="success" data-offstyle="danger" data-width="70" data-on="ON" data-off="OFF" id="touchrecord"></div>
            </div>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col-xs-12">
          <div class="box box-danger">
            <div class="box-header">
              <h3 class="box-title">Screenshots</h3>
            </div>
            <div class="box-body">
               <div class="row" id="imagesList">
               <?php
                 include "api/imagedata.php";
               ?>
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

$.get(api+"firmware", function(data){
    $(".firmware_version").html(data);
});

var last="";
function update_pictures() {
    $.get("api/imagedata.php", function(data){
        if (last != data) {
            $("#imagesList").html(data);
            last = data;
        }
    });
    setTimeout(update_pictures,1500);
}

update_pictures();

function refreshtoggle() {
    $.get(api+"readrecordingtouch", function(data){
        if (!($("#touchrecord").is(':checked') && data == '1' || !$("#touchrecord").is(':checked') && data != '1')) {
            $('#touchrecord').bootstrapToggle(data == '1' ? 'on' : 'off');
        }
    });
}
function seteventtouggle() {
    $('#touchrecord').change(function() {
        $.get(api+ ($("#touchrecord").is(':checked') ? "starttouchrecording" : "stoptouchrecording"), function(data){notify("Success",($("#touchrecord").is(':checked') ? "Started" : "Stopped") + " recording touch locations","success");});
    });
}

$("#srwb").click(function(){$.get(api+"startrecording/withBg", function(data){refreshtoggle();$("#touchdiv").fadeIn();notify("Success","Started taking screenshots","success");});});
$("#stpr").click(function(){
    $.get(api+"stoprecording", function(data){
        $("#touchdiv").fadeOut();
        notify("Success","Stopped taking screenshots","success");
    });
    $.get(api+"stoptouchrecording", function(data){});
    if ($("#touchrecord").is(':checked')) {
        $('#touchrecord').bootstrapToggle('off');
    }
});
var orig = null;
refreshtoggle();
$.get(api+"readrecording", function(data){if(data == '1'){$("#touchdiv").fadeIn();}orig=data;seteventtouggle();});

$("#clar").click(function(){
    if (confirm("Are you sure you want to permanently remove all screenshots?")) {
        $.get(api+"clearimages", function(data){notify("Result","Images cleared","success");});
    }
});
</script>
</body>
</html>
