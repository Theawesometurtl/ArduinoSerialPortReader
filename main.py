import serial
import time
 
ser = serial.Serial('COM3', 9800, timeout=1)
time.sleep(2)
f = open("Data.txt", "w+") 

for i in range(50):
    # Reading all bytes available bytes till EOL
    line = ser.readline() 
    if line:
        # Converting Byte Strings into unicode strings
        print(line)
        try:
            string = line.decode('utf-8')
        except UnicodeDecodeError:
            string = line.decode('utf-8') 
        # Converting Unicode String into integer
         
        
        f.write(string, "/n")
        print(string)
 
ser.close()
f.close()