from main1 import *
from time import sleep
import csv


with open("data.csv","w") as dataFile:
    wr = csv.writer(dataFile,quoting=csv.QUOTE_NONE,escapechar=' ')
    wr.writerow(["Institution, Course, Salary (6 months after), Median Tariff"])
    for tution in getInstis():
        id1 = tution["PUBUKPRN"]

        if tution["TEFOutcome"] != "DidNotParticipate" and tution["TEFOutcome"] != "Provisional":

            for x in getData(id1):
                sleep(0.4)
                b = x["KisCourseId"]
                c = x["KisMode"]
                y = getCumulative(getTariffs(id1,b,c))
                if len(getSalary(id1,b,c)) == 1:
                    try:
                        wr.writerow([id1,x["Title"].replace(",",""),getSalary(id1,b,c)[0],tariffAvg(y)])
                        print("Writing")
                    except:
                        continue
