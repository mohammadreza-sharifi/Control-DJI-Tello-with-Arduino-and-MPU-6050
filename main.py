import easytello as tello
import serial
import time

arduino = serial.Serial(port='COM9', baudrate=115200, timeout=.1)

drone = tello.Tello()

while True:

    cmd = arduino.readline()
    print(cmd)
    if cmd == b't\r\n':
        drone.takeoff()
    elif cmd == b'c\r\n':
        drone.land()
    elif cmd == b'f\r\n':
        drone.forward(40)
    elif cmd == b'b\r\n':
        drone.back(40)
    elif cmd == b'r\r\n':
        drone.right(40)
    elif cmd == b'l\r\n':
        drone.left(40)
    elif cmd == b'u\r\n':
        drone.up(40)
    elif cmd == b'd\r\n':
        drone.down(40)
    elif cmd == b'p\r\n':
        drone.cw(90)
    elif cmd == b'o\r\n':
        drone.ccw(90)
    else:
        pass