#Accelerometer Parsing Data
#Author: David Hiltzman

import os, getpass, zipfile, shutil
import sys

the_desktop = os.path.join('C:\\Users',getpass.getuser(),'Desktop')
os.chdir(the_desktop)

with open('accelerometer_data.csv', 'w') as f:
    f.write('Accelerometer,X-Accel,Y-Accel,Z-Accel\n')

with open('sensors.txt', 'r') as f:
    #A0: -5.34,-5.99,5.58,4908
    for line in f:
        #print('Inside For Loop')
        
        #Accelerometer Title
        split1 = line.split(':')
        #print(split1)
        accel_type = split1[0].strip()

        split2 = split1[1].split(',')
        x_accel = split2[0].strip()
        y_accel = split2[1].strip()
        z_accel = split2[2].strip()
        print(split2)
