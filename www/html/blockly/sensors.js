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


var sensors = `
<category name="Sensors" colour="60">
  <block type="sensors_nxttouch"></block>
  <sep gap="5"></sep>
  <block type="sensors_ev3touch"></block>
  <sep gap="5"></sep>
  <block type="sensors_istouchpressed"></block>
  <sep gap="5"></sep>
  <block type="sensors_gettouchbumpcount"></block>
  <sep gap="5"></sep>
  <block type="sensors_resettouchbumpcount"></block>

  <block type="sensors_nxtlight"></block>
  <sep gap="5"></sep>
  <block type="sensors_nxtlightgetvalue"></block>
  <sep gap="5"></sep>
  <block type="sensors_nxtlightsetmode"></block>

  <block type="sensors_nxtcolor"></block>
  <sep gap="5"></sep>
  <block type="sensors_nxtcolorgetcolor"></block>
  <sep gap="5"></sep>
  <block type="sensors_nxtcolorsetmode"></block>

  <block type="sensors_ev3color"></block>
  <sep gap="5"></sep>
  <block type="sensors_ev3colorgetvalue"></block>
  <sep gap="5"></sep>
  <block type="sensors_ev3colorsetmode"></block>

  <block type="sensors_ev3gyro"></block>
  <sep gap="5"></sep>
  <block type="sensors_ev3gyrogetvalue"></block>
  <sep gap="5"></sep>
  <block type="sensors_ev3gyrosetmode"></block>

  <block type="sensors_ev3ultrasonic"></block>
  <sep gap="5"></sep>
  <block type="sensors_ev3ultrasonicgetvalue"></block>
  <sep gap="5"></sep>
  <block type="sensors_ev3ultrasonicdetect"></block>
  <sep gap="5"></sep>
  <block type="sensors_ev3ultrasonicsetmode"></block>

  <block type="sensors_ev3infrared"></block>
  <sep gap="5"></sep>
  <block type="sensors_ev3infraredgetproximity">
    <value name="channel">
      <shadow type="math_number">
        <field name="NUM">1</field>
      </shadow>
    </value>
  </block>
  <sep gap="5"></sep>
  <block type="sensors_ev3infraredchannelheading">
    <value name="channel">
      <shadow type="math_number">
        <field name="NUM">1</field>
      </shadow>
    </value>
  </block>
  <sep gap="5"></sep>
  <block type="sensors_ev3infraredchannelproximity">
    <value name="channel">
      <shadow type="math_number">
        <field name="NUM">1</field>
      </shadow>
    </value>
  </block>
  <sep gap="5"></sep>
  <block type="sensors_ev3infraredgetremote">
    <value name="channel">
      <shadow type="math_number">
        <field name="NUM">1</field>
      </shadow>
    </value>
  </block>
  <sep gap="5"></sep>
  <block type="sensors_ev3infraredsetmode"></block>

  <block type="sensors_absoluteimu"></block>
  <sep gap="5"></sep>
  <block type="sensors_absoluteimugettilt"></block>
  <sep gap="5"></sep>
  <block type="sensors_absoluteimugetacceleration"></block>
  <sep gap="5"></sep>
  <block type="sensors_absoluteimugetmagnetometer"></block>
  <sep gap="5"></sep>
  <block type="sensors_absoluteimugetgyro"></block>
  <sep gap="5"></sep>
  <block type="sensors_absoluteimugetheading"></block>
  <sep gap="5"></sep>
  <block type="sensors_absoluteimusetaccel"></block>
  <sep gap="5"></sep>
  <block type="sensors_absoluteimustartcmpscal"></block>
  <sep gap="5"></sep>
  <block type="sensors_absoluteimustopcmpscal"></block>

  <block type="sensors_sumoeyes"></block>
  <sep gap="5"></sep>
  <block type="sensors_sumoeyesgetvalue"></block>
  <sep gap="5"></sep>
  <block type="sensors_sumoeyessetmode"></block>

  <block type="sensors_lineleader"></block>
  <sep gap="5"></sep>
  <block type="sensors_lineleadergetsteering"></block>
  <sep gap="5"></sep>
  <block type="sensors_lineleadergetaverage"></block>
  <sep gap="5"></sep>
  <block type="sensors_lineleadergetresult"></block>
  <sep gap="5"></sep>
  <block type="sensors_lineleadergetrawcalibrated"></block>

  <block type="sensors_lsa"></block>
  <sep gap="5"></sep>
  <block type="sensors_lsagetrawcalibrated"></block>
</category>
`;


Blockly.Blocks['sensors_nxttouch'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("NXT Touch Sensor at")
        .appendField(new Blockly.FieldDropdown([["BAS1", "BAS1"], ["BAS2", "BAS2"], ["BBS1", "BBS1"], ["BBS2", "BBS2"]]), "sensor_selector");
    this.setInputsInline(true);
    this.setOutput(true, "nxtev3touch");
    this.setColour(0);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_nxttouch'] = function(block) {
  var dropdown_sensor_selector = block.getFieldValue('sensor_selector');
  Blockly.Python.definitions_.import_LegoDevices = "import LegoDevices";
  Blockly.Python.definitions_["nxttouch_" + dropdown_sensor_selector] = 'nxttouch_' + dropdown_sensor_selector + ' = LegoDevices.NXTTouchSensor("' + dropdown_sensor_selector + '")';
  var code = 'nxttouch_' + dropdown_sensor_selector;
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_ev3touch'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("EV3 Touch Sensor at")
        .appendField(new Blockly.FieldDropdown([["BAS1", "BAS1"], ["BAS2", "BAS2"], ["BBS1", "BBS1"], ["BBS2", "BBS2"]]), "sensor_selector");
    this.setInputsInline(true);
    this.setOutput(true, "nxtev3touch");
    this.setColour(0);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_ev3touch'] = function(block) {
  var dropdown_sensor_selector = block.getFieldValue('sensor_selector');
  Blockly.Python.definitions_.import_LegoDevices = "import LegoDevices";
  Blockly.Python.definitions_["ev3touch_" + dropdown_sensor_selector] = 'ev3touch_' + dropdown_sensor_selector + ' = LegoDevices.EV3TouchSensor("' + dropdown_sensor_selector + '")';
  var code = 'ev3touch_' + dropdown_sensor_selector;
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_istouchpressed'] = {
  init: function() {
    this.appendValueInput("sensor")
        .setCheck("nxtev3touch")
        .appendField("is");
    this.appendDummyInput()
        .appendField("pressed");
    this.setInputsInline(true);
    this.setOutput(true, "Boolean");
    this.setColour(0);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_istouchpressed'] = function(block) {
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".isPressed()";
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_gettouchbumpcount'] = {
  init: function() {
    this.appendValueInput("sensor")
        .setCheck("nxtev3touch")
        .appendField("count bumps from");
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(0);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_gettouchbumpcount'] = function(block) {
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".getBumpCount()";
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_resettouchbumpcount'] = {
  init: function() {
    this.appendValueInput("sensor")
        .setCheck("nxtev3touch")
        .appendField("reset bump count of");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(0);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_resettouchbumpcount'] = function(block) {
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".resetBumpCount()\n";
  return code;
};



Blockly.Blocks['sensors_nxtlight'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("NXT Light Sensor at")
        .appendField(new Blockly.FieldDropdown([["BAS1", "BAS1"], ["BAS2", "BAS2"], ["BBS1", "BBS1"], ["BBS2", "BBS2"]]), "sensor_selector");
    this.setInputsInline(true);
    this.setOutput(true, "nxtlight");
    this.setColour(20);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_nxtlight'] = function(block) {
  var dropdown_sensor_selector = block.getFieldValue('sensor_selector');
  Blockly.Python.definitions_.import_LegoDevices = "import LegoDevices";
  Blockly.Python.definitions_["nxtlight_" + dropdown_sensor_selector] = 'nxtlight_' + dropdown_sensor_selector + ' = LegoDevices.NXTLightSensor("' + dropdown_sensor_selector + '")';
  var code = 'nxtlight_' + dropdown_sensor_selector;
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_nxtlightgetvalue'] = {
  init: function() {
    this.appendValueInput("sensor")
        .setCheck("nxtlight")
        .appendField("get value from");
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(20);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_nxtlightgetvalue'] = function(block) {
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".getValue()";
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_nxtlightsetmode'] = {
  init: function() {
    this.appendValueInput("sensor")
        .setCheck("nxtlight")
        .appendField("set mode of");
    this.appendDummyInput()
        .appendField("to")
        .appendField(new Blockly.FieldDropdown([["AMBIENT", "AMBIENT"], ["REFLECTED", "REFLECTED"]]), "mode_selector");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(20);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_nxtlightsetmode'] = function(block) {
  var dropdown_mode_selector = block.getFieldValue('mode_selector');
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".setMode(LegoDevices.PS_SENSOR_MODE_NXT_LIGHT_" + dropdown_mode_selector + ")\n";
  return code;
};



Blockly.Blocks['sensors_nxtcolor'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("NXT Color Sensor at")
        .appendField(new Blockly.FieldDropdown([["BAS1", "BAS1"], ["BAS2", "BAS2"], ["BBS1", "BBS1"], ["BBS2", "BBS2"]]), "sensor_selector");
    this.setInputsInline(true);
    this.setOutput(true, "nxtcolor");
    this.setColour(40);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_nxtcolor'] = function(block) {
  var dropdown_sensor_selector = block.getFieldValue('sensor_selector');
  Blockly.Python.definitions_.import_LegoDevices = "import LegoDevices";
  Blockly.Python.definitions_["nxtcolor_" + dropdown_sensor_selector] = 'nxtcolor_' + dropdown_sensor_selector + ' = LegoDevices.NXTColorSensor("' + dropdown_sensor_selector + '")';
  var code = 'nxtcolor_' + dropdown_sensor_selector;
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_nxtcolorgetcolor'] = {
  init: function() {
    this.appendValueInput("sensor")
        .setCheck("nxtcolor")
        .appendField("get color from");
    this.setInputsInline(true);
    this.setOutput(true, "String");
    this.setColour(40);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_nxtcolorgetcolor'] = function(block) {
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".getColor()";
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_nxtcolorsetmode'] = {
  init: function() {
    this.appendValueInput("sensor")
        .setCheck("nxtcolor")
        .appendField("set mode of");
    this.appendDummyInput()
        .appendField("to")
        .appendField(new Blockly.FieldDropdown([["COLOR", "COLOR"], ["REFLECTED", "REFLECTED"]]), "mode_selector");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(40);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_nxtcolorsetmode'] = function(block) {
  var dropdown_mode_selector = block.getFieldValue('mode_selector');
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".setMode(LegoDevices." + (dropdown_mode_selector == "COLOR" ? "PS_SENSOR_MODE_NXT_COLOR_COLOR" : "PS_SENSOR_TYPE_COLORFULL") + ")\n";
  return code;
};



Blockly.Blocks['sensors_ev3color'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("EV3 Color Sensor at")
        .appendField(new Blockly.FieldDropdown([["BAS1", "BAS1"], ["BAS2", "BAS2"], ["BBS1", "BBS1"], ["BBS2", "BBS2"]]), "sensor_selector");
    this.setInputsInline(true);
    this.setOutput(true, "ev3color");
    this.setColour(60);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_ev3color'] = function(block) {
  var dropdown_sensor_selector = block.getFieldValue('sensor_selector');
  Blockly.Python.definitions_.import_LegoDevices = "import LegoDevices";
  Blockly.Python.definitions_["ev3color_" + dropdown_sensor_selector] = 'ev3color_' + dropdown_sensor_selector + ' = LegoDevices.EV3ColorSensor("' + dropdown_sensor_selector + '")';
  var code = 'ev3color_' + dropdown_sensor_selector;
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_ev3colorgetvalue'] = {
  init: function() {
    this.appendValueInput("sensor")
        .setCheck("ev3color")
        .appendField("get value from");
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(60);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_ev3colorgetvalue'] = function(block) {
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".getValue()";
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_ev3colorsetmode'] = {
  init: function() {
    this.appendValueInput("sensor")
        .setCheck("ev3color")
        .appendField("set mode of");
    this.appendDummyInput()
        .appendField("to")
        .appendField(new Blockly.FieldDropdown([["COLOR", "COLOR"], ["REFLECTED", "REFLECTED"], ["AMBIENT", "AMBIENT"]]), "mode_selector");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(60);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_ev3colorsetmode'] = function(block) {
  var dropdown_mode_selector = block.getFieldValue('mode_selector');
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".setMode(LegoDevices.PS_SENSOR_MODE_EV3_COLOR_" + dropdown_mode_selector + ")\n";
  return code;
};



Blockly.Blocks['sensors_ev3gyro'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("EV3 Gyro Sensor at")
        .appendField(new Blockly.FieldDropdown([["BAS1", "BAS1"], ["BAS2", "BAS2"], ["BBS1", "BBS1"], ["BBS2", "BBS2"]]), "sensor_selector");
    this.setInputsInline(true);
    this.setOutput(true, "ev3gyro");
    this.setColour(80);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_ev3gyro'] = function(block) {
  var dropdown_sensor_selector = block.getFieldValue('sensor_selector');
  Blockly.Python.definitions_.import_LegoDevices = "import LegoDevices";
  Blockly.Python.definitions_["ev3gyro_" + dropdown_sensor_selector] = 'ev3gyro_' + dropdown_sensor_selector + ' = LegoDevices.EV3GyroSensor("' + dropdown_sensor_selector + '")';
  var code = 'ev3gyro_' + dropdown_sensor_selector;
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_ev3gyrogetvalue'] = {
  init: function() {
    this.appendValueInput("sensor")
        .setCheck("ev3gyro")
        .appendField("get value from");
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(80);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_ev3gyrogetvalue'] = function(block) {
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".readValue()";
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_ev3gyrosetmode'] = {
  init: function() {
    this.appendValueInput("sensor")
        .setCheck("ev3gyro")
        .appendField("set mode of");
    this.appendDummyInput()
        .appendField("to")
        .appendField(new Blockly.FieldDropdown([["ANGLE", "ANGLE"], ["RATE", "RATE"]]), "mode_selector");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(80);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_ev3gyrosetmode'] = function(block) {
  var dropdown_mode_selector = block.getFieldValue('mode_selector');
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".setMode(LegoDevices.PS_SENSOR_MODE_EV3_GYRO_" + dropdown_mode_selector + ")\n";
  return code;
};



Blockly.Blocks['sensors_ev3ultrasonic'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("EV3 Ultrasonic Sensor at")
        .appendField(new Blockly.FieldDropdown([["BAS1", "BAS1"], ["BAS2", "BAS2"], ["BBS1", "BBS1"], ["BBS2", "BBS2"]]), "sensor_selector");
    this.setInputsInline(true);
    this.setOutput(true, "ev3ultrasonic");
    this.setColour(100);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_ev3ultrasonic'] = function(block) {
  var dropdown_sensor_selector = block.getFieldValue('sensor_selector');
  Blockly.Python.definitions_.import_LegoDevices = "import LegoDevices";
  Blockly.Python.definitions_["ev3ultrasonic_" + dropdown_sensor_selector] = 'ev3ultrasonic_' + dropdown_sensor_selector + ' = LegoDevices.EV3UltrasonicSensor("' + dropdown_sensor_selector + '")';
  var code = 'ev3ultrasonic_' + dropdown_sensor_selector;
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_ev3ultrasonicgetvalue'] = {
  init: function() {
    this.appendValueInput("sensor")
        .setCheck("ev3ultrasonic")
        .appendField("get distance from");
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(100);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_ev3ultrasonicgetvalue'] = function(block) {
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".getDistance()";
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_ev3ultrasonicdetect'] = {
  init: function() {
    this.appendValueInput("sensor")
        .setCheck("ev3ultrasonic")
        .appendField("detect");
    this.setInputsInline(true);
    this.setOutput(true, "Boolean");
    this.setColour(100);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_ev3ultrasonicdetect'] = function(block) {
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".detect()";
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_ev3ultrasonicsetmode'] = {
  init: function() {
    this.appendValueInput("sensor")
        .setCheck("ev3ultrasonic")
        .appendField("set mode of");
    this.appendDummyInput()
        .appendField("to")
        .appendField(new Blockly.FieldDropdown([["DETECT", "DETECT"], ["DIST_CM", "DIST_CM"], ["DIST_IN", "DIST_IN"]]), "mode_selector");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(100);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_ev3ultrasonicsetmode'] = function(block) {
  var dropdown_mode_selector = block.getFieldValue('mode_selector');
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".setMode(LegoDevices.PS_SENSOR_MODE_EV3_ULTRASONIC_" + dropdown_mode_selector + ")\n";
  return code;
};



Blockly.Blocks['sensors_ev3infrared'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("EV3 Infrared Sensor at")
        .appendField(new Blockly.FieldDropdown([["BAS1", "BAS1"], ["BAS2", "BAS2"], ["BBS1", "BBS1"], ["BBS2", "BBS2"]]), "sensor_selector");
    this.setInputsInline(true);
    this.setOutput(true, "ev3infrared");
    this.setColour(120);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_ev3infrared'] = function(block) {
  var dropdown_sensor_selector = block.getFieldValue('sensor_selector');
  Blockly.Python.definitions_.import_LegoDevices = "import LegoDevices";
  Blockly.Python.definitions_["ev3infrared_" + dropdown_sensor_selector] = 'ev3infrared_' + dropdown_sensor_selector + ' = LegoDevices.EV3InfraredSensor("' + dropdown_sensor_selector + '")';
  var code = 'ev3infrared_' + dropdown_sensor_selector;
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_ev3infraredgetproximity'] = {
  init: function() {
    this.appendValueInput("sensor")
        .setCheck("ev3infrared")
        .appendField("get proximity from");
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(120);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_ev3infraredgetproximity'] = function(block) {
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".readProximity()";
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_ev3infraredchannelheading'] = {
  init: function() {
    this.appendValueInput("sensor")
        .setCheck("ev3infrared")
        .appendField("get channel heading from");
    this.appendValueInput("channel")
        .setCheck("Number")
        .appendField("on channel");
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(120);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_ev3infraredchannelheading'] = function(block) {
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  var value_channel = Blockly.Python.valueToCode(block, 'channel', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".readChannelHeading(" + value_channel + ")";
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_ev3infraredchannelproximity'] = {
  init: function() {
    this.appendValueInput("sensor")
        .setCheck("ev3infrared")
        .appendField("get channel proximity from");
    this.appendValueInput("channel")
        .setCheck("Number")
        .appendField("on channel");
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(120);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_ev3infraredchannelproximity'] = function(block) {
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  var value_channel = Blockly.Python.valueToCode(block, 'channel', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".readChannelProximity(" + value_channel + ")";
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_ev3infraredgetremote'] = {
  init: function() {
    this.appendValueInput("sensor")
        .setCheck("ev3infrared")
        .appendField("get remote position");
    this.appendValueInput("channel")
        .setCheck("Number")
        .appendField("on channel");
    this.setInputsInline(true);
    this.setOutput(true, "Array");
    this.setColour(120);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_ev3infraredgetremote'] = function(block) {
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  var value_channel = Blockly.Python.valueToCode(block, 'channel', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".readRemote(" + value_channel + ")";
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_ev3infraredsetmode'] = {
  init: function() {
    this.appendValueInput("sensor")
        .setCheck("ev3infrared")
        .appendField("set mode of");
    this.appendDummyInput()
        .appendField("to")
        .appendField(new Blockly.FieldDropdown([["CHANNEL", "CHANNEL"], ["PROXIMITY", "PROXIMITY"], ["REMOTE", "REMOTE"]]), "mode_selector");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_ev3infraredsetmode'] = function(block) {
  var dropdown_mode_selector = block.getFieldValue('mode_selector');
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".setMode(LegoDevices.PS_SENSOR_MODE_EV3_IR_" + dropdown_mode_selector + ")\n";
  return code;
};



Blockly.Blocks['sensors_absoluteimu'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("AbsoluteIMU Sensor at")
        .appendField(new Blockly.FieldDropdown([["BAS1", "BAS1"], ["BAS2", "BAS2"], ["BBS1", "BBS1"], ["BBS2", "BBS2"]]), "sensor_selector");
    this.setInputsInline(true);
    this.setOutput(true, "absoluteimu");
    this.setColour(140);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_absoluteimu'] = function(block) {
  var dropdown_sensor_selector = block.getFieldValue('sensor_selector');
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  Blockly.Python.definitions_.import_MsDevices = "import MsDevices";
  Blockly.Python.definitions_["absoluteimu_" + dropdown_sensor_selector] = 'absoluteimu_' + dropdown_sensor_selector + ' = MsDevices.AbsoluteIMU(psm.' + dropdown_sensor_selector + ')';
  var code = 'absoluteimu_' + dropdown_sensor_selector;
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_absoluteimugettilt'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("get")
        .appendField(new Blockly.FieldDropdown([["X", "x"], ["Y", "y"], ["Z", "z"]]), "axis_selector")
        .appendField("tilt from");
    this.appendValueInput("sensor")
        .setCheck("absoluteimu")
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(140);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_absoluteimugettilt'] = function(block) {
  var dropdown_axis_selector = block.getFieldValue('axis_selector');
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".get_tilt" + dropdown_axis_selector + "()";
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_absoluteimugetacceleration'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("get")
        .appendField(new Blockly.FieldDropdown([["X", "x"], ["Y", "y"], ["Z", "z"]]), "axis_selector")
        .appendField("acceleration from");
    this.appendValueInput("sensor")
        .setCheck("absoluteimu")
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(140);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_absoluteimugetacceleration'] = function(block) {
  var dropdown_axis_selector = block.getFieldValue('axis_selector');
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".get_accel" + dropdown_axis_selector + "()";
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_absoluteimugetmagnetometer'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("get")
        .appendField(new Blockly.FieldDropdown([["X", "x"], ["Y", "y"], ["Z", "z"]]), "axis_selector")
        .appendField("magnetometer value from");
    this.appendValueInput("sensor")
        .setCheck("absoluteimu")
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(140);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_absoluteimugetmagnetometer'] = function(block) {
  var dropdown_axis_selector = block.getFieldValue('axis_selector');
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".get_mag" + dropdown_axis_selector + "()";
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_absoluteimugetgyro'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("get")
        .appendField(new Blockly.FieldDropdown([["X", "x"], ["Y", "y"], ["Z", "z"]]), "axis_selector")
        .appendField("gyroscope value from");
    this.appendValueInput("sensor")
        .setCheck("absoluteimu")
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(140);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_absoluteimugetgyro'] = function(block) {
  var dropdown_axis_selector = block.getFieldValue('axis_selector');
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".get_gyro" + dropdown_axis_selector + "()";
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_absoluteimugetheading'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("get heading from");
    this.appendValueInput("sensor")
        .setCheck("absoluteimu")
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(140);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_absoluteimugetheading'] = function(block) {
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".get_heading()";
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_absoluteimusetaccel'] = {
  init: function() {
    this.appendValueInput("sensor")
        .setCheck("absoluteimu")
        .appendField("set accelerometer sensitivity of");
    this.appendDummyInput()
        .appendField("to")
        .appendField(new Blockly.FieldDropdown([["2G", "2G"], ["4G", "4G"], ["8G", "8G"], ["16G", "16G"]]), "mode_selector");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(140);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_absoluteimusetaccel'] = function(block) {
  var dropdown_mode_selector = block.getFieldValue('mode_selector');
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".accel_" + dropdown_mode_selector + "()\n";
  return code;
};

Blockly.Blocks['sensors_absoluteimustartcmpscal'] = {
  init: function() {
    this.appendValueInput("sensor")
        .setCheck("absoluteimu")
        .appendField("start compass calibration of");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(140);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_absoluteimustartcmpscal'] = function(block) {
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".start_cmpscal()\n";
  return code;
};

Blockly.Blocks['sensors_absoluteimustopcmpscal'] = {
  init: function() {
    this.appendValueInput("sensor")
        .setCheck("absoluteimu")
        .appendField("stop compass calibration of");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(140);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_absoluteimustopcmpscal'] = function(block) {
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".stop_cmpscal()\n";
  return code;
};



Blockly.Blocks['sensors_sumoeyes'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("SumoEyes Sensor at")
        .appendField(new Blockly.FieldDropdown([["BAS1", "BAS1"], ["BAS2", "BAS2"], ["BBS1", "BBS1"], ["BBS2", "BBS2"]]), "sensor_selector");
    this.setInputsInline(true);
    this.setOutput(true, "sumoeyes");
    this.setColour(160);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_sumoeyes'] = function(block) {
  var dropdown_sensor_selector = block.getFieldValue('sensor_selector');
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  Blockly.Python.definitions_.import_MsDevices = "import MsDevices";
  Blockly.Python.definitions_["sumoeyes_" + dropdown_sensor_selector] = 'sumoeyes_' + dropdown_sensor_selector + ' = MsDevices.SumoEyes(psm.' + dropdown_sensor_selector + ')';
  var code = 'sumoeyes_' + dropdown_sensor_selector;
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_sumoeyesgetvalue'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("detect obstacle zone with");
    this.appendValueInput("sensor")
        .setCheck("sumoeyes")
    this.setInputsInline(true);
    this.setOutput(true, "String");
    this.setColour(160);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_sumoeyesgetvalue'] = function(block) {
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".detectObstactleZone(True)";
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_sumoeyessetmode'] = {
  init: function() {
    this.appendValueInput("sensor")
        .setCheck("sumoeyes")
        .appendField("set range of");
    this.appendDummyInput()
        .appendField("to")
        .appendField(new Blockly.FieldDropdown([["LONG_RANGE", "LONG_RANGE"], ["SHORT_RANGE", "SHORT_RANGE"]]), "mode_selector");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(160);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_sumoeyessetmode'] = function(block) {
  var dropdown_mode_selector = block.getFieldValue('mode_selector');
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".setRange(" + value_sensor + "." + dropdown_mode_selector + ")\n";
  return code;
};



Blockly.Blocks['sensors_lineleader'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("LineLeader-v2 Sensor at")
        .appendField(new Blockly.FieldDropdown([["BAS1", "BAS1"], ["BAS2", "BAS2"], ["BBS1", "BBS1"], ["BBS2", "BBS2"]]), "sensor_selector");
    this.setInputsInline(true);
    this.setOutput(true, "lineleader");
    this.setColour(180);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_lineleader'] = function(block) {
  var dropdown_sensor_selector = block.getFieldValue('sensor_selector');
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  Blockly.Python.definitions_.import_MsDevices = "import MsDevices";
  Blockly.Python.definitions_["lineleader_" + dropdown_sensor_selector] = 'lineleader_' + dropdown_sensor_selector + ' = MsDevices.LineLeader(psm.' + dropdown_sensor_selector + ')';
  var code = 'lineleader_' + dropdown_sensor_selector;
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_lineleadergetsteering'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("read the steering value from");
    this.appendValueInput("sensor")
        .setCheck("lineleader")
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(180);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_lineleadergetsteering'] = function(block) {
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".steering()";
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_lineleadergetaverage'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("read the average value of the current line from");
    this.appendValueInput("sensor")
        .setCheck("lineleader")
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(180);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_lineleadergetaverage'] = function(block) {
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".average()";
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_lineleadergetresult'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("read the 8 light sensor values as 1 bit from");
    this.appendValueInput("sensor")
        .setCheck("lineleader")
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(180);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_lineleadergetresult'] = function(block) {
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".result()";
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_lineleadergetrawcalibrated'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("read the 8 light sensor values as array from");
    this.appendValueInput("sensor")
        .setCheck("lineleader")
    this.setInputsInline(true);
    this.setOutput(true, "Array");
    this.setColour(180);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_lineleadergetrawcalibrated'] = function(block) {
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".ReadRaw_Calibrated()";
  return [code, Blockly.Python.ORDER_ATOMIC];
};



Blockly.Blocks['sensors_lsa'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("LightSensorArray Sensor at")
        .appendField(new Blockly.FieldDropdown([["BAS1", "BAS1"], ["BAS2", "BAS2"], ["BBS1", "BBS1"], ["BBS2", "BBS2"]]), "sensor_selector");
    this.setInputsInline(true);
    this.setOutput(true, "lsa");
    this.setColour(220);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_lsa'] = function(block) {
  var dropdown_sensor_selector = block.getFieldValue('sensor_selector');
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  Blockly.Python.definitions_.import_MsDevices = "import MsDevices";
  Blockly.Python.definitions_["lsa_" + dropdown_sensor_selector] = 'lsa_' + dropdown_sensor_selector + ' = MsDevices.LightSensorArray(psm.' + dropdown_sensor_selector + ')';
  var code = 'lsa_' + dropdown_sensor_selector;
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Blocks['sensors_lsagetrawcalibrated'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("read the 8 light sensor values as array from");
    this.appendValueInput("sensor")
        .setCheck("lsa")
    this.setInputsInline(true);
    this.setOutput(true, "Array");
    this.setColour(220);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['sensors_lsagetrawcalibrated'] = function(block) {
  var value_sensor = Blockly.Python.valueToCode(block, 'sensor', Blockly.Python.ORDER_ATOMIC);
  code = value_sensor + ".ReadRaw_Calibrated()";
  return [code, Blockly.Python.ORDER_ATOMIC];
};
