#CGI, Common Gateway Interface, standarized way to communicated between server and client

import pickle
from hfp6_4 import AthleteList

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return(AthleteList(templ.pop(0), templ.pop(0), templ))
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)

def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data(each_file) #take each file and turn it into an AthleteList object instance
        all_athletes[ath.name] = ath #each athlete's name is used as the key, the value is the object instance
    try:
        with open('athletes.pickle','wb') as athf: #save the dict via pickle
            pickle.dump(all_athletes,athf)
    except IOError as ioerr:
        print('File error(put_and_store):'+str(ioerr))
        
    return(all_athletes)
    
def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle','rb') as athf: #open the pickled data
            all_athletes = pickle.load(athf) #read the pickle into the dict
    except IOError as ioerr:
        print('File error (get_from_store):' + str(ioerr))
 
    return(all_athletes)