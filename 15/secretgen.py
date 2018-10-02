import os
file = open("secret.txt","w")
file.write(os.urandom(32))
