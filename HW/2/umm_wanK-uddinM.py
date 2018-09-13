#Kaitlin
#SoftDev1 pd6
#K2 -- NO-body expects the Spanish Inquisition!
#2018-09-09

import random ##needed for random function!!
w = ['William Lu', 'Qian', 'Peter', 'Ahnaf', 'Kenny', 'Sophia', 'Sajed', 'Emily', 'Hasif', 'Brian ', 'Dennis',
     'Jiayang', 'Shafali ', 'Isaac ', 'Tania', 'Derek', 'Shin', 'Vincent', 'Ricky', 'Puneet', 'Wei Wen', 'Tim',
     'Jeffrey', 'Joyce ', 'Mohtasim', 'Simon', 'Thomas', 'Ray', 'Jack', 'Karen', 'Robin', 'Jabir', 'Johnny ',
     'Matthew', 'Johnson Li', 'Angela', 'Crystal', 'Jiajie', 'Theodore', 'Anton', 'Max', 'Bo', 'Andrew',
     'Kendrick', 'Kevin', 'Kyle', 'Jamil', 'Mohammed', 'Ryan', 'Jason']

m = ['Daniel', 'Aleksandra', 'Addison', 'Hui Min', 'Aaron', 'Rubin', 'Raunak', 'Stefan', 'Cheryl', 'Cathy', 'Mai',
     'Claire ', 'Alex', 'Bill', 'Daniel', 'Jason']

x = ['Derek', 'Britni', 'Joan', 'Vincent', 'Jared', 'Ivan', 'Thomas', 'Maggie', 'Damian', 'Tina', 'Fabiha', 'John',
     'Susan ', 'Kaitlin', 'Michelle', 'Clara', 'Rachel', 'Amit', 'Jerry', 'Raymond', 'Zane', 'Soojin', 'Maryann',
     'Adil', 'Josh', 'Imad']

##List of Arrays
KREWES = [w,m,x]
##Select which random krewes
krew = random.randint(0,len(KREWES)-1)
##Select the random member from the krew
mem = random.randint(0,len(KREWES[krew])-1)

print(KREWES[krew][mem])
