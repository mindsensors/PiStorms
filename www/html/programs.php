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
    
    @media (max-width: 600px) {
        .editor-row {
            padding-right:30px;
        }
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
              <div class="box-tools pull-right">
                <button type="button" class="btn btn-sm btn-flat btn-success"><i class="fa fa-plus"></i>&nbsp;&nbsp;File</button>
                <button type="button" class="btn btn-sm btn-flat btn-primary"><i class="fa fa-plus"></i>&nbsp;&nbsp;Folder</button>
              </div>
            </div>
            <div class="box-body" id="programs_list">
              <div class="text-center"><h4><i class="fa fa-refresh fa-spin"></i>&nbsp;&nbsp;Fetching</h4></div>
            </div>
          </div>
        </div>
        
        <div class="col-md-6 col-lg-8">
          <div class="box box-danger" style="margin-bottom:0px !important;padding-bottom:0px !important;">
            <div class="box-body" id="edit_options">
                Please select a program on the left or create a new file
            </div>
          </div>
        </div>
        <div class="col-md-6 col-lg-8 editor-row" style="display:none">
          <div class="box">
            <div class="box-body" style="height:630px;">
               <div id="editor"># Please select a program to edit</div>
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
    editor.setOptions({
       autoScrollEditorIntoView: true 
    });
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
                  <td class="text-center"><button onclick="edit(\'&&fn&&\',\'&&fl&&\')" style="width:35px;" class="btn btn-flat btn-success btn-sm"><i class="fa fa-pencil-square-o" aria-hidden="true"></i></button><button style="width:35px;" class="btn btn-flat btn-danger btn-sm"><i class="fa fa-trash" aria-hidden="true"></i></button></td>\
                </tr>';
                
$.get(api + "getprograms", function(data){
    data = $.parseJSON(data);
    table = tbl;
    for (var i = 0; i < data.length; i++) {
        table += row.replace("&&ft&&", data[i][2] == "py" ? "python" : "folder").split("&&fn&&").join(data[i][0]).replace("&&fl&&",data[i][1]);
    }
    table += "</table>";
    $("#programs_list").html(table);
    $("#programs_list").addClass("no-padding");
});

function edit(filename, location) {
    $.post(api+"fetchscript", {path: location}, function(result){
        editor.setValue(result);
        editor.gotoLine(1);
        $("#program_name").html("<b>" + filename + "</b>");
        $("#edit_options").html('<span style="font-size:20px;padding-bottom:0px;margin-bottom:-10px;display:block;">Edit <b>' + filename + '</b></span><br><button type="button" class="btn btn-success btn-flat btn-settings" onclick="save(\'' + location + '\')"><i class="fa fa-save" aria-hidden="true"></i>&nbsp;&nbsp;Save</button><!--<button type="button" class="btn btn-danger btn-flat btn-settings"><i class="fa fa-ban" aria-hidden="true"></i>&nbsp;&nbsp;Cancel</button>-->');
        $(".editor-row").fadeIn();
        editor.session.setScrollTop(0)
        /*
        $(".ace_scrollbar").scrollTop();
        $(".ace_scroller").scrollTop();
        $("#editor").scrollTop();
        */
    });
}

function save(location) {
    notify("Save","Save command sent","success");
    $.post(api+"savescript", {path: location, contents:editor.getValue()}, function(result){
        notify("Saved","File successfully saved","success");
    });
}

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
