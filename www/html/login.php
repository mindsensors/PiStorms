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

if (isset($_SESSION['logged_in']) && $_SESSION['logged_in']) {
    header('Location: ./');
}

?><!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>PiStorms Login</title>
  <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.6/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.5.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/admin-lte/2.3.3/css/AdminLTE.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/pnotify/3.0.0/pnotify.min.css">
  <link rel="icon" href="./favicon.ico" type="image/x-icon"/>

  <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
  <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
  <!--[if lt IE 9]>
  <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
  <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
  <![endif]-->
</head>
<body class="hold-transition login-page">
<div class="login-box">
  <div class="login-logo">
    <b>PiStorms Web</b><br><?php echo gethostname(); ?>
  </div>
  <div class="login-box-body">
    <p class="login-box-msg">Enter the passcode&nbsp;&nbsp;<span href="#" data-toggle="tooltip" title="You can find or reset the passcode using the WebKey script in utils folder"><i class="fa fa-question-circle" aria-hidden="true"></i></span></p>
    <form action="javascript:login()" method="post">
      <div class="form-group has-feedback">
        <input id="pass" type="password" class="form-control" placeholder="Passcode" required>
        <span class="fa fa-key form-control-feedback"></span>
      </div>
      <div class="text-center">
        <button type="submit" class="btn btn-danger btn-flat">Log In</button>
      </div>
    </form>
    

  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.6/js/bootstrap.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pnotify/3.0.0/pnotify.min.js"></script>
<script>
$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip(); 
});

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

function login() {
    $.post("api/login.php", {pass: $("#pass").val()}, function(data){
        console.log(data);
        if (data.charAt(0) == "1") {
            notify("Success!", "Login successfull!", "success");
            window.location.href = "./";
        } else if (data.charAt(0) == "3") {
            notify("Logged in", "Passcode not set.", "warning");
            window.location.href = "./";
        } else {
            notify("Error!", "Invalid passcode.", "error");
        }
    });
}

</script>
</body>
</html>
