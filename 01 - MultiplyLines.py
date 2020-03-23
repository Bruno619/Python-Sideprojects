# This takes every line of the first .txt file and creates a second file in which it 
# repeats the line 'c' times

with open('file.txt', 'r') as originalFile:
    with open('file2.txt', 'w') as secondFile:
        for line in originalFile:
            c = 0
            while c < 2:            
                secondFile.write(line)
                c += 1