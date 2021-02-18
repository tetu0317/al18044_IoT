import serial
import datetime
import requests

ser = serial.Serial('/dev/ttyACM0',9600,timeout = 10)
data = {}

#最初で受信するデータは値がおかしいので無視
is_first = True

while True:
    now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M')
    lux = ser.raadline().decode('utf-8').splitlines()
    data['time'] = now
    data['lux'] = lux

    if is_first:
        is_first = False
    else:
        print(data)
        response = requests.post('https://160.16.210.86:18044/lux',data = data)
        print(response)

ser.close()