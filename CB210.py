import serial

ser = serial.Serial(port='COM4', baudrate=115200, timeout=1)

statusLed = ''
loopCondition = True

print('Start LED control Loop')

while loopCondition:
    print('LED ON  = 1\n'+'LED OFF = 0\n'+'Quit loop = 2')
    statusLed = input('Type which you want: ')
    if statusLed == '0':
        ser.write(b'LED OFF')
        print(ser.readline())
    elif statusLed == '1':
        ser.write(b'LED ON')
        print(ser.readline())
    elif statusLed == '2':
        loopCondition = False
