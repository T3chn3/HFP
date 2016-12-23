"""comments go here"""

def listProc(listA):
    for each_item in listA:
        if isinstance(each_item, list):
            listProc(each_item)
        else:
            print(each_item)
