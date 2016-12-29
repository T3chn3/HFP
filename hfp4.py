'''
man=[]
other=[]

try:
    data = open('sketch.txt')
    
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
                
            elif role == 'Other Man':
                other.append(line_spoken)
          
        except ValueError: 
            pass

    data.close()
except IOError:
    print('The data file is missing!')

#print(man)
#print(other)
out = open("out.txt",'w') #defining out ouput object thats setup to write to

print("this is only a test", file = out)
print(man, file = out)
print("this is only a test01", file = out)
print( other, file = out)
print("this is only a test02", file = out)
out.close()
'''
''' 
Rules of writing

When you use access mode w, Python opens your named file
for writing. If the file already exists, it is cleared of its contents, or clobbered.
 To append to a file, use access mode a, and to open a file for writing and reading 
 (without clobbering), use w+. If you try to open a file for writing that does not 
 already exist, it is first created for you, and then opened for writing.
 '''
 
 
 #Final code, Opened an external file, read the data, sorted the contents, wrote the output to a set of external files. 
 #uses try/except/finally pattern
import os
 
man = []
other = []

def listProc(listA, level=0,indent=False, outFH = sys.stdout):
    for each_item in listA:
        if isinstance(each_item, list):
            listProc(each_item, level +1,indent, outFH)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end='', file=outFH)
            print(each_item, file=outFH)

try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':',1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile is missing!')
    
try:
    man_file=open('man_data.txt','w')
    other_file=open('other_data.txt','w')
    
    listProc(man)
    listProc(other)
    
    #print(man,file=man_file)
    #print(other,file=other_file)
    
except IOError:
    print('File error')
finally:
    man_file.close()
    other_file.close()
   








