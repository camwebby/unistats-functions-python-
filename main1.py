import json
import requests

api_key = "L5R08VNTMZFPGLU2UGUD"
prefix = "http://"+api_key+":password"+"@"

##test data##
essex = "10007791"
UWE = "10007783"

def getInstis():
    getURL = prefix+"data.unistats.ac.uk/api/v4/KIS/Institutions.json?pageSize=10000"
    readInstiJSON = requests.get(url=getURL)
    Institutions = readInstiJSON.json()
    return Institutions 

def getData(institution):
    getURL = prefix+"data.unistats.ac.uk/api/v4/KIS/Institution/"+institution+"/Courses.json?pageSize=10000"
    readJSON = requests.get(url=getURL)
    data = readJSON.json()
    return data


def getStat(institution, course, studyMode):
    statApiURLget = prefix+"data.unistats.ac.uk/api/v4/KIS/Institution/"+institution+"/Course/"+course+"/"+studyMode+"/Statistics.json"
    readCourseJSON = requests.get(url=statApiURLget)
    info = readCourseJSON.json()
    return info

def getInfo(institution, course, studyMode):
    infoApiURLget = prefix+"data.unistats.ac.uk/api/v4/KIS/Institution/"+institution+"/Course/"+course+"/"+studyMode+".json"
    readCourseJSON = requests.get(url=infoApiURLget)
    info = readCourseJSON.json()
    return info

def getWorkStudy(institution, course, studyMode):
    workStudy = []
    for x in getStat(institution, course, studyMode):
        for y in x["Details"]:
            if y["Code"] == "WORKSTUDY":
                workStudy.append(y["Value"])
    return workStudy

def getSalary(institution, course, studyMode):
    salary = []
    for x in getStat(institution, course, studyMode):
        for y in x["Details"]:
            if y["Code"] == "INSTMED":
                salary.append(y["Value"])            
    return salary

def getTariffs(institution, course, studyMode):
    tariffs = []
    for x in getStat(institution, course, studyMode):
        if x["Code"] == "TARIFF":
            for y in x["Details"]:
                tariffs.append(y["Code"])
                tariffs.append(y["Value"])
    if len(tariffs) > 28:
        tariffs = [tariffs[i:i+28] for i in range(0, len(tariffs), 28)] 
    return tariffs

def getCumulative(tariff):
    cumulative = []
    count = 0
    if len(tariff) == 28:
        for x in tariff:
            if isinstance(x,str):
                cumulative.append(x)
            elif isinstance(x,int):
                count = count + x 
                cumulative.append(count)
    else:
        for x in tariff:
            count = 0
            for y in x:
                if isinstance(y,str):
                    cumulative.append(y)
                elif isinstance(y,int):
                    count = count + y 
                    cumulative.append(count)
        cumulative = [cumulative[i:i+28] for i in range(0, len(cumulative), 28)] 
    return cumulative

def tariffAvg(cumul):
    tariff2d = [[],[]]
    for x in cumul[::2]:
        tariff2d[0].append(x)
    for x in cumul[1::2]:
        tariff2d[1].append(x)
    median = 0
    for x,y in enumerate(tariff2d[1]):
        if int(y)==50:
            median = int(tariff2d[0][x][1:])
        elif int(tariff2d[1][x-1]) < 50 and int(y) > 50:
            x1 = int(tariff2d[0][x][1:])
            x2 = 0
            if x1 == 1:
                x2 = x1+46
            else:
                x2 = x1+15
            y1 = int(tariff2d[1][x-1])
            y2 = int(y)
            ratio = (y2 - 50)/(y2-y1)
            median = x2-((x2-x1)*ratio)
    return median

def minTariff(tariff):
    minTariffs = []
    if len(tariff) == 28:
        for y, x in enumerate(tariff):
            if isinstance(x,int) and x >= 5:
                minTariffs.append(tariff[y-1])
                break
    return int(minTariffs[0][1:])
            
    



##print(tariffAvg(getCumulative(getTariffs(essex,"10502","FullTime"))))





##def findCourse(ucas, salary, perc):
##    a = "10007791"
##    for x in getData(insti):
##        b = x["KisCourseId"]
##        c = x["KisMode"]
##        print(getCumulative(getTariffs(a,b,c)))
##
##findCourse(100, 24000, 50)









