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


print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))


''' 
-In-place sorting, used by the sort(), sorts the data then and replaces original order with the new order
-Copied sorting, used by sorted(), sorts the data then returns a sorted copy of the data, origial order is maintained


'''