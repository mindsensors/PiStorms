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
?>  <footer class="main-footer">
    <!--<div class="pull-right hidden-xs">
      <b>Software Version:</b> <span class="software_version"><i class="fa fa-refresh fa-spin"></i> fetching</span> / <b>Hardware Version:</b> <span class="firmware_version"><i class="fa fa-refresh fa-spin"></i> fetching</span>
    </div>-->
    <strong>PiStorms by <a href="http://mindsensors.com" target="_blank">mindsensors.com</a></strong>
  </footer>
  


<div class="modal fade" id="questionFormModal" tabindex="-1" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title">Submit a Bug Report</h4>
      </div>
      <div class="modal-body" id="qbody">
        
        <form action="javascript:question()">
          <h4>Name:</h4>
          <div class="form-group">
            <input id="namein" type="name" class="form-control" placeholder="Name" required>
          </div>
          <h4 style="margin-top:15px">Email:</h4>
          <div class="form-group">
            <input id="emailin" type="email" class="form-control" placeholder="Email" required>
          </div>
          <h4 style="margin-top:15px">Short Title:</h4>
          <div class="form-group">
            <input id="titlein" type="text" class="form-control" placeholder="Short Title" required>
          </div>
          <h4 style="margin-top:15px">Description:</h4>
          <div class="form-group">
            <textarea id="messagein" class="form-control" rows="3" placeholder="Explain the bug in detail and add any other supporting information here as well. Please mention the version numbers, device used, and the page on which the bug occured." required></textarea>
          </div>
          <button type="submit" value="Submit" class="btn btn-flat btn-success">Submit</button>
        </form>
              
      </div>

    </div>
  </div>
</div>

<script>
function question() {
    var namev = $("#namein").val();
    var emailv = $("#emailin").val();
    var titlev = $("#titlein").val();
    var messagev = $("#messagein").val();
    $.post("https://script.google.com/macros/s/AKfycbz1CWSRnawPwAJ38iqA_De4C2ynKVF5Sd4Pe8uUCvDE94EBmQ1i/exec", {name_s: namev, email_s: emailv, summary_s: titlev, description_s: messagev}, function(data){
        $("#qbody").html("<h4>Bug report successfully sent!</h4>");
    });
}
</script>