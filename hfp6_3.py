#This example reads in data from a file, creates a class, with extended methods to add times. 
#The data is sorted and printed to screen

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

class Athlete: #pretty much a wrapper for the list class
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
        
    def top3(self):
        return(sorted(set([sanitize(t) for t in self.times]))[0:3])
    
    def add_time(self, time):
        self.times.append(time)  
        
    def add_times(self, times):
        self.times.extend(times)
        
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return(Athlete(templ.pop(0), templ.pop(0), templ))
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)
    
james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')

print(james.name + "'s fastest times are: " + str(james.top3()))
print(julie.name + "'s fastest times are: " + str(julie.top3()))
print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))

sarah.add_time('0.12')
sarah.add_times(['1.99','2.66'])
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))



































sarah = get_coach_data('sarah2.txt')