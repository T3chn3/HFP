#Simple script to ingest my list of email senders, sourced from Ironport and output a Splunk search.

import re
import sys

list1 = []
list2 = []

#try:

#read in my file
data = open("Stripper.txt")

for each_line in data:
    each_line.strip() #removes whitespace
    result = re.search('@[a-zA-Z0-9\-\.]+',each_line)
    #print(result.group(0))#prints what the regex matched on
    list1.append(each_line) #adds the current line
    list2.append(result.group(0)) #adds the stripped email domain
            
#except FileNotFoundError:
#    print("The data file is missing!")
    
#print(list1)
#print(list2)

#Parse the stripped list and build the search
print("index=\"ironport\" \"", end='') #Start of search, you still need to add the timeframe

for each_line in list2:
    print(each_line, end='')
    print ("\" OR \"", end='')
    
