a = str(input("enter fi;e with txt ext"))

file2 = open(a,'r')
line = file2.readline()

while (line!=""):
             print(line)
             line=file2.readline()

file2.close()
