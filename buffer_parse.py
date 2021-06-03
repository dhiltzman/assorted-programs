#Buffer Management Parsing
#Author: David Hiltzman
#Date: 6/3/2021
#Buffer Management

#This is intended to parse a tsv into several tsvs so I can
#send tsvs to our vendors with their Part Numbers

#This file is heavily modeled after my accelerometer parsing program
import os, getpass, shutil
import sys
import math
import zipfile

the_desktop = os.path.join('C:\\Users',getpass.getuser(),'Desktop')
os.chdir(the_desktop)

#nested_folder = os.path.join('C:\\Users',getpass.getuser(),'Desktop', vibrator_name)
#os.makedirs(nested_folder)

print('Compiling..')

#with open('AccelA0_data.csv', 'w') as f:
    #f.write('Vendor,Name,Material,Vendor Material Number,Material Description,Planned Lead Times,UPDATED Lead Times,Comments\n')

with open('EXPORT.tsv', 'r') as f:
    for line in f:
        #print(line)
        #'\t' splits from the tabs
        #i chose a tsv instead of a csv bc there are commas in the descriptions
        split = line.split('\t')

        vendor = split[0]
        name = split[1]
        material = split[2]
        vendor_material = split[3]
        description = split[4]

        #PDT = Planned Delivery Time
        #Lead times in DAYS^
        planned_PDT = split[5]
        updated_PDT = split[6]
        comments = split[7]

        file_name = vendor + ' ' + name

        #If the file_name isn't the same as the previous Vendor Name creates a new file with the new file name
        #This SHOULD create a new file everytime a new vendor shows up.
        if (file_name != previous_name):
            with open('file_name.csv', 'w') as f:
                f.write('Vendor,Name,Material,Vendor Material Number,Material Description,Planned Lead Times,UPDATED Lead Times,Comments\n')
                print('New Vendor file added')

        #This allots the current name to become the previous name for the next loop
        previous_name = file_name
        print(file_name)
    
print('Complete!')

print('Cleaning Up...')

input('Press Enter to close the Program')
