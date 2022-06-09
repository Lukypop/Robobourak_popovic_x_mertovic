speedFactor = 80
servo = PCAmotor.Servos.S1
pin_L = DigitalPin.P1
pin_R = DigitalPin.P14
pin_Trig = DigitalPin.P8
pin_Echo = DigitalPin.P15

whiteline = 0
connected = 0
start = False
last = 0

strip = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)
pins.set_pull(pin_L, PinPullMode.PULL_NONE)
pins.set_pull(pin_R, PinPullMode.PULL_NONE)
bluetooth.start_uart_service()
basic.show_string("S")

input.on_button_pressed(Button.A, robot_run)

def robot_run():
    global start 
    if start == True: 
        start = False
        print("stojim pane")
    else: 
        start = True
        print("jedu pane")
def motor_run(left = 0, right = 0, speed_factor = 80):
    PCAmotor.motor_run(PCAmotor.Motors.M2, Math.map(Math.constrain(-1 * left * (speedFactor / 100), -100, 100), -100, 100, -255, 255))
    PCAmotor.motor_run(PCAmotor.Motors.M3, Math.map(Math.constrain(right * (speedFactor / 100), -100, 100), -100, 100, -255, 255))

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
    global last
    #puvodni otaceni -12 150
    speed = 69
    reverse_speed = 0
    factor = 175
    obstacle_distance = sonar.ping(pin_Trig, pin_Echo, PingUnit.CENTIMETERS, 100)
    if start:

        l = False if (whiteline ^ pins.digital_read_pin(pin_L)) == 0 else True
        r = False if (whiteline ^ pins.digital_read_pin(pin_R)) == 0 else True

        #console.log_value("left", l)
        #console.log_value("right", r)
        #basic.pause(200)
        
        
        if l and r:
            motor_run(speed, speed, factor)
        elif l and not r:
            motor_run(speed, reverse_speed, factor)
            last = 0
        elif r and not l:
            motor_run(reverse_speed, speed, factor)
            last = 1
        else:
            if last == 0:
                motor_run(reverse_speed, speed, factor)
            else:
                motor_run(speed, reverse_speed, factor)    
    else:
        motor_run()
    basic.pause(32) #reakční frekvence 20 Hz
basic.forever(on_forever)