#making the code better

#cleaning up the input values
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'     
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs) 
    
#reading in the coaches data    
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data=f.readline()
        temp1 = data.strip().split(',')
        return({'Name' : temp1.pop(0), 'dob' : temp1.pop(0), 'Times' : str(sorted(set([sanitize(t) for t in temp1]))[0:3])})           
    except IOError as ioerr:
        print('File Error' + str(ioerr))
        return(None)
        
#function call to read in sarah's data            
sarah = get_coach_data('sarah2.txt')
james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')


#print the dict
print(james['Name']+ "'s fastest times are :" + james['Times'])
print(julie['Name']+ "'s fastest times are :" + julie['Times'])
print(sarah['Name']+ "'s fastest times are :" + sarah['Times'])
print(mikey['Name']+ "'s fastest times are :" + mikey['Times'])
