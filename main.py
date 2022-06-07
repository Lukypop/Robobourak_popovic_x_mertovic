speedFactor = 80
pin_L = DigitalPin.P13
pin_R = DigitalPin.P14
pin_Trig = DigitalPin.P8
pin_Echo = DigitalPin.P15
whiteline = 1
connected = 0
strip = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)
pins.set_pull(pin_L, PinPullMode.PULL_NONE)
pins.set_pull(pin_R, PinPullMode.PULL_NONE)
bluetooth.start_uart_service()
basic.show_string("S")

# temporary code
motor_run(100, 100); basic.pause(2000)
motor_run(); basic.pause(300)
motor_run(-100, -100, 60); basic.pause(2000)
motor_run()

strip.set_pixel_color(0, neopixel.hsl(0, 50, 50)) # hmax = 360, smax = 100, lmax = 50
strip.set_pixel_color(3, neopixel.hsl(140, 100, 25))
strip.show()
# end of temporary code

def motor_run(left = 0, right = 0, speed_factor = 80):
    PCAmotor.motor_run(PCAmotor.Motors.M1, Math.map(Math.constrain(left * (speedFactor / 100), -100, 100), -100, 100, -255, 255))
    PCAmotor.motor_run(PCAmotor.Motors.M4, Math.map(Math.constrain(-1 * right * (speedFactor / 100), -100, 100), -100, 100, -255, 255))

def on_bluetooth_connected():
    global connected
    basic.show_icon(IconNames.HEART)
    connected = 1
    while connected == 1:
        uartData = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
        console.log_value("data", uartData)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    global connected
    basic.show_icon(IconNames.SAD)
    connected = 0
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_forever():
    obstacle_distance = sonar.ping(pin_Trig, pin_Echo, PingUnit.CENTIMETERS, 100)

    l = False if (whiteline ^ pins.digital_read_pin(pin_L)) == 0 else True
    r = False if (whiteline ^ pins.digital_read_pin(pin_R)) == 0 else True

    # TO DO ...

    basic.pause(50) #reakční frekvence 20 Hz
basic.forever(on_forever)