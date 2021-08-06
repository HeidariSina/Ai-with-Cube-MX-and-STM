import serial

data[10]

ser = serial.Serial(	port="COM4", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
ser.open()
for i in range (10)
    ser.write(data[i])
    sleep(1)
ser.close()
