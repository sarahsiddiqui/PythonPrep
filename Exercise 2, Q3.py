# Reading from a file
numFile = open("filee.dat", "r")

# list fields
fNameList = []
lNameList = []
mathList = []
engList = []
scienceList = []
compList = []

while True:
    text = numFile.readline()
    #rstrip removes the newline character read at the end of the line
    text = text.rstrip("\n")     
    if text=="": 
        break
    info = text.split(" ")
    fNameList.append(info[0])
    lNameList.append(info[1])
    mathList.append(int(info[2]))
    engList.append(int(info[3]))
    scienceList.append(int(info[4]))
    compList.append(int(info[5]))
    
numFile.close()

print("First\t\tLast\t\tMath\tEnglish\tScience\tComputers\tAverage")
print(80*"=")
for i in range(len(fNameList)):
    average = (mathList[i] + engList[i] + scienceList[i] + compList[i])/4
    print("%-10s\t%-10s\t%3i\t  %3i\t  %3i\t  %3i\t\t%5.1f" 
          %(fNameList[i], lNameList[i], mathList[i], engList[i], scienceList[i], compList[i], average))