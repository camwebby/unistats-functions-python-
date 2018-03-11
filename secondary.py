from main1 import *
from time import sleep


api_key = "L5R08VNTMZFPGLU2UGUD"

##test data####
essex = "10007791"
UWE = "10007783"
insti = UWE
##test data###


##for x in getData(insti):
##    a = insti
##    b = x["KisCourseId"]
##    c = x["KisMode"]
##    try:
##        if max(getSalary(a,b,c)) < 18000:
##            print("{} has {}% employed or studying further, where the average salary of those working is {}".format(x["Title"], getWorkStudy(a,b,c), getSalary(a,b,c)))
##    except:
##        continue

##for x in getData(essex):
##    if "Psychoanalytic Studies" in x["Title"]:
##        print(getCumulative(getTariffs(essex,x["KisCourseId"],x["KisMode"])))

for tution in getInstis():
    id1 = tution["PUBUKPRN"]

    if tution["TEFOutcome"] != "DidNotParticipate" and tution["TEFOutcome"] != "Provisional":

        for x in getData(id1):
            sleep(0.3)
            b = x["KisCourseId"]
            c = x["KisMode"]
            y = getCumulative(getTariffs(id1,b,c))
            ##    print("{} is the tariff for {}".format(y,x["Title"]))
            if len(getSalary(id1,b,c)) == 1:
                try:
                    print(id1,x["Title"],getSalary(id1,b,c)[0],tariffAvg(y))
                except:
                    continue

