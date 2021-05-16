from smbus import SMBus
import time

address = 0x8#bus address
bus = SMBus(1) #which i2c ports are used. Raspberry pi i2c -1 ports are used.


for i in range(0,10): #sends data back and forth
    data = bus.read_byte(address) #read the data from arduino
    print("data sent from arduino is : %02d" %data) #prints data recived
    time.sleep(1)
    if (2 <int(data)<4): #example temperature data is 3c then raspberry pi prints temperature is low
        print("Temperature is : LOW 3C")
    if(6<int(data)<8): #example temprature data is 7 raspberry pi prints HIGH
        print("Temperature is : HIGH 7C")
time.sleep(1)





