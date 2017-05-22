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
  <title>Logs | PiStorms Web Interface</title>
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
      <h2 class="page-header"><i class="fa fa-file-text-o"></i>&nbsp;&nbsp;PiStorms Logs</h2>
      <div class="row">
        <div class="col-md-12">
          <div class="nav-tabs-custom">
            <ul class="nav nav-tabs">
              <li class="active" data-toggle="tooltip" data-trigger="hover" data-html="true" title="Your general program output (print statements) will also appear here.<br><br>Written to /var/tmp/psmb.out from /usr/local/bin/MSBrowser.py"><a href="#tab_1" data-toggle="tab">Mindsensors Browser</a></li>
              <li data-toggle="tooltip" data-trigger="hover" title="Written to /var/tmp/psmd.out from /usr/local/bin/MSDriver.py"><a href="#tab_2" data-toggle="tab">MSDriver</a></li>
              <li data-toggle="tooltip" data-trigger="hover" title="Written to /var/tmp/sws.out by /usr/local/bin/swarmserver"><a href="#tab_3" data-toggle="tab">Swarm server</a></li>
              <li data-toggle="tooltip" data-trigger="hover" title="Written to /var/tmp/webapi.out from /var/www/web_api/MSWeb.py"><a href="#tab_4" data-toggle="tab">MSWeb</a></li>
              <li data-toggle="tooltip" data-trigger="hover" data-html="true" title="Only the last 25 lines are displayed.<br><br>Written to /var/log/apache2/error.log by /usr/sbin/apache2"><a href="#tab_5" data-toggle="tab">Apache</a></li>
              <li><a href="javascript:window.scrollTo(0,document.body.scrollHeight);">Scroll to the Bottom</a></li>
            </ul>
            <div class="tab-content">
              <div class="tab-pane active" id="tab_1">
                <pre><?php
                    $data = '[empty]';
                    $nf = false;
                    $file = fopen("/var/tmp/psmb.out", "r") || $nf = true;
                    $filesize = filesize("/var/tmp/psmb.out");
                    if (!$nf && $filesize > 0) {
                        $data = fread($file, filesize("/var/tmp/psmb.out"));
                        fclose($file);
                    }
                    if (strlen($data) == 0) {
                        $data = "[empty]";
                    }
                    echo $data;
                ?></pre>
              </div>
              <div class="tab-pane" id="tab_2">
                <pre><?php
                    $data = '[empty]';
                    $nf = false;
                    $file = fopen("/var/tmp/psmb.out", "r") || $nf = true;
                    $filesize = filesize("/var/tmp/sws.out");
                    if (!$nf && $filesize > 0) {
                        $data = fread($file, filesize("/var/tmp/sws.out"));
                        fclose($file);
                    }
                    if (strlen($data) == 0) {
                        $data = "[empty]";
                    }
                    echo $data;
                ?></pre>
              </div>
              <div class="tab-pane" id="tab_3">
                <pre><?php
                    $data = '[empty]';
                    $nf = false;
                    $file = fopen("/var/tmp/psmb.out", "r") || $nf = true;
                    $filesize = filesize("/var/tmp/sws.out");
                    if (!$nf && $filesize > 0) {
                        $data = fread($file, filesize("/var/tmp/sws.out"));
                        fclose($file);
                    }
                    if (strlen($data) == 0) {
                        $data = "[empty]";
                    }
                    echo $data;
                ?></pre>
              </div>
              <div class="tab-pane" id="tab_4">
                <pre><?php
                    $data = '[empty]';
                    $nf = false;
                    $file = fopen("/var/tmp/webapi.out", "r") || $nf = true;
                    $filesize = filesize("/var/tmp/sws.out");
                    if (!$nf && $filesize > 0) {
                        $data = fread($file, filesize("/var/tmp/sws.out"));
                        fclose($file);
                    }
                    if (strlen($data) == 0) {
                        $data = "[empty]";
                    }
                    echo $data;
                ?></pre>
              </div>
              <div class="tab-pane" id="tab_5">
                <pre id="apacheerros">[empty]</pre>
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

$.get(api+"getapacheerrors", function(data){
    $("#apacheerros").html(data || "[empty]");
});

</script>

</body>
</html>
