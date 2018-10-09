#Kaitlin Wan
#SoftDev1 pd6
#K #17: Average
#2018-10-08

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
from util import db_builder

db_builder.maketable()

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()


def combine():
    students  = c.execute("SELECT * FROM peeps")
    print(students)

combine()
