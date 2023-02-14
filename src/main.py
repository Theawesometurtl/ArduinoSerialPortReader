import serial
import time
from socketIO import sendMessage
 
sendMessage('hi, this is from another file')
ser = serial.Serial('COM4', 9800, timeout=1)
time.sleep(2)
f = open("data.js", "w+") 

for i in range(1):
    # Reading all bytes available bytes till EOL
    line = ser.readline() 
    if line:
        # Converting Byte Strings into unicode strings
        try:
            string = str(line.decode("utf-8"))
        except UnicodeDecodeError:
            string = str(line.decode("utf-8"))
         #Converting Unicode String into integer
         
        
        f.write("""thing.innerHTML = "%s" """ % string)
        print(string)
 
ser.close()
f.close()