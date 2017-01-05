
c_james=[]
c_julie=[]
c_mikey=[]
c_sarah=[]

#Sanitize() 
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'     
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)


with open('james.txt') as jaf:
    data=jaf.readline()
james=data.strip().split(',') #example of method chaining, methods are applied from left to right 


with open('julie.txt') as juf:
    data=juf.readline()
julie=data.strip().split(',')

with open('mikey.txt') as mif:
    data=mif.readline()
mikey=data.strip().split(',')

with open('sarah.txt') as saf:
    data=saf.readline()
sarah=data.strip().split(',')


for each_i in james:
    c_james.append(sanitize(each_i))
    
for each_i in sarah:
    c_sarah.append(sanitize(each_i))

for each_i in julie:
    c_julie.append(sanitize(each_i))

for each_i in mikey:
    c_mikey.append(sanitize(each_i))    

print('James')
print(sorted(james)) #add the reverse=True flag to sort in decending order
print(sorted(c_james))

print("Julie")
print(sorted(julie))
print(sorted(c_julie))

print("Mikey")
print(sorted(mikey))
print(sorted(c_mikey))

print("Sarah")
print(sorted(sarah))
print(sorted(c_sarah))



''' 
-In-place sorting, used by the sort(), sorts the data then and replaces original order with the new order
-Copied sorting, used by sorted(), sorts the data then returns a sorted copy of the data, origial order is maintained
-method chaining is read from left to right
-fuction chaining is read from right to left

-This is a good example of input->sanitize->process->output pattern
-Lots of duplication going on there. Next section covers List Comprehension to reduce code duplication
'''

#list comprehension
#the above function in a single line
#new list  transformation   to each item  in an existing list
c_mikey = [sanitize(each_t) for each_t in mikey] #the append() is implied

#other examples
'''
min =[1,2,3]
secs=[m * 60 for m in min]

print(secs) -> [60,120,180] 

'''

print(sorted([sanitize(t) for t in julie]))

#remove duplates in a list, and return the top 3 values

''' 
sequence = ['1', '2', '3', '3', '6', '4', '5', '6']
unique = []
[unique.append(item) for item in sequence if item not in unique]
'''

mikey = sorted([sanitize(t)for t in mikey])
unique = []
[unique.append(i) for i in mikey if i not in unique]
print('mikey\'s top values' + str(unique[0:3]))

sarah = sorted([sanitize(t)for t in sarah])
unique = []
[unique.append(i) for i in sarah if i not in unique]
print('sarah\'s top values' + str(unique[0:3]))

julie = sorted([sanitize(t)for t in julie])
unique = []
[unique.append(i) for i in julie if i not in unique]
print('julie\'s top values' + str(unique[0:3]))

#using sets can be a much easier way to remove dupes

distances = set() #factory function 
distances = {10.6,10,11,10.6,"two",7,7.1,8.1,8.1}
'''
A function factory is a function used to make new data items of a particular type.
set(), creates a new set with the supplied parameteres.
'''

distances = set(james) #since distances is defined as a set, all dupes in james will be ignored and not placed in distances

#All this code can be reduced to using the sorted(set())[0:3]

#post code review suggestions

def get_coach_data(filename):
    try:
        open(filename) as f:
            data=f.readline()
        return(data.strip().split(','))
    except IOError as ioerr
        print('File Error' + str(ioerr))
        return(None)
#calling the function 
sarah = get_coach_data('sarah.txt')

