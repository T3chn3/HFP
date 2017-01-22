#Forms

#On the web server
import cgi #used to invoke the request
<form action="cgi-bin/process-time.py" method="POST"> Enter a timing value: #action to take and method to envoke for the response, text
<input type="Text" name="TimeValue" size=40> #TimeValue will hold the users input
<br />
<input type="Submit" value="Send"> </form> #code for the button

form = cgi.FieldStorage() #get the data from the form above
timing_value = form["TimeValue"].value #access the value associated with "TimeValue" from the form.

#this code is used to extend the yate.py template
#altered the cgi script to receive the users input via POST

#skipped the rest of this section! Just pulling out the sqlite implementation 


