#Dictionary and Class usage and examples

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
        return(data.strip().split(','))
    except IOError as ioerr:
        print('File Error' + str(ioerr))
        return(None)
        
#function call to read in sarah's data            
sarah = get_coach_data('sarah2.txt')

(sarah_name, sarah_dob) = sarah.pop(0),sarah.pop(0)

print(sarah_name + "'s fastest times are:" + str(sorted(set([sanitize(t) for t in sarah]))[0:3]))

#shortcoming of this code is that it's only written for Sarah, you would still need to alter 
#print statements for each runner, easy with 4 runners, difficult with 4000 runners.

#the three pieces of data about sarah are all disjointed or independent of each other

#Enter the Dictionary (Key/Value Pairs), aka mapping a hash or an associative array
#Keys: Name/DOB/Times Values: sarah's data

#can you have an unlimited number of keys?

#The order the data is added to the dict isn't maintained, but the key/value association is maintained 












