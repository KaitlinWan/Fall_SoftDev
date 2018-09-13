import os
import time

hwNum = input("HW Number: ")

path = os.getcwd()
path += "/HW/" + str(hwNum)

title = input("HW Title: ")

fname = input("File name: ")

os.makedirs(path)

f = open(path + "/" + fname, "w")
f.write("#Kaitlin\n#SoftDev1 pd6\n#K" + hwNum + " -- " + title + "\n#" + time.strftime("%Y-%m-%d"))
f.close()
