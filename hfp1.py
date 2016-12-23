#hfp1
#idle usage Pro-Tips
#Alt-P - recalls the last code statement
#Alt-N - quickly moves to the next code statement

#using a for loop to iterate over each item in a list, better than using a while loop
for i in listX
    print(i)

#Identifiers can only start with a letter or _

if condtion:
    #the true contition holds
else:
    #the false case occurs

	#printing nested list items
for each_item in movies1:
    if isinstance(each_item, list):
        for eb in each_item:
            print(eb)
    else:
        print(each_item)

#BIF - Build in function
#help(BIF), displays a description of the provided built in function

#isinstance(each_item, list), you muar provide an object and a type (class or tuple) to check for. 
#^ like asking is this object a list -> return T or F 

#dir(__builtins__) - displays all available built in fuctions

#function template
def funcName(arg0,arg1):
    #code to execute on provided parameters, indentation matters! blocked based on indentation are called Suite's

#recursive function to process each item in a list
def listProc(listA):
    for each_item in listA:
        if isinstance(each_item, list):
            listProc(each_item)
        else:
            print(each_item)
			
#Python 3 limits it's recursion limit to 1000 times
