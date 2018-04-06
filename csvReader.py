import csv

econPure = []
econBreadth = []

psychologyPure = []
psychologyBreadth = []

engineering = []
mechanical = []
civilEng = []
electricalEng = []

physicsPure = []

historyBreadth = []
historyPhil = []

compBreadth = []
compSciPure = []

medicine = []

physiotherapyPure = []

mathPure = []
mathBreadth = []

businessBreadth = []

biologyPure = []

chemistryPure = []
chemistryBreadth = []

artBreadth = []

modernLanguages = []

artDesign = []

english = []

agriculture = []

educ = []

media = []


header = "Institution, Course, Type, Study Mode, Foundation Year(s), Sandwich Year(s), Total years, Salary (6 months after), Median Tariff"



with open("FullDataSet.csv","r") as dataFile:
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
            if "civil  engineering" in row[1].lower():
                civilEng.append(row)
            if "electrical  engineering" in row[1].lower() or "electronic  engineering" in row[1].lower():
                electricalEng.append(row)
            if "physics" == row[1].lower():
                physicsPure.append(row)
                
            if "art" in row[1].lower():
                artBreadth.append(row)
            if "business" in row[1].lower():
                businessBreadth.append(row)
            if "mathematics" in row[1].lower() or "mathematical" in row[1].lower():
                mathBreadth.append(row)
            if "mathematics" == row[1].lower():
                mathPure.append(row)
            if "computer  science" == row[1].lower():
                compSciPure.append(row)
            if "computer" in row[1].lower():
                compBreadth.append(row)
            if "biology" == row[1].lower():
                biologyPure.append(row)
            if "chemistry" == row[1].lower():
                chemistryPure.append(row)
            if "chemistry" in row[1].lower() or "chemical" in row[1].lower():
                chemistryBreadth.append(row)
            if "physiotherapy" == row[1].lower():
                physiotherapyPure.append(row)
            if "medicine" in row[1].lower():
                medicine.append(row)
            if "history" in row[1].lower():
                historyBreadth.append(row)
            if "history" == row[1].lower() or "philosophy" == row[1].lower():
                historyPhil.append(row)
            if "german" == row[1].lower() or "french" == row[1].lower() or "spanish" == row[1].lower() or "chinese" == row[1].lower():
                modernLanguages.append(row)
            if "art" in row[1].lower() or "design" in row[1].lower():
                artDesign.append(row)
            if "english  language" == row[1].lower() or "english  literature" == row[1].lower():
                english.append(row)
            if "agriculture" in row[1].lower():
                agriculture.append(row)
            if "education" in row[1].lower():
                educ.append(row)
            if "media" in row[1].lower():
                media.append(row)
                

def writeToCSV(csvFile, subject):
    with open(csvFile,"w") as file:
        wr = csv.writer(file)
        wr.writerow([header])
        for x in subject:
            wr.writerow(x)

##writeToCSV("civil.csv", civilEng)
##writeToCSV("electricEng.csv", electricalEng)
##
##writeToCSV("physicsPure.csv", physicsPure)


writeToCSV("media.csv",media)
writeToCSV("modernLanguages.csv", modernLanguages)
writeToCSV("historyBreadth.csv",historyBreadth)
writeToCSV("historyPhil.csv",historyPhil)
writeToCSV("biologyPure.csv",biologyPure)
writeToCSV("mathematicsPure.csv",mathPure)
writeToCSV("mathematicsBreadth.csv",mathBreadth)
writeToCSV("computerBreadth.csv",compBreadth)
writeToCSV("compScience.csv",compSciPure)
writeToCSV("business.csv",businessBreadth)
writeToCSV("artAndDesign.csv", artDesign)
writeToCSV("physiotherapy.csv",physiotherapyPure)
writeToCSV("mechEng.csv", mechanical)
writeToCSV("engineeringAll.csv", engineering)
writeToCSV("medicine.csv",medicine)
writeToCSV("english.csv",english)
writeToCSV("agriculture.csv",agriculture)
writeToCSV("chemistry.csv", chemistryPure)
writeToCSV("biology.csv", biologyPure)
writeToCSV("education.csv", educ)





