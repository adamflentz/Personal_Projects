import csv

namedict = {}
totalvotes = 0
with open('votes.csv', 'r') as csvfile:
    votecounter = csv.reader(csvfile)
    rowcount = 0
    for row in votecounter:
        elementcount = 0
        for element in row:
            print(element)
            if elementcount == 0 or rowcount == 0:
                pass
            elif element not in namedict:
                namedict[element] = 1
                totalvotes += 1
            else:
                namedict[element] += 1
                totalvotes += 1
            elementcount += 1
        rowcount += 1
    print(namedict)

with open ('output.csv', 'w') as csvoutput:
    outputwriter = csv.writer(csvoutput)
    for key in namedict:
        outputwriter.writerow([key, namedict[key], (namedict[key] / totalvotes)])

