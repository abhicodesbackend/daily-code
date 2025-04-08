inFile = open("something.txt","r")
inStr = inFile.read()
inFile.close()
eStr = inStr.split("\n")

idCount = len(eStr)

writeStr = ""
count = 0
while count < idCount:
    writeStr = writeStr + str(eStr[count]) + ","
    count+=1
outFile = open("SEmail.txt","w")
outFile.write(writeStr)
outFile.close()
