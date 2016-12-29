"""
Multi Line Look like so...
"""
#Single line comment

def listProc(listA, level=0,indent=False):
    for each_item in listA:
        if isinstance(each_item, list):
            listProc(each_item, level +1,indent)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end='')
            print(each_item)

movies = [ "The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,["Graham Chapman", ["Michael Palin",
"John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

''' 
Key Takeaways
module: a text file that contains Python code
disstribution utilities: allow you to turn your module into a sharable package
setup.py: defines the metadata about your package, versioning, usage...ect
Import: is the flag to use the modules functions
namespace: myimport.myfunction(), used to quantify the modules functions when envoking them using the module function() form
** You can pull specific fuctions from modules by using the `from module import fuction` statement.
__builtins__: namespace for the builtin functions
range(): BIF can be used with for to interate a fixed number of times.
end=``: turns off the print()'s automatic inclusion of the new-line on output
Pro-Tip: Arguments to your functions are optional if you provide them with a default value
'''

