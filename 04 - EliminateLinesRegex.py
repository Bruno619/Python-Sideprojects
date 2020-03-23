import re, csv

# This script takes a file and creates a second one with every line that doesn't contain \s or -

with open('file1.csv', 'r') as file1:
    file1Csv = csv.reader(file1, delimiter=';')
    with open('file2.csv', 'w') as file2:
        file2Csv = csv.writer(file2, delimiter=';')
        newLine = []
        for element in file1Csv:
            match = re.search(r'\s|-', element[0])
            if not match:
                newLine.append(element)
        for element in newLine:
            file2Csv.writerow(element)