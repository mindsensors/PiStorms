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

<category name="System" colour="5">
  <block type="system_print">
    <value name="TEXT">
      <shadow type="text">
        <field name="TEXT">Hello World</field>
      </shadow>
    </value>
  </block>

  <block type="system_sleep">
    <value name="TIME">
      <shadow type="math_number">
        <field name="NUM">3</field>
      </shadow>
    </value>
  </block>

  <block type="system_exit"></block>

  <block type="variable_pistorms"></block>

  <block type="system_shutdown"></block>

  <block type="system_getbattery"></block>

  <block type="system_getfirmware"></block>

  <block type="system_getvendor"></block>

  <block type="system_getdeviceid"></block>
</category>



<script>
Blockly.Blocks['system_print'] = {
  init: function() {
    this.appendValueInput("TEXT")
        .setCheck(null)
        .appendField("print");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(5);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['system_print'] = function(block) {
  var value_text = Blockly.Python.valueToCode(block, 'TEXT', Blockly.Python.ORDER_ATOMIC);
  var code = 'print(' + value_text + ')\n';
  return code;
};


Blockly.Blocks['system_sleep'] = {
  init: function() {
    this.appendValueInput("TIME")
        .setCheck("Number")
        .appendField("pause for");
    this.appendDummyInput()
        .appendField("seconds");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(5);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['system_sleep'] = function(block) {
  var value_time = Blockly.Python.valueToCode(block, 'TIME', Blockly.Python.ORDER_ATOMIC);
  Blockly.Python.definitions_.import_time = "import time";
  var code = 'time.sleep('+value_time+')\n';
  return code;
};


Blockly.Blocks['system_exit'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("exit out of the program");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(5);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['system_exit'] = function(block) {
  var code = 'sys.exit(-1)\n';
  return code;
};


Blockly.Blocks['variable_pistorms'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("PiStorms Instance");
    this.setInputsInline(true);
    this.setOutput(true, "PiStorms");
    this.setColour(330);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['variable_pistorms'] = function(block) {
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm';
  return [code, Blockly.Python.ORDER_NONE];
};


Blockly.Blocks['system_shutdown'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("shutdown PiStorms");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(5);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['system_shutdown'] = function(block) {
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.Shutdown()\n';
  return code;
};


Blockly.Blocks['system_getbattery'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("get battery voltage");
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(5);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['system_getbattery'] = function(block) {
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.battVoltage()';
  return [code, Blockly.Python.ORDER_NONE];
};


Blockly.Blocks['system_getfirmware'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("get firmware version");
    this.setInputsInline(true);
    this.setOutput(true, "String");
    this.setColour(5);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['system_getfirmware'] = function(block) {
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.GetFirmwareVersion()';
  return [code, Blockly.Python.ORDER_NONE];
};


Blockly.Blocks['system_getvendor'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("get vendor name");
    this.setInputsInline(true);
    this.setOutput(true, "String");
    this.setColour(5);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['system_getvendor'] = function(block) {
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.GetVendorName()';
  return [code, Blockly.Python.ORDER_NONE];
};


Blockly.Blocks['system_getdeviceid'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("get device ID");
    this.setInputsInline(true);
    this.setOutput(true, "String");
    this.setColour(5);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['system_getdeviceid'] = function(block) {
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.GetDeviceId()';
  return [code, Blockly.Python.ORDER_NONE];
};
</script>
