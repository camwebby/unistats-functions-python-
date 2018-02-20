import json
import requests

api_key = "L5R08VNTMZFPGLU2UGUD"
prefix = "http://"+api_key+":password"+"@"



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
            if y["Code"] == "MED":
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
                cumulative.append(int(x[1:]))
            elif isinstance(x,int):
                count = count + x 
                cumulative.append(count)
    else:
        for x in tariff:
            count = 0
            for y in x:
                if isinstance(y,str):
                    cumulative.append(int(y[1:]))
                elif isinstance(y,int):
                    count = count + y 
                    cumulative.append(count)
        cumulative = [cumulative[i:i+28] for i in range(0, len(cumulative), 28)] 
    return cumulative



##def findCourse(ucas, salary, perc):
##    a = "10007791"
##    for x in getData(prefix+youareell):
##        b = x["KisCourseId"]
##        c = x["KisMode"]
##        print(getCumulative(getTariffs(a,b,c)))
##
##findCourse(100, 24000, 50)
        
        
    







