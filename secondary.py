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


for x in getData(essex):
    sleep(0.1)
    b = x["KisCourseId"]
    c = x["KisMode"]
    y = getCumulative(getTariffs(essex,b,c))
##    print("{} is the tariff for {}".format(y,x["Title"]))
    try:
        print("{} is the median tariff for {} where tariff is{}".format(tariffAvg(y),x["Title"],y))
    except:
        continue

