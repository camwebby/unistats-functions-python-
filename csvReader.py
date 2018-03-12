import csv

econ = []
psychology = []
engineering = []
mechanical = []


with open("data.csv","r") as dataFile:
    read = csv.reader(dataFile)
    for count,row in enumerate(read):
        if count % 2 == 0:
            if "economics" in row[1].lower():
                econ.append(row)
            elif "psychology" in row[1].lower():
                psychology.append(row)
            if "engineering" in row[1].lower():
                engineering.append(row)
            if "mechanical  engineering" in row[1].lower():
                mechanical.append(row)

                
print(mechanical)
