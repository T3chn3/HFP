
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

