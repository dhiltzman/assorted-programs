#Accelerometer Parsing Data
#Author: David Hiltzman

import os, getpass, shutil
import sys
import math

the_desktop = os.path.join('C:\\Users',getpass.getuser(),'Desktop')
os.chdir(the_desktop)

vibrator_name = input('Input a name for the accelerometer test (Model and Test #): ')

print('Compiling A0.')
with open('AccelA0_data.csv', 'w') as f:
    f.write('Accelerometer,X-Accel,Y-Accel,Z-Accel,Magnitude\n')

with open('sensors.txt', 'r') as f:
    #A0: -5.34,-5.99,5.58,4908
    for line in f:
        #print('Inside For Loop')
        
        #Accelerometer Title
        split1 = line.split(':')
        accel_type = split1[0].strip()

        if (accel_type == 'A0'):
            split2 = split1[1].split(',')
            x_accel = split2[0].strip()
            x_squared = float(x_accel) ** 2
        
            y_accel = split2[1].strip()
            y_squared = float(y_accel) ** 2
        
            z_accel = split2[2].strip()
            z_squared = float(z_accel) ** 2

            #Computing the Magnitude
            magnitude = math.sqrt(float(x_squared) + float(y_squared) + float(z_squared))

            full_data = accel_type + ',' + x_accel + ',' + y_accel + ',' + z_accel + ',' + str(magnitude) + '\n'
        
            with open('AccelA0_data.csv', 'a') as f:
                f.write(full_data)
    
print('A0 Complete!')

#A1
print('Compiling A1.')
with open('AccelA1_data.csv', 'w') as f:
    f.write('Accelerometer,X-Accel,Y-Accel,Z-Accel,Magnitude\n')

with open('sensors.txt', 'r') as f:
    #A0: -5.34,-5.99,5.58,4908
    for line in f:
        #print('Inside For Loop')
        
        #Accelerometer Title
        split1 = line.split(':')
        accel_type = split1[0].strip()

        if (accel_type == 'A1'):
            split2 = split1[1].split(',')
            x_accel = split2[0].strip()
            x_squared = float(x_accel) ** 2
        
            y_accel = split2[1].strip()
            y_squared = float(y_accel) ** 2
        
            z_accel = split2[2].strip()
            z_squared = float(z_accel) ** 2

            #Computing the Magnitude
            magnitude = math.sqrt(float(x_squared) + float(y_squared) + float(z_squared))

            full_data = accel_type + ',' + x_accel + ',' + y_accel + ',' + z_accel + ',' + str(magnitude) + '\n'
        
            with open('AccelA1_data.csv', 'a') as f:
                f.write(full_data)
    
print('A1 Complete!')

#A2
print('Compiling A2.')
with open('AccelA2_data.csv', 'w') as f:
    f.write('Accelerometer,X-Accel,Y-Accel,Z-Accel,Magnitude\n')

with open('sensors.txt', 'r') as f:
    #A0: -5.34,-5.99,5.58,4908
    for line in f:
        #print('Inside For Loop')
        
        #Accelerometer Title
        split1 = line.split(':')
        accel_type = split1[0].strip()

        if (accel_type == 'A2'):
            split2 = split1[1].split(',')
            x_accel = split2[0].strip()
            x_squared = float(x_accel) ** 2
        
            y_accel = split2[1].strip()
            y_squared = float(y_accel) ** 2
        
            z_accel = split2[2].strip()
            z_squared = float(z_accel) ** 2

            #Computing the Magnitude
            magnitude = math.sqrt(float(x_squared) + float(y_squared) + float(z_squared))

            full_data = accel_type + ',' + x_accel + ',' + y_accel + ',' + z_accel + ',' + str(magnitude) + '\n'
        
            with open('AccelA2_data.csv', 'a') as f:
                f.write(full_data)
    
print('A2 Complete!')

#A3
print('Compiling A3.')
with open('AccelA3_data.csv', 'w') as f:
    f.write('Accelerometer,X-Accel,Y-Accel,Z-Accel,Magnitude\n')

with open('sensors.txt', 'r') as f:
    #A0: -5.34,-5.99,5.58,4908
    for line in f:
        #print('Inside For Loop')
        
        #Accelerometer Title
        split1 = line.split(':')
        accel_type = split1[0].strip()

        if (accel_type == 'A3'):
            split2 = split1[1].split(',')
            x_accel = split2[0].strip()
            x_squared = float(x_accel) ** 2
        
            y_accel = split2[1].strip()
            y_squared = float(y_accel) ** 2
        
            z_accel = split2[2].strip()
            z_squared = float(z_accel) ** 2

            #Computing the Magnitude
            magnitude = math.sqrt(float(x_squared) + float(y_squared) + float(z_squared))

            full_data = accel_type + ',' + x_accel + ',' + y_accel + ',' + z_accel + ',' + str(magnitude) + '\n'
        
            with open('AccelA3_data.csv', 'a') as f:
                f.write(full_data)
    
print('A3 Complete!')

print('Cleaning Up...')
#cleaning up by zipping the two files, and removing the directory
os.chdir(the_desktop)
new_zip = zipfile.ZipFile(vibrator_name + '.zip', 'w')
new_zip.write('AccelA0_data.csv', compress_type=zipfile.ZIP_DEFLATED)
new_zip.write('AccelA1_data.csv', compress_type=zipfile.ZIP_DEFLATED)
new_zip.write('AccelA2_data.csv', compress_type=zipfile.ZIP_DEFLATED)
new_zip.write('AccelA3_data.csv', compress_type=zipfile.ZIP_DEFLATED)
new_zip.close()

print('Zip file complete!')
input()
