#Code to read in a list of domains and output for TRAC and Splunk
import re
import sys

list = []

def dedupe(dees): 
   # order preserving
   checked = []
   for e in dees:
       if e not in checked:
           checked.append(e)
   return checked


def slack(a):
    print("******************* TRAC *******************	//\(oo)/\\ ")
    for each_line in a:
        print(each_line + ', ',end='')
    print('\n')
   
def splunk(b):
    print("******************* Splunk *******************^8^")
    print("\'web_traffic\' ", end='')
    for each_line in b:
        print('\"'+ each_line +"\" OR ", end='')
    print('\n')

def noHyper(c):
    print("******************* No Hyerlinks *******************=^..^=")
    for each_line in c:
        print (each_line.replace(".", "[.]"))
        
      
   
try:
    data = open('domains.txt')
    for each_line in data:
        each_line.strip() #removes whitespace
        #each_line.strip("http:\/\/") # removes http:\\ if present
        #each_line.strip("https:\/\/") # removes http:\\ if present
        #each_line.strip("www.") #removes leading www. if present
        #print(each_line)
        result = re.search('\\b(?:[0-9]{1,3}\\.){3}[0-9]{1,3}\\b',each_line)
        if result == None:
            result = re.search('[a-zA-Z0-9\-\.]+',each_line)
            if result != None:
                list.append(result.group(0))
            else:
                print("Error Parsing Object")
        #result = re.search('[a-zA-Z0-9\-\.]+',each_line)#searches for a domain or IP
        #print(result.group(0))
        list.append(result.group(0))    
    data.close()
except IOError:
    print('The datafile is missing!')
    
list = dedupe(list)
slack(list)
splunk(list)
noHyper(list)

    
    
    
    
    
