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

print(james)
print(julie)
print(mikey)
print(sarah)