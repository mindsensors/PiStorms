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
  <sep gap="50"></sep>
  <block type="servo_setPos"></block>
  <block type="servo_setSpeed"></block>
  <block type="servo_stop"></block>
  <sep gap="50"></sep>
  <block type="servo_setNeutralPoint"></block>
  <block type="servo_setNeutral"></block>

  <sep gap="100"></sep>

  <block type="servo_setPulse"></block>
  <sep gap="50"></sep>
  <block type="servo_setPos_value"></block>
  <block type="servo_setSpeed_value"></block>
  <block type="servo_setPulse_value"></block>
</category>



<script>
function makeBlock(identifier, parameters, generateCode) {
    Blockly.Blocks[identifier] = {init: parameters};
    Blockly.Python[identifier] = generateCode;
}


makeBlock('servo_init',
    function() {
        this.appendDummyInput()
            .appendField("servo at")
            .appendField(new Blockly.FieldDropdown(["BBS1","BBS2","BBS3","BAS3","BAS2","BAS1"].map(p=>[p,p])), "port")
        this.setInputsInline(true);
        this.setOutput(true, "RCServo");
        this.setColour(230);
        this.setTooltip("Represents a servo plugged in to a specific port.");
        this.setHelpUrl("http://www.mindsensors.com/reference/PiStorms/html/class_pi_storms_grx_1_1_pi_storms_grx.html");
    },
    function(block) {
        var port = block.getFieldValue('port');
        Blockly.Python.definitions_.import_RCServo = "from PiStorms_GRX import RCServo";
        Blockly.Python.definitions_[`servo_${port}`] = `servo_${port} = RCServo("${port}")`;
        return [`servo_${port}`, Blockly.Python.ORDER_ATOMIC];
    }
);


makeBlock('servo_setPos',
    function() {
        this.appendValueInput("servo")
            .setCheck("RCServo")
            .appendField("move servo")
        this.appendDummyInput()
            .appendField("to position")
            .appendField(new Blockly.FieldNumber(90, 0, 180, 1), "pos")
        this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(230);
        this.setTooltip("Move a (regular) servo to a position. The position can be between 0 and 180 degrees. This should match your physical servo.");
        this.setHelpUrl("http://www.mindsensors.com/reference/PiStorms/html/class_pi_storms_grx_1_1_pi_storms_grx.html");
    },
    function(block) {
        var servo = Blockly.Python.valueToCode(block, 'servo', Blockly.Python.ORDER_ATOMIC);
        var pos = block.getFieldValue('pos');
        return `${servo}.setPos(${pos})\n`;
    }
);


makeBlock('servo_setSpeed',
    function() {
        this.appendValueInput("servo")
            .setCheck("RCServo")
            .appendField("set servo")
        this.appendDummyInput()
            .appendField("'s speed to")
            .appendField(new Blockly.FieldNumber(50, -100, 100, 1), "speed")
        this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(230);
        this.setTooltip("Set a continuous rotation servo to a speed from -100 (reverse) to 100 (forwards). If your servo moves even when set to 0 speed (\"drifting\"), be sure to run the calibration program in the 45-Utils folder!");
        this.setHelpUrl("http://www.mindsensors.com/reference/PiStorms/html/class_pi_storms_grx_1_1_pi_storms_grx.html");
    },
    function(block) {
        var servo = Blockly.Python.valueToCode(block, 'servo', Blockly.Python.ORDER_ATOMIC);
        var speed = block.getFieldValue('speed');
        return `${servo}.setSpeed(${speed})\n`;
    }
);


makeBlock('servo_stop',
    function() {
        this.appendValueInput("servo")
            .setCheck("RCServo")
            .appendField("stop servo")
        this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(230);
        this.setTooltip("No matter what, stop sending a pulse to this servo. Even if a continuous rotation servo does not have its neutral point set correctly, this will still stop it.");
        this.setHelpUrl("http://www.mindsensors.com/reference/PiStorms/html/class_pi_storms_grx_1_1_pi_storms_grx.html");
    },
    function(block) {
        var servo = Blockly.Python.valueToCode(block, 'servo', Blockly.Python.ORDER_ATOMIC);
        return `${servo}.stop()\n`;
    }
);


makeBlock('servo_setNeutralPoint',
    function() {
        this.appendValueInput("servo")
            .setCheck("RCServo")
            .appendField("set")
        this.appendDummyInput()
            .appendField("'s neutral point to")
            .appendField(new Blockly.FieldNumber(1500, 500, 2500, 1), "neutralPoint")
        this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(230);
        this.setTooltip("Set the standard (resting) pulse for this servo. See the tooltip for \"set pulse\" for more details. The neutral point should be 1500, but all servos vary slightly when they are manufactured. For instance, your servo might still spin when set to 1500, but 1680 is the actual \"middle\".");
        this.setHelpUrl("http://www.mindsensors.com/reference/PiStorms/html/class_pi_storms_grx_1_1_pi_storms_grx.html");
    },
    function(block) {
        var servo = Blockly.Python.valueToCode(block, 'servo', Blockly.Python.ORDER_ATOMIC);
        var neutralPoint = block.getFieldValue('neutralPoint');
        return `${servo}.setNeutralPoint(${neutralPoint})\n`;
    }
);


makeBlock('servo_setNeutral',
    function() {
        this.appendValueInput("servo")
            .setCheck("RCServo")
            .appendField("move")
        this.appendDummyInput()
            .appendField("to its neutral position")
        this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(230);
        this.setTooltip("Return this servo to its neutral position. This should move normal servos to the middle, and stop continuous rotation servos.");
        this.setHelpUrl("http://www.mindsensors.com/reference/PiStorms/html/class_pi_storms_grx_1_1_pi_storms_grx.html");
    },
    function(block) {
        var servo = Blockly.Python.valueToCode(block, 'servo', Blockly.Python.ORDER_ATOMIC);
        return `${servo}.setNeutral()\n`;
    }
);


makeBlock('servo_setPulse',
    function() {
        this.appendValueInput("servo")
            .setCheck("RCServo")
            .appendField("set")
        this.appendDummyInput()
            .appendField("'s pulse to")
            .appendField(new Blockly.FieldNumber(1500, 500, 2500, 1), "pulse")
            .appendField("microseconds")
        this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(230);
        this.setTooltip("This is more low-level, most people won't have to (or want to) use this. You can set the number of microseconds between pulses sent to this servo. 500 is the minimum, 2500 is the maximum. 1500 should be the median, but read the tooltip for \"set neutral position\".");
        this.setHelpUrl("http://www.mindsensors.com/reference/PiStorms/html/class_pi_storms_grx_1_1_pi_storms_grx.html");
    },
    function(block) {
        var servo = Blockly.Python.valueToCode(block, 'servo', Blockly.Python.ORDER_ATOMIC);
        var pulse = block.getFieldValue('pulse');
        return `${servo}.setPulse(${pulse})\n`;
    }
);


makeBlock('servo_setPos_value',
    function() {
        this.appendValueInput("servo")
            .setCheck("RCServo")
            .appendField("move servo")
        this.appendDummyInput()
            .appendField("to position")
        this.appendValueInput("pos")
            .setCheck("Number")
        this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(230);
        this.setTooltip("Move a (regular) servo to a position. The position can be between 0 and 180 degrees. This should match your physical servo.\n\nCareful! The position input isn't checked. Make sure it is between 0 and 180, or the program will crash.");
        this.setHelpUrl("http://www.mindsensors.com/reference/PiStorms/html/class_pi_storms_grx_1_1_pi_storms_grx.html");
    },
    function(block) {
        var servo = Blockly.Python.valueToCode(block, 'servo', Blockly.Python.ORDER_ATOMIC);
        var pos = Blockly.Python.valueToCode(block, 'pos', Blockly.Python.ORDER_ATOMIC);
        return `${servo}.setPos(${pos})\n`;
    }
);


makeBlock('servo_setSpeed_value',
    function() {
        this.appendValueInput("servo")
            .setCheck("RCServo")
            .appendField("set servo")
        this.appendDummyInput()
            .appendField("'s speed to")
        this.appendValueInput("speed")
            .setCheck("Number")
        this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(230);
        this.setTooltip("Set a continuous rotation servo to a speed from -100 (reverse) to 100 (forwards). If your servo moves even when set to 0 speed (\"drifting\"), be sure to run the calibration program in the 45-Utils folder.\n\nCareful! The speed input isn't checked. Make sure it is between -100 and 100, or the program will crash.");
        this.setHelpUrl("http://www.mindsensors.com/reference/PiStorms/html/class_pi_storms_grx_1_1_pi_storms_grx.html");
    },
    function(block) {
        var servo = Blockly.Python.valueToCode(block, 'servo', Blockly.Python.ORDER_ATOMIC);
        var speed = Blockly.Python.valueToCode(block, 'speed', Blockly.Python.ORDER_ATOMIC);
        return `${servo}.setSpeed(${speed})\n`;
    }
);


makeBlock('servo_setPulse_value',
    function() {
        this.appendValueInput("servo")
            .setCheck("RCServo")
            .appendField("set")
        this.appendValueInput("pulse")
            .setCheck("Number")
            .appendField("'s pulse to")
        this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(230);
        this.setTooltip("This is more low-level, most people won't have to (or want to) use this. You can set the number of microseconds between pulses sent to this servo. 500 is the minimum, 2500 is the maximum. 1500 should be the median, but read the tooltip for \"set neutral position\".\n\nCareful! The pulse input isn't checked. Make sure it is between 500 and 2500, or the program will crash.");
        this.setHelpUrl("http://www.mindsensors.com/reference/PiStorms/html/class_pi_storms_grx_1_1_pi_storms_grx.html");
    },
    function(block) {
        var servo = Blockly.Python.valueToCode(block, 'servo', Blockly.Python.ORDER_ATOMIC);
        var pulse = Blockly.Python.valueToCode(block, 'pulse', Blockly.Python.ORDER_ATOMIC);
        return `${servo}.setPulse(${pulse})\n`;
    }
);
</script>
