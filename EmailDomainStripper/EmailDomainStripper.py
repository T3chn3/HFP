#Simple script to ingest my list of email senders, sourced from Ironport and format the list for TRAC/Exchange searches

import re
import sys

list1 = []

try:
#read in my file
    data = open("Stripper.txt")

    for each_line in data:
        each_line.strip() #removes whitespace
        result = re.search('@[a-zA-Z0-9\-\.]+',each_line)#matches on email domain
        list1.append(each_line[0:result.start()]) #adds the current bun to list
            
except FileNotFoundError:
    print("The data file is missing!")

print('***************** Exchange Format *****************')
print("******************** d[ o_0 ]b ********************"+ "\n")
for each_line in list1:
    print(each_line, end='\n')

print("https://scrypture.cirt.ibechtel.com/s/query_ad" + "\n")   
    
print('***************** TRAC Format *****************' + "\n")
for each_line in list1:
    print(each_line + ", ", end='')
  
