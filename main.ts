let speedFactor = 80
let pin_L = DigitalPin.P13
let pin_R = DigitalPin.P14
let pin_Trig = DigitalPin.P8
let pin_Echo = DigitalPin.P15
let whiteline = 1
let connected = 0
let strip = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)
pins.setPull(pin_L, PinPullMode.PullNone)
pins.setPull(pin_R, PinPullMode.PullNone)
bluetooth.startUartService()
basic.showString("S")
//  temporary code
motor_run(100, 100)
basic.pause(2000)
motor_run()
basic.pause(300)
motor_run(-100, -100, 60)
basic.pause(2000)
motor_run()
strip.setPixelColor(0, neopixel.hsl(0, 50, 50))
//  hmax = 360, smax = 100, lmax = 50
strip.setPixelColor(3, neopixel.hsl(140, 100, 25))
strip.show()
//  end of temporary code
function motor_run(left: number = 0, right: number = 0, speed_factor: number = 80) {
    PCAmotor.MotorRun(PCAmotor.Motors.M1, Math.map(Math.constrain(left * (speedFactor / 100), -100, 100), -100, 100, -255, 255))
    PCAmotor.MotorRun(PCAmotor.Motors.M4, Math.map(Math.constrain(-1 * right * (speedFactor / 100), -100, 100), -100, 100, -255, 255))
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
    let obstacle_distance = sonar.ping(pin_Trig, pin_Echo, PingUnit.Centimeters, 100)
    let l = (whiteline ^ pins.digitalReadPin(pin_L)) == 0 ? false : true
    let r = (whiteline ^ pins.digitalReadPin(pin_R)) == 0 ? false : true
    //  TO DO ...
    basic.pause(50)
})
