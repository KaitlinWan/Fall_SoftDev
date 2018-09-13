#Kaitlin
#SoftDev1 pd6
#K6 -- Stl/O: Divine your Destiny!
#2018-09-13

##PYTHON SCRIPT TO CHANGE CSV TO DICTIONARY
import csv #CSV PACKAGE!
from pprint import pprint ##EASIER TO READ

# To Do anything, you need to be able to read it first
reader = csv.DictReader(open('occupations.csv', 'rb'))
#rb = read in binary mode
#Why in Binary?: you should append 'b' to the mode value to
#open the file in binary mode, which will improve portability
#(https://docs.python.org/2/library/functions.html#open)

#Software portability is usually thought of in quasi-spatial
#terms: can this code be moved sideways to existing hardware
#and software platforms other than the one it was built for?
#(http://www.catb.org/esr/writings/taoup/html/ch17s05.html)


##Initialize empty dictionary
myDict = {}

for row in reader:
    name = row["Job Class"]
    per = row["Percentage"]
    ##Adds new Key to dictionary and Conv string to number
    myDict[name] = float(per)

del myDict['Total']
##remove the last one! we do not need 'Total'

#===================== END OF SCRIPT SECTION ====================

import random
##WEIGHTED RANDOM FUNCTION
def weightedRandom():
    myList=[]
    for x in myDict:
        num = int(myDict[x] * 10) ##NO MORE DECIMALS!!!
        for i in range(num): ##adds num many to string
            myList.append(x)
    choice = random.choice(myList)
    print("Probablity: ")
    print(str( myList.count(choice)) + "/" + str(len(myList)))
    return choice


print(weightedRandom())
