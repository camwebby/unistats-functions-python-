from main1 import *

api_key = "L5R08VNTMZFPGLU2UGUD"

##test data####
essex = "10007791"
UWE = "10007783"
insti = UWE
##test data###

for x in getData(insti):
    a = insti
    b = x["KisCourseId"]
    c = x["KisMode"]
    try:
        if max(getSalary(a,b,c)) < 18000:
            print("{} has {}% employed or studying further, where the average salary of those working is {}".format(x["Title"], getWorkStudy(a,b,c), getSalary(a,b,c)))
    except:
        continue
