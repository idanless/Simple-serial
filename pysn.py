import serial
import datetime
ser = serial.Serial('/dev/ttyUSB0',115200)

f = open('dataFile.txt','a')

while 1 :
    f.write('\n')
    f.write(str(datetime.datetime.now())+'\t'+str(ser.readline().decode("utf-8")))
    f.close()
    f = open('outputfile.txt','a')
