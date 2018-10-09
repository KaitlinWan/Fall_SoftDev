#Kaitlin Wan
#SoftDev1 pd6
#K #17: Average
#2018-10-08

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
from util import db_builder

db_builder.maketable()

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()
ids = []

def id():
    students = c.execute("SELECT * FROM peeps")
    #Returns Tuples
    peeps = []
    mainDic = {}
    #Makes a LIST of TUPLES
    for row in students:
        peeps.append(row) #Puts Tuple inside a List
    for x in peeps:
        ids.append(x[1]) #Makes a LIST of ids
    #MAKES IDs INTO DICTIONARY
    mainDic = { i : None for i in ids}
    #print(peeps)
    #print(ids)
    #print(mainDic)
    return mainDic

students = id()

#Add a List of Grades as part of def of classes:
def addGrade():
    allGrades = []
    grades = []

    for x in ids:
        command = "SELECT mark FROM courses WHERE id = " + str(x) + ";"
        print(command)
        marks = c.execute(command) #holds only marks of x student in a tuple
        for row in marks: #Grade
            if(marks == None):
                pass
            print(row)
            grades.append(row)
        for x in grades:
            print(x)
        students[x] = grades
    print(students)


def table():
    c.execute("CREATE TABLE peeps_avg (id INTEGER, average FLOAT)")
    c.execute("SELECT id, average FROM peeps")
    for data in c.fetchall():
        c.execute("INSERT INTO peeps_avg VALUES ( \"{}\" , \"{}\" )".format(data[0] , data[1]) ) #run SQL statement


table()
