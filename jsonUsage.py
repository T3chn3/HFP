#JSON notes
'''
JS - JavaScript
ON - Object Notation

Initally designed to pass data from one JavaScript program to another it 
is now an interchange language to work between different programming languages.
Language-neutral data interchange format 
'''
#import json #or you could import simplejson, don't know what the major differences are?
'''
json is the standard built in Library.
json is simplejson added to stdlib. It was added in 2.6, while simple json works with 2.4+
simplejson is updated more frequently.
best pratice is to load one or the other as a fallback
"
try: import simplejson as json
except: ImportError: import json
"
The jury is still out on which json lib is the best.
cjson is fastest
simplejson is almost on par with cjson
json is about 10x slower than simplejson
^based on benchmarking
'''
try: import simplejson as json
except ImportError: 
        import json

names = ['John',['Johnny','Jack'], 'Michael', ['Mike','Mikey','Mick']] #list
print(type(names))
print(names)
a = json.dumps(names)
print(type(a))
print(a)
b = json.loads(a)
print(type(b))
print(b)

