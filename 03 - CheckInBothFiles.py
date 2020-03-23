import csv

# File structure:
# token;value

# This code checks if every single value of the first file is present in the second one, if it's present
# it creates a 3rd file and copies the line in which the value is present to a 3rd file 

with open('file1.csv', 'r') as file1:
    file1Csv = csv.reader(file1, delimiter=';')
    with open('file2.csv', 'r') as file2:
        file2Csv = csv.reader(file2, delimiter=';')
        with open('file3.csv', 'w') as file3File:
            file3Csv = csv.writer(file3File, delimiter=';')
            file3Lines = []
            file2Values = []
            for file2Line in file2Csv:
                file2Values.append(file2Line[1])
            for file1Line in file1Csv:
                if file1Line[1] in file2Values:
                    file3Lines.append(file1Line)
                else:
                    print(file1Line)
            for element in file3Lines:
                file3Csv.writerow(element)