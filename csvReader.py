import csv

econPure = []
econBreadth = []

psychologyPure = []
psychologyBreadth = []

engineering = []
mechanical = []
civilEng = []
electricalEng = []
maths = []
english = []
history = []
law = []
finance = []


header = "Institution, Course, Type, Study Mode, Foundation Year(s), Sandwich Year(s), Total years, Salary (6 months after), Median Tariff"

with open("data2.csv","r") as dataFile:
    read = csv.reader(dataFile)
    for count,row in enumerate(read):
        if count % 2 == 0:
            if "economics" == row[1].lower():
                econPure.append(row)
            if "economics" in row[1].lower():
                econBreadth.append(row)
                
            if "psychology" == row[1].lower():
                psychologyPure.append(row)
            if "psychology" in row[1].lower():
                psychologyBreadth.append(row)
                
            if "engineering" in row[1].lower():
                engineering.append(row)
            if "mechanical  engineering" in row[1].lower():
                mechanical.append(row)


def writeToCSV(csvFile, subject):
    with open(csvFile,"w") as file:
        wr = csv.writer(file)
        wr.writerow([header])
        for x in subject:
            wr.writerow(x)

writeToCSV("psychPure.csv", psychologyPure)
writeToCSV("psychBreadth.csv", psychologyBreadth)

           

