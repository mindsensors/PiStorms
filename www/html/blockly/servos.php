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

<category name="Servos" colour="240">
  <block type="servo_init"></block>
  <block type="servo_init2"></block>
  <sep gap="50"></sep>

  <block type="servo_pos"></block>
  <block type="servo_setspeed"></block>
  <block type="servo_stop"></block>
  <sep gap="50"></sep>

  <block type="servo_setneutralpoint"></block>
  <block type="servo_setneutral"></block>
  <sep gap="50"></sep>

  <block type="servo_setpulse"></block>
</category>



<script>
Blockly.Blocks['servo_init'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("new servo at")
        .appendField(new Blockly.FieldDropdown([["BAS1","'BAS1'"], ["BAS2","'BAS2'"], ["BAS3","'BAS3'"], ["BBS1","'BBS1'"], ["BBS2","'BBS2'"], ["BBS3","'BBS3'"]]), "port_selector");
    this.setOutput(true, null);
    this.setColour(230);
    this.setTooltip("Set up a new servo. Be sure to save it to a variable! Look under \"Custom Vars\".");
    this.setHelpUrl("http://www.mindsensors.com/reference/PiStorms/html/class_pi_storms_grx_1_1_pi_storms_grx.html");
  }
};
Blockly.Python['servo_init'] = function(block) {
  var port = block.getFieldValue('port_selector');
  Blockly.Python.definitions_.from_PiStorms_GRX_import_RCServo = "from PiStorms_GRX import RCServo";
  var code = 'RCServo('+port+')';
  return [code, Blockly.Python.ORDER_NONE];
};


Blockly.Blocks['servo_init2'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("new servo at")
        .appendField(new Blockly.FieldDropdown([["BAS1","'BAS1'"], ["BAS2","'BAS2'"], ["BAS3","'BAS3'"], ["BBS1","'BBS1'"], ["BBS2","'BBS2'"], ["BBS3","'BBS3'"]]), "port_selector")
        .appendField("with neutral point")
        .appendField(new Blockly.FieldNumber(1500, 500, 2500, 1), "neutralPoint");
    this.setOutput(true, null);
    this.setColour(230);
    this.setTooltip("Set up a new servo. Be sure to save it to a variable! Look under \"Custom Vars\".");
    this.setHelpUrl("http://www.mindsensors.com/reference/PiStorms/html/class_pi_storms_grx_1_1_pi_storms_grx.html");
  }
};
Blockly.Python['servo_init'] = function(block) {
  var port = block.getFieldValue('port_selector');
  var neutralPoint = block.getFieldValue('neutralPoint');
  Blockly.Python.definitions_.from_PiStorms_GRX_import_RCServo = "from PiStorms_GRX import RCServo";
  var code = 'RCServo('+port+', '+neutralPoint+')';
  return [code, Blockly.Python.ORDER_NONE];
};


Blockly.Blocks['servo_pos'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("move")
        .appendField(new Blockly.FieldVariable("servo"), "RCServo_instance")
        .appendField("to position")
        .appendField(new Blockly.FieldNumber(90, 0, 180), "pos");
        //.appendField(new Blockly.FieldAngle('0'), 'NUM'); // not using this because we can't restrict the bounds to a semi-circle
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip("Move a (regular) servo to a position. The position can be between 0 and 180 degrees. This should match your physical servo.");
    this.setHelpUrl("http://www.mindsensors.com/reference/PiStorms/html/class_pi_storms_grx_1_1_pi_storms_grx.html");
  }
};
Blockly.Python['servo_pos'] = function(block) {
  var servo = Blockly.Python.variableDB_.getName(block.getFieldValue('RCServo_instance'), Blockly.Variables.NAME_TYPE);
  var pos = block.getFieldValue('pos');
  var code = servo+'.setPos('+pos+')\n';
  return code;
};


Blockly.Blocks['servo_setspeed'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("set")
        .appendField(new Blockly.FieldVariable("servo"), "RCServo_instance")
        .appendField("speed to")
        .appendField(new Blockly.FieldNumber(0, -100, 100), "speed");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip("Set a continuous rotation servo to a speed from -100 (reverse) to 100 (forwards). If your servo moves even when set to 0 speed (\"drifting\"), be sure to run the calibration program in the 45-Utils folder!");
    this.setHelpUrl("http://www.mindsensors.com/reference/PiStorms/html/class_pi_storms_grx_1_1_pi_storms_grx.html");
  }
};
Blockly.Python['servo_setspeed'] = function(block) {
  var servo = Blockly.Python.variableDB_.getName(block.getFieldValue('RCServo_instance'), Blockly.Variables.NAME_TYPE);
  var speed = block.getFieldValue('speed');
  var code = servo+'.setSpeed('+speed+')\n';
  return code;
};


Blockly.Blocks['servo_stop'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("stop")
        .appendField(new Blockly.FieldVariable("servo"), "RCServo_instance");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip("No matter what, stop sending a pulse to this servo. Even if a continuous rotation servo does not have its neutral point set correctly, this will stop it.");
    this.setHelpUrl("http://www.mindsensors.com/reference/PiStorms/html/class_pi_storms_grx_1_1_pi_storms_grx.html");
  }
};
Blockly.Python['servo_stop'] = function(block) {
  var servo = Blockly.Python.variableDB_.getName(block.getFieldValue('RCServo_instance'), Blockly.Variables.NAME_TYPE);
  var code = servo+'.stop()\n';
  return code;
};


Blockly.Blocks['servo_setneutralpoint'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("set")
        .appendField(new Blockly.FieldVariable("servo"), "RCServo_instance")
        .appendField("'s neutral point to")
        .appendField(new Blockly.FieldNumber(1500, 500, 2500, 1), "neutralPoint");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip("Set the standard (resting) pulse for this servo. See the tooltip for \"set pulse\" for more details. The neutral point should be 1500, but all servos vary slightly when they are manufactured. For instance, your servo might still spin when set to 1500, but 1680 is the actual \"middle\".");
    this.setHelpUrl("http://www.mindsensors.com/reference/PiStorms/html/class_pi_storms_grx_1_1_pi_storms_grx.html");
  }
};
Blockly.Python['servo_setneutralpoint'] = function(block) {
  var servo = Blockly.Python.variableDB_.getName(block.getFieldValue('RCServo_instance'), Blockly.Variables.NAME_TYPE);
  var neutralPoint = block.getFieldValue('neutralPoint');
  var code = servo+'.setNeutralPoint('+neutralPoint+')\n';
  return code;
};


Blockly.Blocks['servo_setneutral'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("move")
        .appendField(new Blockly.FieldVariable("servo"), "RCServo_instance")
        .appendField("to its neutral position");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip("Return this servo to its neutral position. This should move normal servos to the middle, and stop continuous rotation servos.");
    this.setHelpUrl("http://www.mindsensors.com/reference/PiStorms/html/class_pi_storms_grx_1_1_pi_storms_grx.html");
  }
};
Blockly.Python['servo_setneutral'] = function(block) {
  var servo = Blockly.Python.variableDB_.getName(block.getFieldValue('RCServo_instance'), Blockly.Variables.NAME_TYPE);
  var code = servo+'.setNeutral()\n';
  return code;
};


Blockly.Blocks['servo_setpulse'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("set")
        .appendField(new Blockly.FieldVariable("servo"), "RCServo_instance")
        .appendField("'s pulse to")
        .appendField(new Blockly.FieldNumber(1500, 500, 2500, 1), "pulse")
        .appendField("microseconds");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip("This is more low-level, most people won't have to (or want to) use this. You can set the number of microseconds between pulses sent to this servo. 500 is the minimum, 2500 is the maximum. 1500 should be the median, but read the tooltip for \"set neutral position\".");
    this.setHelpUrl("http://www.mindsensors.com/reference/PiStorms/html/class_pi_storms_grx_1_1_pi_storms_grx.html");
  }
};
Blockly.Python['servo_setpulse'] = function(block) {
  var servo = Blockly.Python.variableDB_.getName(block.getFieldValue('RCServo_instance'), Blockly.Variables.NAME_TYPE);
  var pulse = block.getFieldValue('pulse');
  var code = servo+'.setPulse('+pulse+')\n';
  return code;
};
</script>
