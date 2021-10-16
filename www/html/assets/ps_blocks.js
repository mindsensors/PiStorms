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
# August 2016    Roman Bohuk     Initial Authoring 
# October 2016   Seth Tenembaum  Add showMessage
# January 2017   Roman Bohuk     Add support for SumoEyes, LineLeader, LightSensorArray, and a bug fix 
*/



function hexToRgb(hex) {
    var shorthandRegex = /^#?([a-f\d])([a-f\d])([a-f\d])$/i;
    hex = hex.replace(shorthandRegex, function(m, r, g, b) {
        return r + r + g + g + b + b;
    });
    var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16)
    } : null;
}





// ------------------- MOTORS -------------------
Blockly.Blocks['motors_setspeed'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(Blockly.Msg.SET_SPEED_OF_MOTOR)
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

Blockly.Blocks['motors_brake'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(Blockly.Msg.SET_MOTOR)
        .appendField(new Blockly.FieldDropdown([["BAM1", "BAM1"], ["BAM2", "BAM2"], ["BBM1", "BBM1"], ["BBM2", "BBM2"]]), "motor_selector")
        .appendField(Blockly.Msg.TO_BRAKE);
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
        .appendField(Blockly.Msg.SET_MOTOR)
        .appendField(new Blockly.FieldDropdown([["BAM1", "BAM1"], ["BAM2", "BAM2"], ["BBM1", "BBM1"], ["BBM2", "BBM2"]]), "motor_selector")
        .appendField(Blockly.Msg.TO_FLOAT);
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
        .appendField(Blockly.Msg.SET_MOTOR)
        .appendField(new Blockly.FieldDropdown([["BAM1", "BAM1"], ["BAM2", "BAM2"], ["BBM1", "BBM1"], ["BBM2", "BBM2"]]), "motor_selector")
        .appendField(Blockly.Msg.TO_HOLD);
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

Blockly.Blocks['motors_getposition'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(Blockly.Msg.GET_POSITION_OF)
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
        .appendField(Blockly.Msg.RESET_POSITION_OF)
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

Blockly.Blocks['motors_syncspeed'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(Blockly.Msg.SYNC_SPEED_OF_BANK)
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
        .appendField(Blockly.Msg.FLOAT_BANK)
        .appendField(new Blockly.FieldDropdown([["A", "BAM1"], ["B", "BBM1"]]), "bank_selector")
        .appendField(Blockly.Msg.MOTORS);
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
        .appendField(Blockly.Msg.BRAKE_BANK)
        .appendField(new Blockly.FieldDropdown([["A", "BAM1"], ["B", "BBM1"]]), "bank_selector")
        .appendField(Blockly.Msg.MOTORS);
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

Blockly.Blocks['motors_waituntilnotbusy'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(Blockly.Msg.WAIT_UNTIL_MOTOR)
        .appendField(new Blockly.FieldDropdown([["BAM1", "BAM1"], ["BAM2", "BAM2"], ["BBM1", "BBM1"], ["BBM2", "BBM2"]]), "motor_selector")
        .appendField(Blockly.Msg.STOPS);
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

Blockly.Blocks['motors_runsecs'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(Blockly.Msg.RUN_MOTOR)
        .appendField(new Blockly.FieldDropdown([["BAM1", "BAM1"], ["BAM2", "BAM2"], ["BBM1", "BBM1"], ["BBM2", "BBM2"]]), "motor_selector");
    this.appendValueInput("TIME")
        .setCheck("Number")
        .appendField(Blockly.Msg.FOR);
    this.appendDummyInput()
        .appendField("seconds at speed");
    this.appendValueInput("SPEED")
        .setCheck("Number");
    this.appendDummyInput()
        .appendField(Blockly.Msg.AND)
        .appendField(new Blockly.FieldDropdown([["brake", "True"], ["don't brake", "False"]]), "brake_selector")
        .appendField(Blockly.Msg.WHEN_DONE);
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
        .appendField(Blockly.Msg.RUN_MOTOR)
        .appendField(new Blockly.FieldDropdown([["BAM1", "BAM1"], ["BAM2", "BAM2"], ["BBM1", "BBM1"], ["BBM2", "BBM2"]]), "motor_selector");
    this.appendValueInput("DEG")
        .setCheck("Number")
        .appendField("for");
    this.appendDummyInput()
        .appendField(Blockly.Msg.DEGREES_AT_SPEED);
    this.appendValueInput("SPEED")
        .setCheck("Number");
    this.appendDummyInput()
        .appendField(Blockly.Msg.AND)
        .appendField(new Blockly.FieldDropdown([["brake", "True"], ["hold", "hold"], ["don't brake", "False"]]), "brake_selector")
        .appendField(Blockly.Msg.WHEN_DONE);
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
        .appendField(Blockly.Msg.CHECK_IF_MOTOR)
        .appendField(new Blockly.FieldDropdown([["BAM1", "BAM1"], ["BAM2", "BAM2"], ["BBM1", "BBM1"], ["BBM2", "BBM2"]]), "motor_selector")
        .appendField(Blockly.Msg.IS_BUSY);
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
        .appendField(Blockly.Msg.CHECK_IF_MOTOR)
        .appendField(new Blockly.FieldDropdown([["BAM1", "BAM1"], ["BAM2", "BAM2"], ["BBM1", "BBM1"], ["BBM2", "BBM2"]]), "motor_selector")
        .appendField(Blockly.Msg.IS_STALLED);
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
        .appendField(Blockly.Msg.CHECK_IF_MOTOR)
        .appendField(new Blockly.FieldDropdown([["BAM1", "BAM1"], ["BAM2", "BAM2"], ["BBM1", "BBM1"], ["BBM2", "BBM2"]]), "motor_selector")
        .appendField(Blockly.Msg.IS_OVERLOADED);
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


Blockly.Blocks['motors_setparams'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(Blockly.Msg.SET_PERFORMANCE_PARAMETERS_FOR_BANK)
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

// ------------------- SYSTEM -------------------
Blockly.Blocks['system_sleep'] = {
  init: function() {
    this.appendValueInput("TIME")
        .setCheck("Number")
        .appendField(Blockly.Msg.PAUSE_FOR);
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

Blockly.Blocks['system_print'] = {
  init: function() {
    this.appendValueInput("TEXT")
        .setCheck(null)
        .appendField(Blockly.Msg.PRINT);
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

Blockly.Blocks['system_getbattery'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(Blockly.Msg.GET_BATTERY_VOLTAGE);
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

Blockly.Blocks['system_keypressed'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(Blockly.Msg.CHECK_IF_GO_BUTTON_IS_PRESSED);
    this.setInputsInline(true);
    this.setOutput(true, "Boolean");
    this.setColour(200);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['system_keypressed'] = function(block) {
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'bool(psm.isKeyPressed())';
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
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.getKeyPressCountx()';
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
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.resetKeyPressCount()\n';
  return code;
};


Blockly.Blocks['led_control'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("turn LED")
        .appendField(new Blockly.FieldDropdown([["1", "1"], ["2", "2"]]), "led_selector");
    this.appendDummyInput()
        .appendField("to color")
        .appendField(new Blockly.FieldColour("#ff0000"), "COLOR");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(140);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['led_control'] = function(block) {
  var dropdown_led_selector = block.getFieldValue('led_selector');
  var colour_color = block.getFieldValue('COLOR');
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var rgb = hexToRgb(colour_color);
  var code = 'psm.led(' + dropdown_led_selector + ', ' + rgb.r + ', ' + rgb.g + ', ' + rgb.b + ')\n';
  return code;
};









// Sensors

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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
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
  return [code, Blockly.Python.ORDER_NONE];
};




Blockly.Blocks['screen'] = {
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


Blockly.Blocks['screen_drawroundedrect'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("draw rounded rectangle");
    this.appendValueInput("x")
        .setCheck("Number")
        .appendField("X");
    this.appendValueInput("y")
        .setCheck("Number")
        .appendField("Y");
    this.appendValueInput("width")
        .setCheck("Number")
        .appendField("Width");
    this.appendValueInput("height")
        .setCheck("Number")
        .appendField("Height");
    this.appendValueInput("radius")
        .setCheck("Number")
        .appendField("Radius");
    this.appendDummyInput()
        .appendField("Filled with ")
        .appendField(new Blockly.FieldColour("#ff0000"), "COLOR")
        .appendField(" color");
    this.appendDummyInput()
        .appendField("Display on completion")
        .appendField(new Blockly.FieldCheckbox("TRUE"), "DISPLAY");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_drawroundedrect'] = function(block) {
  var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC);
  var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC);
  var value_width = Blockly.Python.valueToCode(block, 'width', Blockly.Python.ORDER_ATOMIC);
  var value_height = Blockly.Python.valueToCode(block, 'height', Blockly.Python.ORDER_ATOMIC);
  var value_radius = Blockly.Python.valueToCode(block, 'radius', Blockly.Python.ORDER_ATOMIC);
  var colour_color = block.getFieldValue('COLOR');
  var checkbox_display = block.getFieldValue('DISPLAY') == 'TRUE' ? 'True' : 'False';
  var rgb = hexToRgb(colour_color);
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.fillRoundRect(' + value_x + ', ' + value_y + ', ' + value_width + ', ' + value_height + ', ' + value_radius + ', (' + rgb.r + ', ' + rgb.g + ', ' + rgb.b + '), ' + checkbox_display + ')\n';
  return code;
};

Blockly.Blocks['screen_drawrect'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("draw rectangle");
    this.appendValueInput("x")
        .setCheck("Number")
        .appendField("X");
    this.appendValueInput("y")
        .setCheck("Number")
        .appendField("Y");
    this.appendValueInput("width")
        .setCheck("Number")
        .appendField("Width");
    this.appendValueInput("height")
        .setCheck("Number")
        .appendField("Height");
    this.appendDummyInput()
        .appendField("Filled with ")
        .appendField(new Blockly.FieldColour("#ff0000"), "COLOR")
        .appendField(" color");
    this.appendDummyInput()
        .appendField("Display on completion")
        .appendField(new Blockly.FieldCheckbox("TRUE"), "DISPLAY");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_drawrect'] = function(block) {
  var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC);
  var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC);
  var value_width = Blockly.Python.valueToCode(block, 'width', Blockly.Python.ORDER_ATOMIC);
  var value_height = Blockly.Python.valueToCode(block, 'height', Blockly.Python.ORDER_ATOMIC);
  var colour_color = block.getFieldValue('COLOR');
  var checkbox_display = block.getFieldValue('DISPLAY') == 'TRUE' ? 'True' : 'False';
  var rgb = hexToRgb(colour_color);
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.fillRect(' + value_x + ', ' + value_y + ', ' + value_width + ', ' + value_height + ', (' + rgb.r + ', ' + rgb.g + ', ' + rgb.b + '), display = ' + checkbox_display + ')\n';
  return code;
};
Blockly.Blocks['screen_drawcircle'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("draw circle");
    this.appendValueInput("x")
        .setCheck("Number")
        .appendField("X");
    this.appendValueInput("y")
        .setCheck("Number")
        .appendField("Y");
    this.appendValueInput("radius")
        .setCheck("Number")
        .appendField("Width");
    this.appendDummyInput()
        .appendField("Filled with ")
        .appendField(new Blockly.FieldColour("#ff0000"), "COLOR")
        .appendField(" color");
    this.appendDummyInput()
        .appendField("Display on completion")
        .appendField(new Blockly.FieldCheckbox("TRUE"), "DISPLAY");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_drawcircle'] = function(block) {
  var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC);
  var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC);
  var value_radius = Blockly.Python.valueToCode(block, 'radius', Blockly.Python.ORDER_ATOMIC);
  var colour_color = block.getFieldValue('COLOR');
  var checkbox_display = block.getFieldValue('DISPLAY') == 'TRUE' ? 'True' : 'False';
  var rgb = hexToRgb(colour_color);
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.fillCircle(' + value_x + ', ' + value_y + ', ' + value_radius + ', (' + rgb.r + ', ' + rgb.g + ', ' + rgb.b + '), display = ' + checkbox_display + ')\n';
  return code;
};

Blockly.Blocks['screen_drawbmp'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("draw image from file");
    this.appendValueInput("x")
        .setCheck("Number")
        .appendField("X");
    this.appendValueInput("y")
        .setCheck("Number")
        .appendField("Y");
    this.appendValueInput("width")
        .setCheck("Number")
        .appendField("Width");
    this.appendValueInput("height")
        .setCheck("Number")
        .appendField("Height");
    this.appendValueInput("location")
        .setCheck("String")
        .appendField("Path to image");
    this.appendDummyInput()
        .appendField("Display on completion")
        .appendField(new Blockly.FieldCheckbox("TRUE"), "DISPLAY");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_drawbmp'] = function(block) {
  var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC);
  var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC);
  var value_width = Blockly.Python.valueToCode(block, 'width', Blockly.Python.ORDER_ATOMIC);
  var value_height = Blockly.Python.valueToCode(block, 'height', Blockly.Python.ORDER_ATOMIC);
  var value_location = Blockly.Python.valueToCode(block, 'location', Blockly.Python.ORDER_ATOMIC);
  var checkbox_display = block.getFieldValue('DISPLAY') == 'TRUE' ? 'True' : 'False';
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.fillBmp(' + value_x + ', ' + value_y + ', ' + value_width + ', ' + value_height + ', path = ' + value_location + ', display = ' + checkbox_display + ')\n';
  return code;
};

Blockly.Blocks['screen_getwidthheight'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("get")
        .appendField(new Blockly.FieldDropdown([["width", "Width"], ["height", "Height"]]), "mode_selector")
        .appendField("of the screen");
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_getwidthheight'] = function(block) {
  var dropdown_mode_selector = block.getFieldValue('mode_selector');
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  code = "psm.screen.screen" + dropdown_mode_selector + "()";
  return [code, Blockly.Python.ORDER_NONE];
};


Blockly.Blocks['screen_drawtitle'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("display title");
    this.appendValueInput("TEXT")
        .setCheck("String")
        .appendField("Text");
    this.appendDummyInput()
        .appendField("Display on completion")
        .appendField(new Blockly.FieldCheckbox("TRUE"), "DISPLAY");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_drawtitle'] = function(block) {
  var value = Blockly.Python.valueToCode(block, 'TEXT', Blockly.Python.ORDER_ATOMIC);
  var checkbox_display = block.getFieldValue('DISPLAY') == 'TRUE' ? 'True' : 'False';
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.drawDisplay(' + value + ', ' + checkbox_display + ')\n';
  return code;
};
Blockly.Blocks['screen_clear'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("clear the screen");
    this.appendDummyInput()
        .appendField("Display on completion")
        .appendField(new Blockly.FieldCheckbox("TRUE"), "DISPLAY");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_clear'] = function(block) {
  var checkbox_display = block.getFieldValue('DISPLAY') == 'TRUE' ? 'True' : 'False';
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.clearScreen(' + checkbox_display + ')\n';
  return code;
};

Blockly.Blocks['screen_gettouchcoord'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("get")
        .appendField(new Blockly.FieldDropdown([["X", "X"], ["Y", "Y"]]), "mode_selector")
        .appendField("coordinate of touchscreen press");
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_gettouchcoord'] = function(block) {
  var dropdown_mode_selector = block.getFieldValue('mode_selector');
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  code = "psm.screen.TS_" + dropdown_mode_selector + "()";
  return [code, Blockly.Python.ORDER_NONE];
};
Blockly.Blocks['screen_rotate'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("rotate screen")
        .appendField(new Blockly.FieldDropdown([["left", "Left"], ["right", "Right"]]), "mode_selector")
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_rotate'] = function(block) {
  var dropdown_mode_selector = block.getFieldValue('mode_selector');
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  code = "psm.screen.rotate" + dropdown_mode_selector + "()\n";
  return code;
};

Blockly.Blocks['screen_istouched'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("is touched");
    this.setInputsInline(true);
    this.setOutput(true, "Boolean");
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_istouched'] = function(block) {
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  code = "psm.screen.isTouched()";
  return [code, Blockly.Python.ORDER_NONE];
};





Blockly.Blocks['screen_drawautotxt'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("draw text");
    this.appendValueInput("str")
        .setCheck("String")
        .appendField("Text");
    this.appendValueInput("x")
        .setCheck("Number")
        .appendField("X");
    this.appendValueInput("y")
        .setCheck("Number")
        .appendField("Y");
    this.appendValueInput("size")
        .setCheck("Number")
        .appendField("Size");
    this.appendDummyInput()
        .appendField("Fileld with ")
        .appendField(new Blockly.FieldColour("#ff0000"), "COLOR")
        .appendField(" color");
    this.appendDummyInput()
        .appendField("Display on completion")
        .appendField(new Blockly.FieldCheckbox("TRUE"), "DISPLAY");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_drawautotxt'] = function(block) {
  var value_str = Blockly.Python.valueToCode(block, 'str', Blockly.Python.ORDER_ATOMIC);
  var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC);
  var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC);
  var colour_color = block.getFieldValue('COLOR');
  var value_size = Blockly.Python.valueToCode(block, 'size', Blockly.Python.ORDER_ATOMIC);
  var checkbox_display = block.getFieldValue('DISPLAY') == 'TRUE' ? 'True' : 'False';
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var rgb = hexToRgb(colour_color);
  var code = 'psm.screen.drawAutoText(' + value_str + ', ' + value_x + ', ' + value_y + ', fill = (' + rgb.r + ', ' + rgb.g + ', ' + rgb.b + '), size = ' + value_size +  ', display = ' + checkbox_display + ')\n';
  return code;
};










Blockly.Blocks['terminal_printatline'] = {
  init: function() {
    this.appendValueInput("text")
        .appendField("print");
    this.appendValueInput("line")
        .setCheck("Number")
        .appendField("at line");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(200);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['terminal_printatline'] = function(block) {
  var value_text = Blockly.Python.valueToCode(block, 'text', Blockly.Python.ORDER_ATOMIC);
  var value_line = Blockly.Python.valueToCode(block, 'line', Blockly.Python.ORDER_ATOMIC);
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.termPrintAt(' + value_line + ', ' + value_text + ')\n';
  return code;
};

Blockly.Blocks['terminal_print'] = {
  init: function() {
    this.appendValueInput("text")
        .appendField("print");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(200);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['terminal_print'] = function(block) {
  var value_text = Blockly.Python.valueToCode(block, 'text', Blockly.Python.ORDER_ATOMIC);
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.termPrint(' + value_text + ')\n';
  return code;
};

Blockly.Blocks['terminal_println'] = {
  init: function() {
    this.appendValueInput("text")
        .appendField("print");
    this.appendDummyInput()
        .appendField("with newline");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(200);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['terminal_println'] = function(block) {
  var value_text = Blockly.Python.valueToCode(block, 'text', Blockly.Python.ORDER_ATOMIC);
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.termPrintln(' + value_text + ')\n';
  return code;
};

Blockly.Blocks['terminal_replacelastline'] = {
  init: function() {
    this.appendValueInput("text")
        .appendField("replace last line with");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(200);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['terminal_replacelastline'] = function(block) {
  var value_text = Blockly.Python.valueToCode(block, 'text', Blockly.Python.ORDER_ATOMIC);
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.termReplaceLastLine(' + value_text + ')\n';
  return code;
};

Blockly.Blocks['terminal_gotoline'] = {
  init: function() {
    this.appendValueInput("line")
        .setCheck("Number")
        .appendField("go to line");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(200);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['terminal_gotoline'] = function(block) {
  var value_line = Blockly.Python.valueToCode(block, 'line', Blockly.Python.ORDER_ATOMIC);
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.termGotoLine(' + value_line + ')\n';
  return code;
};

Blockly.Blocks['terminal_refreshline'] = {
  init: function() {
    this.appendValueInput("line")
        .setCheck("Number")
        .appendField("refresh line");
    this.appendDummyInput()
        .appendField("and ")
        .appendField(new Blockly.FieldCheckbox("TRUE"), "display")
        .appendField(" display");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(200);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['terminal_refreshline'] = function(block) {
  var value_line = Blockly.Python.valueToCode(block, 'line', Blockly.Python.ORDER_ATOMIC);
  var checkbox_display = block.getFieldValue('display') == 'TRUE';
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.refreshLine(' + value_line + ', ' + checkbox_display + ')\n';
  return code;
};


Blockly.Blocks['screen_askyesnoquestion'] = {
  init: function() {
    this.appendValueInput("text")
        .setCheck("String")
        .appendField("ask a yes/no question");
    this.setInputsInline(true);
    this.setOutput(true, "Boolean");
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_askyesnoquestion'] = function(block) {
  var value_text = Blockly.Python.valueToCode(block, 'text', Blockly.Python.ORDER_ATOMIC);
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.askYesOrNoQuestion([' + value_text + '])';
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Blocks['screen_showmessage'] = {
  init: function() {
    this.appendValueInput("text")
        .setCheck("String")
        .appendField("show message");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_showmessage'] = function(block) {
  var value_text = Blockly.Python.valueToCode(block, 'text', Blockly.Python.ORDER_ATOMIC);
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.showMessage([' + value_text + '])\n';
  return code;
};








Blockly.Blocks['screen_refresh'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("refresh the screen")
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_refresh'] = function(block) {
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.refresh()\n';
  return code;
};




Blockly.Blocks['screen_drawbutton'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("draw button");
    this.appendValueInput("x")
        .setCheck("Number")
        .appendField("X");
    this.appendValueInput("y")
        .setCheck("Number")
        .appendField("Y");
    this.appendValueInput("width")
        .setCheck("Number")
        .appendField("Width");
    this.appendValueInput("height")
        .setCheck("Number")
        .appendField("Height");
    this.appendValueInput("text")
        .setCheck("String")
        .appendField("Text");
    this.appendDummyInput()
        .appendField("Display on completion")
        .appendField(new Blockly.FieldCheckbox("TRUE"), "DISPLAY");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};
Blockly.Python['screen_drawbutton'] = function(block) {
  var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC);
  var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC);
  var value_width = Blockly.Python.valueToCode(block, 'width', Blockly.Python.ORDER_ATOMIC);
  var value_height = Blockly.Python.valueToCode(block, 'height', Blockly.Python.ORDER_ATOMIC);
  var value_location = Blockly.Python.valueToCode(block, 'text', Blockly.Python.ORDER_ATOMIC);
  var checkbox_display = block.getFieldValue('DISPLAY') == 'TRUE' ? 'True' : 'False';
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.drawButton(' + value_x + ', ' + value_y + ', ' + value_width + ', ' + value_height + ', text = ' + value_location + ', display = ' + checkbox_display + ', align="xcenter")\n';
  return code;
};

Blockly.Blocks['screen_checkbutton'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("check button");
    this.appendValueInput("x")
        .setCheck("Number")
        .appendField("X");
    this.appendValueInput("y")
        .setCheck("Number")
        .appendField("Y");
    this.appendValueInput("width")
        .setCheck("Number")
        .appendField("Width");
    this.appendValueInput("height")
        .setCheck("Number")
        .appendField("Height");
    this.setInputsInline(false);
    this.setOutput(true, "Boolean");
    this.setColour(300);
    this.setTooltip('');
    this.setHelpUrl('https://www.mindsensors.com/forum');
  }
};

Blockly.Python['screen_checkbutton'] = function(block) {
  var value_x = Blockly.Python.valueToCode(block, 'x', Blockly.Python.ORDER_ATOMIC);
  var value_y = Blockly.Python.valueToCode(block, 'y', Blockly.Python.ORDER_ATOMIC);
  var value_width = Blockly.Python.valueToCode(block, 'width', Blockly.Python.ORDER_ATOMIC);
  var value_height = Blockly.Python.valueToCode(block, 'height', Blockly.Python.ORDER_ATOMIC);
  Blockly.Python.definitions_.from_PiStorms_import_PiStorms = "from PiStorms import PiStorms";
  Blockly.Python.definitions_.psm_PiStorms = "psm = PiStorms()";
  var code = 'psm.screen.checkButton(' + value_x + ', ' + value_y + ', ' + value_width + ', ' + value_height + ')';
  return [code, Blockly.Python.ORDER_NONE];
};


// Reference
// pause for https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#kib8fq
// set speed of motor https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#t9v9id
// get position of https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#4f7nyh
// send to log https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#tsudab
// runsecs https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#pynd89
// set performace parameters https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#duebh9

// nxt touch at https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#5xqcdm
