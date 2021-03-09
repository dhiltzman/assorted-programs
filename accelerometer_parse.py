#Accelerometer Parsing Data
#Author: David Hiltzman

import os, getpass, shutil
import sys
import math

the_desktop = os.path.join('C:\\Users',getpass.getuser(),'Desktop')
os.chdir(the_desktop)

with open('accelerometer_data.csv', 'w') as f:
    f.write('Accelerometer,X-Accel,Y-Accel,Z-Accel,Magnitude\n')

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
        x_squared = float(x_accel) ** 2
        
        y_accel = split2[1].strip()
        y_squared = float(y_accel) ** 2
        
        z_accel = split2[2].strip()
        z_squared = float(z_accel) ** 2
        #print(split2)

        #Computing the Magnitude
        magnitude = math.sqrt(float(x_squared) + float(y_squared) + float(z_squared))
        #print(magnitude)
