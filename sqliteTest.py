#Python includes SQLite

#import sqlite3

#Python Database API Pattern
#Connect->Create->Interact->Commit->Rollback->Close
'''
Sqlite is just a flat .txt file, can be read via any text editor

#Connect, establish a connection to the database
connection = sqlite3.connect('test.sqlite')

#Create, create a cursor to interact with the db
cursor = connection.cursor()

#Interact
cursor.execute("""SELECT DATE('NOW')""")

#Commit
connection.commit()

#Rollback

#Close
connection.close()
'''
'''
import os
import sqlite3

connection = sqlite3.connect('coachdata.sqlite') #this will create the .sqlite file if it doens't exist.

cursor = connection.cursor()
cursor.execute("""CREATE TABLE athletes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    name TEXT NOT NULL,
                    dob DATE NOT NULL )""")
cursor.execute("""CREATE TABLE timing_data (
                    athlete_id INTEGER NOT NULL,
                    value TEXT NOT NULL,
                    FOREIGN KEY (athlete_id) REFERENCES athletes)""")

connection.commit() #commit() is required to update the db and make changes perminate
connection.close()

#Use SQLite Manager in FireFox to view .sqlite files to verify the contents of the db.
'''
#CRUD pattern, was written in python 2, find an example in python 3

#Other examples covered in the last chapter. 

#Reading in CVS, headings to a list and data into a dict

#use the input() to prompt the user for input. p404

#find the closest match for a given input. p416

#converting time to seconds and seconds to time p419



