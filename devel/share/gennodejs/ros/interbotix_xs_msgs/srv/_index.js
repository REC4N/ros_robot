
"use strict";

let OperatingModes = require('./OperatingModes.js')
let Reboot = require('./Reboot.js')
let MotorGains = require('./MotorGains.js')
let TorqueEnable = require('./TorqueEnable.js')
let RobotInfo = require('./RobotInfo.js')
let RegisterValues = require('./RegisterValues.js')

module.exports = {
  OperatingModes: OperatingModes,
  Reboot: Reboot,
  MotorGains: MotorGains,
  TorqueEnable: TorqueEnable,
  RobotInfo: RobotInfo,
  RegisterValues: RegisterValues,
};
