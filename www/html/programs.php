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
# Date              Author          Comments
# July 2016         Roman Bohuk     Initial Authoring
# December 2016     Roman Bohuk     A few bugfixes (ability to rename files, bug reporting function)
# May 2017     Seth Tenembaum  Remove login requirement
*/

include "api/config.php";

?><!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="theme-color" content="#DD4B39">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>Programs | PiStorms Web Interface</title>
  <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
  <link rel="stylesheet" href="assets/bootstrap.min.css">  <!-- Font Awesome -->
  <link rel="stylesheet" href="assets/font-awesome.min.css">
  <link rel="stylesheet" href="assets/AdminLTE.min.css">
  <link rel="stylesheet" href="assets/pnotify.min.css">
  <link rel="stylesheet" href="assets/skin-red.min.css">
  <link rel="stylesheet" href="assets/slider.css">
    <script src="assets/blockly/blockly_compressed.js"></script>
  <script src="assets/blockly/blocks_compressed.js"></script>
  <script src="assets/blockly/python_compressed.js"></script>
  <script src="assets/blockly/msg/js/en.js"></script>
  <style>
    .btn-sq {
      width: 50px !important;
      height: 50px !important;
      font-size: 24px;
    }
  </style>
  <style type="text/css" media="screen">
    #blocklyeditor, #aceeditor {
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
        .blocklyeditor-row, .aceeditor-row {
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
                <button type="button" onclick="addfile('py');" class="btn btn-sm btn-flat btn-success"><i class="fa fa-plus"></i>&nbsp;&nbsp;File</button>
                <button type="button" onclick="addfile('bl');" class="btn btn-sm btn-flat btn-info"><i class="fa fa-plus"></i>&nbsp;&nbsp;Blockly File</button>
                <button type="button" onclick="addfile('folder');" class="btn btn-sm btn-flat btn-primary"><i class="fa fa-plus"></i>&nbsp;&nbsp;Folder</button>
              </div>
            </div>
            <div class="box-body" id="programs_list" style="max-height:640px; overflow: auto;">
              <div class="text-center"><h4><i class="fa fa-refresh fa-spin"></i>&nbsp;&nbsp;Fetching</h4></div>
            </div>
          </div>
        </div>

        <div class="col-md-6 col-lg-8" id="editorDash">
          <div class="box box-danger" style="margin-bottom:0px !important;padding-bottom:0px !important;">
            <div class="box-body" id="edit_options">
                Please select a program on the left or create a new file
            </div>
          </div>
        </div>
        <div class="col-md-6 col-lg-8 aceeditor-row" style="display:none">
          <div class="box">
            <div class="box-body" style="height:630px;">
               <div id="aceeditor" class="editor" style="height: 100%; width: 100%;"></div>
            </div>
          </div>
        </div>
        <div class="col-md-6 col-lg-8 blocklyeditor-row" style="display:none">
          <div class="box">
            <div class="box-body" style="height:630px;">
               <div id="blocklyeditor" class="editor" style="height: 100%; width: 100%;"></div>
            </div>
          </div>
        </div>

      </div>

    </section>
  </div>

<?php include_once("./components/footer.php"); ?>

</div>


<div class="modal fade" tabindex="-1" id="filenameModal" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title">Enter Name</h4>
      </div>
      <div class="modal-body">
        Create an object in <code id="pathmodal">/home/pi/PiStorms/programs/</code>
        <br><br>
        <div id="modalinputgroup" class="form-group">
            <input class="form-control" minlen="2" type="text" id="filenameinput" placeholder="Enter file name here">
            <span id="modalinputhelp" class="help-block"></span>
        </div>
        <input class="form-control" type="hidden" id="filetypeinput" value="">
        The name must start with a 2-digit number to be displayed. Example: <code>01-Sample</code><br>Do not put a file extension
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default btn-flat" data-dismiss="modal">Close</button>
        <button type="button" onclick="createobject()" class="btn btn-success btn-flat">Create new <span id="objecttype"></span></button>
      </div>
    </div>
  </div>
</div>

<div class="modal fade" tabindex="-1" id="renameModal" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title">Rename File</h4>
      </div>
      <div class="modal-body">
        Rename <code id="file2"></code> to
        <br><br>
        <div id="modalinputgroup2" class="form-group">
            <input class="form-control" minlen="2" type="text" id="filenameinput2" placeholder="Enter new name here">
            <input type="hidden" id="id2">
            <span id="modalinputhelp2" class="help-block"></span>
        </div>
        <input class="form-control" type="hidden" id="filetypeinput2" value="">
        The name must start with a 2-digit number to be displayed. Example: <code>01-Sample</code><br>Do not put a file extension
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default btn-flat" data-dismiss="modal">Close</button>
        <button type="button" onclick="renameobject()" class="btn btn-success btn-flat">Rename</button>
      </div>
    </div>
  </div>
</div>


<script src="assets/jquery.min.js"></script>
<script src="assets/bootstrap.min.js"></script>
<script type="text/javascript" src="assets/app.min.js"></script>
<script type="text/javascript" src="assets/pnotify.min.js"></script>
<script type="text/javascript" src="assets/jquery.slimscroll.min.js"></script>
<script type="text/javascript" src="assets/bootstrap-slider.min.js"></script>
<script type="text/javascript" src="assets/sha256.min.js"></script>

<xml id="toolbox" style="display: none">
    <?php include "blockly/standard.php"; ?>
    <?php include "blockly/motors.php"; ?>
    <?php include "blockly/servos.php"; ?>
    <?php include "blockly/sensors.php"; ?>
    <?php include "blockly/screen.php"; ?>
    <?php include "blockly/led.php"; ?>
    <?php include "blockly/buttons.php"; ?>
    <?php include "blockly/system.php"; ?>
</xml>

<script>
setTimeout(()=>$("body").addClass("sidebar-collapse"), 10);

var api = "http://<?=$_SERVER['SERVER_NAME']?>:3141/";
$.get(api+'isgrx', function(data) {
    if (data=='1')
        $('#toolbox category[name=Motors]').remove();
    else
        $('#toolbox category[name=Servos]').remove();
});
</script>

<script src="assets/ace/ace.js"></script>

<script>
var justcreated = false;
var justcreatedfile = "";
var justcreatedtype = "";

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

var currentdir = "";
var initdir = "";
var api = "http://<?=$_SERVER['SERVER_NAME']?>:3141/";

var tbl = '<table class="table table-striped">\
                <tr>\
                  <th class="text-center">Type</th>\
                  <th class="text-center">Name</th>\
                  <th style="width:120px" class="text-center">Actions</th>\
                </tr>';
var filerow = '<tr>\
                  <td class="text-center"><img src="assets/&&ft&&.png" alt="object" style="height:40px"></img></td>\
                  <td class="text-center"><b>&&fn&&</b></td>\
                  <td class="text-center"><button onclick="edit(\'&&fn&&\',\'&&fl&&\',\'&&id&&\')" style="width:32px;" class="btn btn-flat btn-success btn-sm"><i class="fa fa-pencil-square-o" aria-hidden="true"></i></button><button onclick="rename(\'&&fn&&\',\'&&fl&&\',\'&&id&&\')" style="width:32px;" class="btn btn-flat btn-warning btn-sm"><i class="fa fa-font" aria-hidden="true"></i></button><button style="width:32px;" onclick="deleteFile(&&id&&);" class="btn btn-flat btn-danger btn-sm"><i class="fa fa-trash" aria-hidden="true"></i></button></td>\
                </tr>';
var folderrow = '<tr>\
                  <td class="text-center"><img src="assets/&&ft&&.png" alt="object" style="height:40px"></img></td>\
                  <td class="text-center"><b>&&fn&&</b></td>\
                  <td class="text-center"><button style="width:32px;" onclick="traverse(\'&&fn&&\');" class="btn btn-flat btn-info btn-sm"><i class="fa fa-level-down" aria-hidden="true"></i></button><button onclick="rename(\'&&fn&&\',\'&&fl&&\',\'&&id&&\')" style="width:32px;" class="btn btn-flat btn-warning btn-sm"><i class="fa fa-font" aria-hidden="true"></i></button><button style="width:32px;" onclick="deleteDirectory(&&id&&);" class="btn btn-flat btn-danger btn-sm"><i class="fa fa-trash" aria-hidden="true"></i></button></td>\
                </tr>';
var backrow = '<tr style="cursor:pointer" onclick="traverseup();">\
                  <td class="text-center"><img src="assets/updir.png" alt="object" style="height:34px;margin:3px;"></img></td>\
                  <td class="text-center"><b>Go back up</b></td>\
                </tr>';

var progs = [];

function fetchlist() {
    $.post(api + "getprograms", {path:currentdir}, function(data){
        data = $.parseJSON(data);
        progs = data;
        table = tbl;
        if (currentdir != initdir) {
            table += backrow;
        }
        for (var i = 0; i < data.length; i++) {
            table += (data[i][2] == "py" || data[i][2] == "bl" ? filerow : folderrow).replace("&&ft&&", data[i][2] == "py" ? "python" : data[i][2] == "bl" ? "blockly" : "folder").split("&&fn&&").join(data[i][0]).replace("&&fl&&",data[i][1]).split("&&id&&").join(i);
            if (justcreated && data[i][2] == justcreatedtype && data[i][0].split(".")[0] == justcreatedfile.split(".")[0]) {
                edit(data[i][0],data[i][1],i);
            }
        }
        table += "</table>";
        $("#programs_list").html(table);
        $("#programs_list").addClass("no-padding");
    });
}

$.get(api + "getprogramsdir", function(data){
    currentdir = data;
    initdir = data;
    fetchlist();
});


var editor = ace.edit("aceeditor");
editor.setTheme("ace/theme/monokai");
editor.getSession().setMode("ace/mode/python");
editor.setOptions({
   autoScrollEditorIntoView: true
});
var workspace = null;


var edittype = "";

function blocklyedit(filename, location, id, content) {
    var stored = content.split('--START BLOCKS--\n')[1].split('\n--END BLOCKS--')[0].split("\n");
    var broken = stored.length != 2;
    var hash = CryptoJS.SHA256(stored[0]).toString();
    broken = broken || hash != stored[1];
    if (broken) {
        if (confirm("The blockly file is corrupted and the program can't restore the saved blocks. Do you want to edit the code in a text editor instead?")) {
            edittype = "py";
            aceedit(filename, location, id, content);
            return 0;
        }
    }
    var xml_text = Base64.decode(stored[0]);
    $(".aceeditor-row").hide();
    $(".blocklyeditor-row").show();
    if (workspace != null) {workspace.dispose();}
    workspace = Blockly.inject('blocklyeditor',
      {toolbox: document.getElementById('toolbox')});
    var xml = Blockly.Xml.textToDom(xml_text);
    Blockly.Xml.domToWorkspace(xml, workspace);
}

function aceedit(filename, location, id, content) {
    edittype = "py";
    if (workspace != null) {workspace.dispose();}
    $(".blocklyeditor-row").hide();
    editor.setValue(content);
    editor.gotoLine(1);
    $(".aceeditor-row").show();
    editor.session.setScrollTop(0)
}


function edit(filename, location, id) {
    $.post(api+"fetchscript", {path: location}, function(result){
        edittype = progs[id][2];
        $("#edit_options").html('<span style="font-size:20px;padding-bottom:0px;margin-bottom:-10px;display:block;">Edit <b>' + filename + '</b></span><br><button type="button" class="btn btn-success btn-flat btn-settings" onclick="save(\'' + location + '\')"><i class="fa fa-save" aria-hidden="true"></i>&nbsp;&nbsp;Save</button><!--<button type="button" class="btn btn-danger btn-flat btn-settings"><i class="fa fa-ban" aria-hidden="true"></i>&nbsp;&nbsp;Cancel</button>-->');
        if (progs[id][2] == "bl") {
            blocklyedit(filename, location, id, result);
            return 0;
        } else {
            aceedit(filename, location, id, result);
            return 1;
        }
    });
    var current = $(document).scrollTop();
    var need = $("#editorDash").offset().top - 20;
    if (current > need || Math.abs(current - need) > 70) {
        $('html,body').animate({
           scrollTop: need
        });
    }
}


var copyright = '\n# Copyright (c) ' + new Date().getFullYear() + ' mindsensors.com\n# \n# This program is free software; you can redistribute it and/or modify\n# it under the terms of the GNU General Public License version 2 as\n# published by the Free Software Foundation.\n#\n# This program is distributed in the hope that it will be useful,\n# but WITHOUT ANY WARRANTY; without even the implied warranty of\n# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the\n# GNU General Public License for more details.\n#\n# You should have received a copy of the GNU General Public License\n# along with this program; if not, write to the Free Software\n# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.\n#\n#mindsensors.com invests time and resources providing this open source code, \n#please support mindsensors.com  by purchasing products from mindsensors.com!\n#Learn more product option visit us @  http://www.mindsensors.com\n';

function save(location) {
    var content = "";
    if (edittype == "bl") {
        var xml = Blockly.Xml.workspaceToDom(workspace);
        var xml_code = Blockly.Xml.domToText(xml);
        var blocks = Base64.encode(xml_code);
        var code = Blockly.Python.workspaceToCode(workspace);
        content = '#!/usr/bin/env python\n\n# ATTENTION!\n# Please do not manually edit the contents of this file\n# Only use the web interface for editing\n# Otherwise, the file may no longer be editable using the web interface, or you changes may be lost\n' + copyright + '\n"""\n--BLOCKLY FILE--\n--START BLOCKS--\n' + blocks + '\n' + CryptoJS.SHA256(blocks).toString() + '\n--END BLOCKS--\n"""\n\n\n' + code;

    } else if (edittype == "py") {
        content = editor.getValue();
    }
    $.post(api+"savescript", {path: location, contents:content}, function(result){
        notify("Saved","File successfully saved","success");
        fetchlist();
    });

}

function deleteFile(id) {
    var location = progs[id][1];
    if (progs[id][2] == "folder") {
        notify("Error","An error has occured","error");
        return 0;
    }
    if (confirm("Are you sure you want to delete this file?")) {
        $.post(api+"removefile", {path: location}, function(result){
            notify("Deleted","File successfully deleted","success");
        });
        fetchlist();
    }
}

function deleteDirectory(id) {
    var location = progs[id][1];
    if (progs[id][2] != "folder") {
        notify("Error","An error has occured","error");
        return 0;
    }
    if (confirm("Are you sure you want to delete this folder?")) {
        $.post(api+"removedir", {path: location}, function(result){
            notify("Deleted","Folder successfully deleted","success");
        });
        fetchlist();
    }
}

function traverse(path) {
    currentdir += path;
    fetchlist();
}

function traverseup() {
    currentdir = currentdir.split("/").slice(0,currentdir.split("/").length-1).join("/") + "/";
    fetchlist();
}

$("#srwb").click(function(){$.get(api+"startrecording/withBg", function(data){});notify("Success","Started taking frames with background","success");});
$("#stpr").click(function(){$.get(api+"stoprecording", function(data){});notify("Success","Stopped recording","success");});
$("#chkr").click(function(){$.get(api+"readrecording", function(data){notify("Result",data,"success");});});
$("#clar").click(function(){
    if (confirm("Are you sure you want to permanently remove all screenshots?")) {
        $.get(api+"clearimages", function(data){notify("Result","Images cleared","success");});
    }
});


function addfile(type) {
    $("#filenameinput").val("")
    $('#objecttype').html(type == "folder" ? "Folder" : type == "bl" ? "Drag-and-drop program" : "Python program")
    if (type == "folder") {$('#filenameinput').attr("placeholder", "Enter folder name here.");}
    $("#filetypeinput").val(type);
    var pathtoadd = currentdir.charAt(currentdir.length-1) != "/" ? currentdir + "/" : currentdir;
    $("#pathmodal").html(pathtoadd);
    $('#filenameModal').modal('show');
}

function checkname(type) {
    $("#filenameinput").val("")
    $('#objecttype').html(type == "folder" ? "Folder" : type == "bl" ? "Drag-and-drop program" : "Python program")
    if (type == "folder") {$('#filenameinput').attr("placeholder", "Enter folder name here.");}
    $("#filetypeinput").val(type);
    $('#filenameModal').modal('show');
}


/**
*
*  Base64 encode / decode
*  http://www.webtoolkit.info/
*
**/
var Base64 = {

// private property
_keyStr : "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",

// public method for encoding
encode : function (input) {
    var output = "";
    var chr1, chr2, chr3, enc1, enc2, enc3, enc4;
    var i = 0;

    input = Base64._utf8_encode(input);

    while (i < input.length) {

        chr1 = input.charCodeAt(i++);
        chr2 = input.charCodeAt(i++);
        chr3 = input.charCodeAt(i++);

        enc1 = chr1 >> 2;
        enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
        enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
        enc4 = chr3 & 63;

        if (isNaN(chr2)) {
            enc3 = enc4 = 64;
        } else if (isNaN(chr3)) {
            enc4 = 64;
        }

        output = output +
        this._keyStr.charAt(enc1) + this._keyStr.charAt(enc2) +
        this._keyStr.charAt(enc3) + this._keyStr.charAt(enc4);

    }

    return output;
},

// public method for decoding
decode : function (input) {
    var output = "";
    var chr1, chr2, chr3;
    var enc1, enc2, enc3, enc4;
    var i = 0;

    input = input.replace(/[^A-Za-z0-9\+\/\=]/g, "");

    while (i < input.length) {

        enc1 = this._keyStr.indexOf(input.charAt(i++));
        enc2 = this._keyStr.indexOf(input.charAt(i++));
        enc3 = this._keyStr.indexOf(input.charAt(i++));
        enc4 = this._keyStr.indexOf(input.charAt(i++));

        chr1 = (enc1 << 2) | (enc2 >> 4);
        chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
        chr3 = ((enc3 & 3) << 6) | enc4;

        output = output + String.fromCharCode(chr1);

        if (enc3 != 64) {
            output = output + String.fromCharCode(chr2);
        }
        if (enc4 != 64) {
            output = output + String.fromCharCode(chr3);
        }

    }

    output = Base64._utf8_decode(output);

    return output;

},

// private method for UTF-8 encoding
_utf8_encode : function (string) {
    string = string.replace(/\r\n/g,"\n");
    var utftext = "";

    for (var n = 0; n < string.length; n++) {

        var c = string.charCodeAt(n);

        if (c < 128) {
            utftext += String.fromCharCode(c);
        }
        else if((c > 127) && (c < 2048)) {
            utftext += String.fromCharCode((c >> 6) | 192);
            utftext += String.fromCharCode((c & 63) | 128);
        }
        else {
            utftext += String.fromCharCode((c >> 12) | 224);
            utftext += String.fromCharCode(((c >> 6) & 63) | 128);
            utftext += String.fromCharCode((c & 63) | 128);
        }

    }

    return utftext;
},

// private method for UTF-8 decoding
_utf8_decode : function (utftext) {
    var string = "";
    var i = 0;
    var c = c1 = c2 = 0;

    while ( i < utftext.length ) {

        c = utftext.charCodeAt(i);

        if (c < 128) {
            string += String.fromCharCode(c);
            i++;
        }
        else if((c > 191) && (c < 224)) {
            c2 = utftext.charCodeAt(i+1);
            string += String.fromCharCode(((c & 31) << 6) | (c2 & 63));
            i += 2;
        }
        else {
            c2 = utftext.charCodeAt(i+1);
            c3 = utftext.charCodeAt(i+2);
            string += String.fromCharCode(((c & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63));
            i += 3;
        }

    }

    return string;
}

}



// http://stackoverflow.com/a/10834843/3600428
function isInteger(str) {
    var n = ~~Number(str);
    return String(n) === str && n >= 0;
}

function createobject() {
    var typein = $("#filetypeinput").val();
    var namein = $("#filenameinput").val();

    var grievances = [];
    for (var i = 0; i < progs.length; i++) {
        if (progs[i][0].toLowerCase() == namein.toLowerCase() || progs[i][0].toLowerCase() == namein.toLowerCase()+".py") {
            grievances.push("An object with such name already exists!");
            break;
        }
    }
    if (namein.length <= 3) {
        grievances.push("Filename is too short!");
    }
    if (!isInteger(namein.substring(0,2).replace("0","1"))) {
        grievances.push("The filename does not start with a 2-digit number!");
    }
    var legal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    var ext = "-_";
    for (var i = 0; i < namein.length; i++) {
        if ((legal + ext).indexOf(namein.charAt(i)) < 0) {
            grievances.push("The filename cannot contain spaces and special characters other than <code>-_</code>!");
            break;
        }
    }
    if (legal.indexOf(namein.charAt(namein.length - 1)) < 0) {
        grievances.push("The filename cannot end with a special character!");
    }

    if (grievances.length <= 0) {
        $.post(api+"addobject", {path: currentdir, type:typein, filename:namein}, function(result){
            notify("Success","Object successfully created","success");
            fetchlist();
            grievances = [];
            $('#filenameModal').modal('hide');
            $('#filenameinput').val("");
            $('#modalinputhelp').html('');
            $('#modalinputgroup').removeClass('has-error');
            if (typein == "bl" || typein == "py") {
                justcreated = true;
                justcreatedfile = namein;
                justcreatedtype = typein;
            }
        });
    } else {
        $('#modalinputgroup').addClass('has-error');
        $('#modalinputhelp').html(grievances.join('<br>'));
    }
}



function rename(filename, location, id) {
    $("#filenameinput").val("")
    $("#file2").html(filename);
    $("#id2").val(id);
    $('#renameModal').modal('show');
}

function renameobject() {
    var namein = $("#filenameinput2").val();
    var nameinold = $("#file2").html();
    var end = nameinold.toLowerCase().endsWith(".py") ? ".py" : "";
    var grievances = [];
    if ((nameinold == namein || nameinold == namein+'.py') && namein != "") {
        grievances.push("The name is the same as the original!");
    } else {
        for (var i = 0; i < progs.length; i++) {
            if (progs[i][0].toLowerCase() == namein.toLowerCase() || progs[i][0].toLowerCase() == namein.toLowerCase()+".py") {
                grievances.push("An object with such name already exists!");
                break;
            }
        }
    }
    if (namein.length <= 3) {
        grievances.push("Filename is too short!");
    }
    if (!isInteger(namein.substring(0,2).replace("0","1"))) {
        grievances.push("The filename does not start with a 2-digit number!");
    }
    var legal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    var ext = "-_";
    for (var i = 0; i < namein.length; i++) {
        if ((legal + ext).indexOf(namein.charAt(i)) < 0) {
            grievances.push("The filename cannot contain spaces and special characters other than <code>-_</code>!");
            break;
        }
    }
    if (legal.indexOf(namein.charAt(namein.length - 1)) < 0) {
        grievances.push("The filename cannot end with a special character!");
    }

    if (grievances.length <= 0) {
        console.log({path: currentdir, filename:nameinold, filenamenew:namein + end});
        $.post(api+"renameobject", {path: currentdir, filename:nameinold, filenamenew:namein + end}, function(result){
            if (result == "1") {
                notify("Success","Object renamed successfully","success");
                fetchlist();
                grievances = [];
                $('#filenameModal2').modal('hide');
                $('#filenameinput2').val("");
                $('#modalinputhelp2').html('');
                $('#modalinputgroup2').removeClass('has-error');
                $('#renameModal').modal('hide');
            } else {
                notify("Success","An error has occured","danger");
            }
        });
    } else {
        $('#modalinputgroup2').addClass('has-error');
        $('#modalinputhelp2').html(grievances.join('<br>'));
    }
}


$("#filenameinput").keyup(function (e) {
    if (e.keyCode == 13) {
        createobject();
    }
});
</script>

</body>
</html>
