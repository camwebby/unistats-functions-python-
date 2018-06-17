from main1 import *
from time import sleep
import csv


with open("database.csv","w") as dataFile:
    wr = csv.writer(dataFile,quoting=csv.QUOTE_NONE,escapechar='~')
    wr.writerow(["Institution","Course","Label","URL","Mode","Salary","avgTariff","lowerTariff","Employment"])
    for tution in getInstis():
        id1 = tution["PUBUKPRN"]
        institution = tution["Name"]

        for x in getData(id1):
            sleep(0.5)
            b = x["KisCourseId"]
            c = x["KisMode"]
            y = getCumulative(getTariffs(id1,b,c))
            info = getInfo(id1,b,c)
            if len(getSalary(id1,b,c)) == 1:
                try:
                    courseTitle = x["Title"]
                    courseURL = info["CoursePageUrl"]
                    courseLabel = info["KisAimLabel"]
                    courseMode = c
                    courseSalary = getSalary(id1, b, c)[0]
                    avgTariff = tariffAvg(y)
                    miniTariff = minTariff(getTariffs(id1,b,c))
                    courseEmployment = getWorkStudy(id1,b,c)[0]

                    wr.writerow([institution,courseTitle,courseLabel,courseURL,courseMode,courseSalary,avgTariff,miniTariff,courseEmployment])
                    print("writing")
                except:
                    print("Cannot write instance")
                    continue
