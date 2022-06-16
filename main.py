speedFactor = 80
speed = 70
pin_L = DigitalPin.P8
pin_R = DigitalPin.P1
pin_Trig = DigitalPin.P15
pin_Echo = DigitalPin.P12

whiteline = 0
connected = 0
start = False
uartData = "0"
lock = False

pins.set_pull(pin_L, PinPullMode.PULL_NONE)
pins.set_pull(pin_R, PinPullMode.PULL_NONE)
bluetooth.start_uart_service()
basic.show_string("S")

def start_it():
    global start
    if start == True: 
        start = False
    else: start = True

def motor_run(left = 0, right = 0, speed_factor = 80):
    PCAmotor.motor_run(PCAmotor.Motors.M2, Math.map(Math.constrain(-1 * left * (speedFactor / 100), -100, 100), -100, 100, -255, 255))
    PCAmotor.motor_run(PCAmotor.Motors.M3, Math.map(Math.constrain(right * (speedFactor / 100), -100, 100), -100, 100, -255, 255))

def on_bluetooth_connected():
    global connected, uartData, lock
    basic.show_icon(IconNames.HEART)
    connected = 1 
    while connected == 1:
        uartData = str(bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH)))
        print(uartData)
        if uartData == "B1":
            motor_run(speed, -speed, speedFactor)
            basic.pause(888)
        elif uartData == "B2": motor_run()
        elif uartData == "B3": start_it()
        if start:
            lock = True
            console.log_value("start", uartData)
            if uartData == "0": lock = False
            elif uartData == "A": motor_run(speed, speed, speedFactor)
            elif uartData == "B": motor_run(-speed, -speed, speedFactor)
            elif uartData == "C": motor_run(-speed, speed, speedFactor)
            elif uartData == "D": motor_run(speed, -speed, speedFactor)
            
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    global connected
    basic.show_icon(IconNames.SAD)
    connected = 0
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def main():
    reverse_speed = -12
    factor = 75
    last = 0
    if start and not lock:    
        l = False if (whiteline ^ pins.digital_read_pin(pin_L)) == 0 else True
        r = False if (whiteline ^ pins.digital_read_pin(pin_R)) == 0 else True
        if l and r:
            motor_run(speed, speed, factor)
        elif l and not r:
            motor_run(speed, reverse_speed, factor)
            last = 0
        elif r and not l:
            motor_run(reverse_speed, speed, factor)
            last = 1
        else:
            if last == 0: motor_run(reverse_speed, speed, factor)
            else: motor_run(speed, reverse_speed, factor)
    basic.pause(10) #reakční frekvence 20 Hz
basic.forever(main)            
