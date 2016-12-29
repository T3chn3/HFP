'''
input-process-output model
reading data from an external source

Basic Pattern
the_file = open("Ransome.txt")
#Do something with the data  #processing
#in "the_file".              #processing
the_file.close()

to read each line use
the_file.readline(), end='' #store a single line in memory
use print to display each line
print(the_file.readline(), end='')

use seek(0) to restart the current line in the buffer to 0, the first line
use tell() to return the current position of the file read/write pointer within the file.
close() method of a file object flushes any unwritten information and closes the file object, after which no more writing can be done.

'''
data4 = open('Ransom.txt')
for each_line in data4:
    if not each_line.find(':') == -1:
        (role, line_spoken) = each_line.split(':',1)
        print(role, end='')
        print(' said: ', end='')
        print(line_spoken, end='')
    else
        
data4.close()

''' 
Adding more logic increases complexity

Changes to the input will cause updates to the code.

Error handling - 

traceback: a notification that something has gone wrong during runtime, detailed description of what occured

You may catch an exception and ignore it or run some code to attempt to recover from the error

Try first then recover pattern
Normal Flow -> Python tries the code -> everyhing works out 

Exception flow -> Python tries your code, but fails -> CRASH -> your code recovery code executes -> your exception is handled -> code continues


pass keyword is the same as NULL value
 '''
 #Same code as above with Try/Catch exceptions implemented
  ''' 
 try:
    code that may cause an error
 except:
    your error-recovery code
    
    Dont focus on trying to handle every possible error case
  '''
  
#the pass just skips the line with the error
data = open('Ransom.txt')

for each_line in data:
	try:
	    (role, line_spoken) = each_line.split(':', 1) 
	    print(role, end='')
	    print(' said: ', end='')
	    print(line_spoken, end='')
	except:
		pass
    
data.close()

#this code will skip the lines that caused the ValueError Traceback, but not the file IOError for the initial file missing.

import os

if os.path.exist('Ransom.txt'):
    data = open('Ransom.txt')
    
    for each_line in data:
        if not each_line.find(':') == -1:
            (role, line_spoken) = each_line.split(':', 1) 
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except:
            pass
    data.close()
    
else:
    print('The Data file is missing!')
    
#^ not the best method

''' By using Python’s exception-handling mechanism, you get to concentrate on what your code 
needs to do, as opposed to worrying about what can go wrong and writing extra code to avoid 
runtime errors. '''

#The final code, also specifies the type of Error to pass on, all other will still be flagged at runtime
try:
    data = open('Ransom.txt')
    
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except ValueError: 
            pass

    data.close()
except IOError:
    print('The data file is missing!')