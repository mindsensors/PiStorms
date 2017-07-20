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
# Date           Author          Comments
# July 2017      Seth Tenembaum  Split into multiple files
*/
?>

<category name="Buttons_GRX" colour="200">
  <block type="system_keypressed"></block>
  <block type="system_getkeypresscount"></block>
  <block type="system_resetkeypresscount"></block>
</category>



<script>
Blockly.Blocks['system_keypressed'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("check if GO button is pressed");
    this.setInputsInline(true);
    this.setOutput(true, "Boolean");
    this.setColour(200);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['system_keypressed'] = function(block) {
  Blockly.Python.definitions_.import_PiStorms_GRX = "from PiStorms_GRX import PiStorms_GRX";
  Blockly.Python.definitions_.grx_PiStorms_GRX = "grx = PiStorms_GRX()";
  var code = 'grx.isKeyPressed()';
  return [code, Blockly.Python.ORDER_NONE];
};


Blockly.Blocks['system_getkeypresscount'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("get key press count");
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(200);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['system_getkeypresscount'] = function(block) {
  Blockly.Python.definitions_.import_PiStorms_GRX = "from PiStorms_GRX import PiStorms_GRX";
  Blockly.Python.definitions_.grx_PiStorms_GRX = "grx = PiStorms_GRX()";
  var code = 'grx.getKeyPressCount()';
  return [code, Blockly.Python.ORDER_NONE];
};


Blockly.Blocks['system_resetkeypresscount'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("reset key press count");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(200);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['system_resetkeypresscount'] = function(block) {
  Blockly.Python.definitions_.import_PiStorms_GRX = "from PiStorms_GRX import PiStorms_GRX";
  Blockly.Python.definitions_.grx_PiStorms_GRX = "grx = PiStorms_GRX()";
  var code = 'grx.resetKeyPressCount()\n';
  return code;
};
</script>
