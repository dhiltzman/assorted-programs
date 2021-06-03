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

folder_name = input('Please enter a folder name to save files in: ')

folder = os.path.join('C:\\Users',getpass.getuser(),'Desktop', folder_name)

if os.path.exists(folder) == True:
    print('Path already exists')
    print()
elif os.path.exists(folder) == False:
    print('Path does not exist')
    os.makedirs(folder)
    print('Path created')
    print()
else:
    print('something went wrong')
    print()

print('Compiling..')
print('Please wait.')

with open('EXPORT.tsv', 'r') as f:
    #Declaring var for comparision
    previous_name = ''
    line_number = 0
    for line in f:
        #print(line)
        #'\t' splits from the tabs
        #i chose a tsv instead of a csv bc there are commas in the descriptions
        split = line.split('\t')

        vendor = split[0]
        name = split[1]

        if (name.startswith('"')):
            name = name[1:-1]
            
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

        os.chdir(folder)

        #Skips first line
        if (file_name == 'Vendor Name'):
            continue
        #Creates a new file if not found
        if (file_name != previous_name):
            with open(file_name + '.tsv', 'w') as f:
                f.write('Vendor \t Name \t Material \t Vendor Material Number \t Material Description \t Planned Lead Times \t UPDATED Lead Times \t Comments\n')
                #print('New Vendor file added')
        #Writes line to csv 
        elif (file_name == previous_name):
            full_data = vendor + '\t' + name + '\t' + material + '\t' + vendor_material + '\t' + description + '\t' + planned_PDT + '\t' + updated_PDT + '\t' + comments
            with open(file_name + '.tsv', 'a') as f:
                #print(full_data)
                f.write(full_data)
                #print('Write line complete')
        #This allots the current name to become the previous name for the next loop
        previous_name = file_name
        line_number = line_number + 1

        #print('Line Number: ' + str(line_number))
        #print(file_name)
    
print('Complete!')

input('Press Enter to close the Program')
