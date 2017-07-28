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

<category name="Motors" colour="240">
  <block type="motors_setspeed">
    <value name="SPEED">
      <shadow type="math_number">
        <field name="NUM">50</field>
      </shadow>
    </value>
  </block>

  <block type="motors_getposition"></block>

  <block type="motors_resetposition"></block>

  <block type="motors_brake"></block>

  <block type="motors_float"></block>

  <block type="motors_hold"></block>

  <block type="motors_syncspeed">
    <value name="SPEED">
      <shadow type="math_number">
        <field name="NUM">50</field>
      </shadow>
    </value>
  </block>

  <block type="motors_syncfloat"></block>

  <block type="motors_syncbrake"></block>

  <block type="motors_runsecs">
    <value name="SPEED">
      <shadow type="math_number">
        <field name="NUM">50</field>
      </shadow>
    </value>
    <value name="TIME">
      <shadow type="math_number">
        <field name="NUM">3</field>
      </shadow>
    </value>
  </block>

  <block type="motors_rundegrees">
    <value name="SPEED">
      <shadow type="math_number">
        <field name="NUM">50</field>
      </shadow>
    </value>
    <value name="DEG">
      <shadow type="math_number">
        <field name="NUM">180</field>
      </shadow>
    </value>
  </block>

  <block type="motors_isbusy"></block>

  <block type="motors_isstalled"></block>

  <block type="motors_isoverloaded"></block>

  <block type="motors_waituntilnotbusy"></block>

  <block type="motors_setparams">
    <value name="Kp_tacho">
      <shadow type="math_number">
        <field name="NUM">6</field>
      </shadow>
    </value>
    <value name="Ki_tacho">
      <shadow type="math_number">
        <field name="NUM">0</field>
      </shadow>
    </value>
    <value name="Kd_tacho">
      <shadow type="math_number">
        <field name="NUM">0</field>
      </shadow>
    </value>
    <value name="Kp_speed">
      <shadow type="math_number">
        <field name="NUM">1</field>
      </shadow>
    </value>
    <value name="Ki_speed">
      <shadow type="math_number">
        <field name="NUM">0</field>
      </shadow>
    </value>
    <value name="Kd_speed">
      <shadow type="math_number">
        <field name="NUM">0</field>
      </shadow>
    </value>
    <value name="passcount">
      <shadow type="math_number">
        <field name="NUM">10</field>
      </shadow>
    </value>
    <value name="tolerance">
      <shadow type="math_number">
        <field name="NUM">5</field>
      </shadow>
    </value>
  </block>

</category>



<script>
Blockly.Blocks['motors_setspeed'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("set speed of motor")
        .appendField(new Blockly.FieldDropdown([["BAM1", "BAM1"], ["BAM2", "BAM2"], ["BBM1", "BBM1"], ["BBM2", "BBM2"]]), "motor_selector");
    this.appendValueInput("SPEED")
        .setCheck("Number")
        .appendField("to");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(240);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['motors_setspeed'] = function(block) {
  var dropdown_motor_selector = block.getFieldValue('motor_selector');
  var value_speed = Blockly.Python.valueToCode(block, 'SPEED', Blockly.Python.ORDER_ATOMIC);
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.'+ dropdown_motor_selector + '.setSpeed(' + value_speed + ')\n';
  return code;
};


Blockly.Blocks['motors_getposition'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("get position of")
        .appendField(new Blockly.FieldDropdown([["BAM1", "BAM1"], ["BAM2", "BAM2"], ["BBM1", "BBM1"], ["BBM2", "BBM2"]]), "motor_selector");
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(240);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['motors_getposition'] = function(block) {
  var dropdown_motor_selector = block.getFieldValue('motor_selector');
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.'+ dropdown_motor_selector + '.pos()';
  return [code, Blockly.Python.ORDER_NONE];
};


Blockly.Blocks['motors_resetposition'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("reset position of")
        .appendField(new Blockly.FieldDropdown([["BAM1", "BAM1"], ["BAM2", "BAM2"], ["BBM1", "BBM1"], ["BBM2", "BBM2"]]), "motor_selector");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(240);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['motors_resetposition'] = function(block) {
  var dropdown_motor_selector = block.getFieldValue('motor_selector');
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.'+ dropdown_motor_selector + '.resetPos()\n';
  return code;
};


Blockly.Blocks['motors_brake'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("set motor")
        .appendField(new Blockly.FieldDropdown([["BAM1", "BAM1"], ["BAM2", "BAM2"], ["BBM1", "BBM1"], ["BBM2", "BBM2"]]), "motor_selector")
        .appendField("to brake");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(240);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['motors_brake'] = function(block) {
  var dropdown_motor_selector = block.getFieldValue('motor_selector');
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.'+ dropdown_motor_selector + '.brake()\n';
  return code;
};


Blockly.Blocks['motors_float'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("set motor")
        .appendField(new Blockly.FieldDropdown([["BAM1", "BAM1"], ["BAM2", "BAM2"], ["BBM1", "BBM1"], ["BBM2", "BBM2"]]), "motor_selector")
        .appendField("to float");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(240);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['motors_float'] = function(block) {
  var dropdown_motor_selector = block.getFieldValue('motor_selector');
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.'+ dropdown_motor_selector + '.float()\n';
  return code;
};


Blockly.Blocks['motors_hold'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("set motor")
        .appendField(new Blockly.FieldDropdown([["BAM1", "BAM1"], ["BAM2", "BAM2"], ["BBM1", "BBM1"], ["BBM2", "BBM2"]]), "motor_selector")
        .appendField("to hold");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(240);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['motors_hold'] = function(block) {
  var dropdown_motor_selector = block.getFieldValue('motor_selector');
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.'+ dropdown_motor_selector + '.hold()\n';
  return code;
};


Blockly.Blocks['motors_syncspeed'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("sync speed of bank")
        .appendField(new Blockly.FieldDropdown([["A", "BAM1"], ["B", "BBM1"]]), "bank_selector");
    this.appendValueInput("SPEED")
        .setCheck("Number")
        .appendField("motors to");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(240);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['motors_syncspeed'] = function(block) {
  var dropdown_bank_selector = block.getFieldValue('bank_selector');
  var value_speed = Blockly.Python.valueToCode(block, 'SPEED', Blockly.Python.ORDER_ATOMIC);
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.'+ dropdown_bank_selector + '.setSpeedSync(' + value_speed + ')\n';
  return code;
};


Blockly.Blocks['motors_syncfloat'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("float bank")
        .appendField(new Blockly.FieldDropdown([["A", "BAM1"], ["B", "BBM1"]]), "bank_selector")
        .appendField("motors");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(240);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['motors_syncfloat'] = function(block) {
  var dropdown_bank_selector = block.getFieldValue('bank_selector');
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.'+ dropdown_bank_selector + '.floatSync()\n';
  return code;
};


Blockly.Blocks['motors_syncbrake'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("brake bank")
        .appendField(new Blockly.FieldDropdown([["A", "BAM1"], ["B", "BBM1"]]), "bank_selector")
        .appendField("motors");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(240);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['motors_syncbrake'] = function(block) {
  var dropdown_bank_selector = block.getFieldValue('bank_selector');
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.'+ dropdown_bank_selector + '.brakeSync()\n';
  return code;
};


Blockly.Blocks['motors_runsecs'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("run motor")
        .appendField(new Blockly.FieldDropdown([["BAM1", "BAM1"], ["BAM2", "BAM2"], ["BBM1", "BBM1"], ["BBM2", "BBM2"]]), "motor_selector");
    this.appendValueInput("TIME")
        .setCheck("Number")
        .appendField("for");
    this.appendDummyInput()
        .appendField("seconds at speed");
    this.appendValueInput("SPEED")
        .setCheck("Number");
    this.appendDummyInput()
        .appendField("and")
        .appendField(new Blockly.FieldDropdown([["brake", "True"], ["don't brake", "False"]]), "brake_selector")
        .appendField("when done");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(240);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['motors_runsecs'] = function(block) {
  var dropdown_motor_selector = block.getFieldValue('motor_selector');
  var value_time = Blockly.Python.valueToCode(block, 'TIME', Blockly.Python.ORDER_ATOMIC);
  var value_speed = Blockly.Python.valueToCode(block, 'SPEED', Blockly.Python.ORDER_ATOMIC);
  var dropdown_brake_selector = block.getFieldValue('brake_selector');
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.'+ dropdown_motor_selector + '.runSecs(' + value_time + ', ' + value_speed + ', ' + dropdown_brake_selector + ')\n';
  return code;
};


Blockly.Blocks['motors_rundegrees'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("run motor")
        .appendField(new Blockly.FieldDropdown([["BAM1", "BAM1"], ["BAM2", "BAM2"], ["BBM1", "BBM1"], ["BBM2", "BBM2"]]), "motor_selector");
    this.appendValueInput("DEG")
        .setCheck("Number")
        .appendField("for");
    this.appendDummyInput()
        .appendField("degrees at speed");
    this.appendValueInput("SPEED")
        .setCheck("Number");
    this.appendDummyInput()
        .appendField("and")
        .appendField(new Blockly.FieldDropdown([["brake", "True"], ["hold", "hold"], ["don't brake", "False"]]), "brake_selector")
        .appendField("when done");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(240);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['motors_rundegrees'] = function(block) {
  var dropdown_motor_selector = block.getFieldValue('motor_selector');
  var value_deg = Blockly.Python.valueToCode(block, 'DEG', Blockly.Python.ORDER_ATOMIC);
  var value_speed = Blockly.Python.valueToCode(block, 'SPEED', Blockly.Python.ORDER_ATOMIC);
  var b = block.getFieldValue('brake_selector');
  b = (b == "True") ? "True, False" : ((b == "hold") ? "False, False" : "False, False");
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.'+ dropdown_motor_selector + '.runDegs(' + value_deg + ', ' + value_speed + ', ' + b + ')\n';
  return code;
};


Blockly.Blocks['motors_isbusy'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("check if motor")
        .appendField(new Blockly.FieldDropdown([["BAM1", "BAM1"], ["BAM2", "BAM2"], ["BBM1", "BBM1"], ["BBM2", "BBM2"]]), "motor_selector")
        .appendField("is busy");
    this.setInputsInline(true);
    this.setOutput(true, "Boolean");
    this.setColour(240);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['motors_isbusy'] = function(block) {
  var dropdown_motor_selector = block.getFieldValue('motor_selector');
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.'+ dropdown_motor_selector + '.isBusy()';
  return [code, Blockly.Python.ORDER_NONE];
};


Blockly.Blocks['motors_isstalled'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("check if motor")
        .appendField(new Blockly.FieldDropdown([["BAM1", "BAM1"], ["BAM2", "BAM2"], ["BBM1", "BBM1"], ["BBM2", "BBM2"]]), "motor_selector")
        .appendField("is stalled");
    this.setInputsInline(true);
    this.setOutput(true, "Boolean");
    this.setColour(240);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['motors_isstalled'] = function(block) {
  var dropdown_motor_selector = block.getFieldValue('motor_selector');
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.'+ dropdown_motor_selector + '.isStalled()';
  return [code, Blockly.Python.ORDER_NONE];
};


Blockly.Blocks['motors_isoverloaded'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("check if motor")
        .appendField(new Blockly.FieldDropdown([["BAM1", "BAM1"], ["BAM2", "BAM2"], ["BBM1", "BBM1"], ["BBM2", "BBM2"]]), "motor_selector")
        .appendField("is overloaded");
    this.setInputsInline(true);
    this.setOutput(true, "Boolean");
    this.setColour(240);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['motors_isoverloaded'] = function(block) {
  var dropdown_motor_selector = block.getFieldValue('motor_selector');
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.'+ dropdown_motor_selector + '.isOverloaded()';
  return [code, Blockly.Python.ORDER_NONE];
};


Blockly.Blocks['motors_waituntilnotbusy'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("wait until motor")
        .appendField(new Blockly.FieldDropdown([["BAM1", "BAM1"], ["BAM2", "BAM2"], ["BBM1", "BBM1"], ["BBM2", "BBM2"]]), "motor_selector")
        .appendField("stops");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(240);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['motors_waituntilnotbusy'] = function(block) {
  var dropdown_bank_selector = block.getFieldValue('motor_selector');
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.'+ dropdown_bank_selector + '.waitUntilNotBusy()\n';
  return code;
};


Blockly.Blocks['motors_setparams'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("set performance parameters for bank")
        .appendField(new Blockly.FieldDropdown([["A", "BAM1"], ["B", "BBM1"]]), "motor_selector");
    this.appendValueInput("Kp_tacho")
        .setCheck("Number")
        .appendField("Proportional-gain of the encoder position");
    this.appendValueInput("Ki_tacho")
        .setCheck("Number")
        .appendField("Integral-gain of the encoder position");
    this.appendValueInput("Kd_tacho")
        .setCheck("Number")
        .appendField("Derivative-gain of the encoder position");
    this.appendValueInput("Kp_speed")
        .setCheck("Number")
        .appendField("Proportional-gain of the speed");
    this.appendValueInput("Ki_speed")
        .setCheck("Number")
        .appendField("Integral-gain of the speed");
    this.appendValueInput("Kd_speed")
        .setCheck("Number")
        .appendField("Derivative-gain of the speed");
    this.appendValueInput("passcount")
        .setCheck("Number")
        .appendField("# of times the encoder should be within tolerance");
    this.appendValueInput("tolerance")
        .setCheck("Number")
        .appendField("The tolerance (in ticks) for encoder positioning");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(240);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['motors_setparams'] = function(block) {
  var dropdown_motor_selector = block.getFieldValue('motor_selector');
  var value_kp_tacho = Blockly.Python.valueToCode(block, 'Kp_tacho', Blockly.Python.ORDER_ATOMIC);
  var value_ki_tacho = Blockly.Python.valueToCode(block, 'Ki_tacho', Blockly.Python.ORDER_ATOMIC);
  var value_kd_tacho = Blockly.Python.valueToCode(block, 'Kd_tacho', Blockly.Python.ORDER_ATOMIC);
  var value_kp_speed = Blockly.Python.valueToCode(block, 'Kp_speed', Blockly.Python.ORDER_ATOMIC);
  var value_ki_speed = Blockly.Python.valueToCode(block, 'Ki_speed', Blockly.Python.ORDER_ATOMIC);
  var value_kd_speed = Blockly.Python.valueToCode(block, 'Kd_speed', Blockly.Python.ORDER_ATOMIC);
  var value_passcount = Blockly.Python.valueToCode(block, 'passcount', Blockly.Python.ORDER_ATOMIC);
  var value_tolerance = Blockly.Python.valueToCode(block, 'tolerance', Blockly.Python.ORDER_ATOMIC);
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.'+ dropdown_motor_selector + '.SetPerformanceParameters(' + value_kp_tacho + ', ' + value_ki_tacho + ', ' + value_kd_tacho + ', ' + value_kp_speed + ', ' + value_ki_speed + ', ' + value_kd_speed + ', ' + value_passcount + ', ' + value_tolerance + ')\n';
  return code;
};
</script>
