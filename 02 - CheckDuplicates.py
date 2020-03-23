# This takes a .txt file and creates a second one in which every line of the first one 
# is present only once

with open('file.txt', 'r') as originalFile:
    with open('file2.txt', 'w') as secondFile:
        allLines = []
        for line in originalFile:
            if line not in allLines:
                allLines.append(line)
            else:
                print(line)
        for element in allLines:
            secondFile.write(element)