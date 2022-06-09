let speedFactor = 80
let servo = PCAmotor.Servos.S1
let pin_L = DigitalPin.P1
let pin_R = DigitalPin.P14
let pin_Trig = DigitalPin.P8
let pin_Echo = DigitalPin.P15
let whiteline = 0
let connected = 0
let start = false
let last = 0
let strip = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)
pins.setPull(pin_L, PinPullMode.PullNone)
pins.setPull(pin_R, PinPullMode.PullNone)
bluetooth.startUartService()
basic.showString("S")
input.onButtonPressed(Button.A, function robot_run() {
    
    if (start == true) {
        start = false
        console.log("stojim pane")
    } else {
        start = true
        console.log("jedu pane")
    }
    
})
function motor_run(left: number = 0, right: number = 0, speed_factor: number = 80) {
    PCAmotor.MotorRun(PCAmotor.Motors.M2, Math.map(Math.constrain(-1 * left * (speedFactor / 100), -100, 100), -100, 100, -255, 255))
    PCAmotor.MotorRun(PCAmotor.Motors.M3, Math.map(Math.constrain(right * (speedFactor / 100), -100, 100), -100, 100, -255, 255))
}

bluetooth.onBluetoothConnected(function on_bluetooth_connected() {
    let uartData: string;
    
    basic.showIcon(IconNames.Heart)
    connected = 1
    while (connected == 1) {
        uartData = bluetooth.uartReadUntil(serial.delimiters(Delimiters.Hash))
        console.logValue("data", uartData)
    }
})
bluetooth.onBluetoothDisconnected(function on_bluetooth_disconnected() {
    
    basic.showIcon(IconNames.Sad)
    connected = 0
})
// reakční frekvence 20 Hz
basic.forever(function on_forever() {
    let l: any;
    let r: any;
    
    // puvodni otaceni -12 150
    let speed = 69
    let reverse_speed = 0
    let factor = 175
    let obstacle_distance = sonar.ping(pin_Trig, pin_Echo, PingUnit.Centimeters, 100)
    if (start) {
        l = (whiteline ^ pins.digitalReadPin(pin_L)) == 0 ? false : true
        r = (whiteline ^ pins.digitalReadPin(pin_R)) == 0 ? false : true
        // console.log_value("left", l)
        // console.log_value("right", r)
        // basic.pause(200)
        if (l && r) {
            motor_run(speed, speed, factor)
        } else if (l && !r) {
            motor_run(speed, reverse_speed, factor)
            last = 0
        } else if (r && !l) {
            motor_run(reverse_speed, speed, factor)
            last = 1
        } else if (last == 0) {
            motor_run(reverse_speed, speed, factor)
        } else {
            motor_run(speed, reverse_speed, factor)
        }
        
    } else {
        motor_run()
    }
    
    basic.pause(32)
})
