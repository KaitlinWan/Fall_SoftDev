#Kaitlin Wan
#SoftDev1 pd6
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

command = "CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER PRIMARY KEY);"        #build SQL stmt, save as string
c.execute(command)

with open('peeps.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #insert into tbl values(name,age,id);
        pop = ("insert into peeps values(" + "'" + row['name'] + "'" + ',' + row['age'] + ',' + row['id'] + ');')
        c.execute(pop)

command = ('select * from peeps;')
c.execute(command) #run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
