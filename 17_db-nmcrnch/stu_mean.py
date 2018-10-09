#TEAM GARY RISES AGAIN - Kaitlin Wan & Joshua Weiner
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

def make_dict():
    students = c.execute("SELECT * FROM peeps")
    #Returns Tuples
    peeps = []
    #Makes a LIST of TUPLES
    for row in students:
        peeps.append({'id' : row[2] , 'marks' : [], 'name' : row[0]}) #Puts Tuple id/grade pair inside a List

    for student in peeps:
        id_num = student['id'] #get student id
        command = "SELECT mark FROM courses WHERE courses.id={}".format(id_num) #gets the grades from each course that shares the student id
        grades = c.execute(command) #command to retrieve the grades
        for mark in grades:
            mark = list(mark)
            student['marks'].append(mark[0]) #Adds grades to matching student id.
    return peeps #return dict

#Calculate Average:
def findAvg(grades):
    avgs = []
    for row in grades:
        allG = row['marks']
        avg = 0
        for grade in allG:
            avg = sum(allG)/len(allG)
            #print(avg)
        avgs.append({'id' : row['id'] , 'average' : avg, 'name': row['name']})
    print(avgs) #FOR DISPLAY AS OUTLINED IN HW
    return avgs


def table(stu_avgs):
    c.execute("CREATE TABLE peeps_avg (id INTEGER, average FLOAT)") #Create new table in DB
    id_avg = stu_avgs
    for x in id_avg:
        #print(x)
        c.execute("INSERT INTO peeps_avg VALUES({0}, {1})".format(x['id'] , x['average']) ) #run SQL statement

#============ RUN ===============
student_grades = make_dict()
#print(students) # Test statement for debugging
student_averages = findAvg(student_grades)
#print(student_averages) #Test statement for debugging
table(student_averages)
#========== END RUN==============

db.commit() #save changes
db.close()  #close database

#P.S. Teletype is an amazing tool for collaboration!!
