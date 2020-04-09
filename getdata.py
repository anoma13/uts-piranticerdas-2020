import serial

print("Running UNO")

arduino = serial.Serial("/dev/ttyUSB0", timeout=1, baudrate=9600)

while True:
	a = arduino.readline().decode("utf-8").strip('\n').strip('\r')
	if(a!=''):
		temp = a.split(';')
		print(temp[0]+";"+temp[1]+";"+temp[2])
