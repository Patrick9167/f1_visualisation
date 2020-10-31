import csv
import json
from itertools import zip_longest
import numpy as np

def time_to_num(time):
    return (int(time[0])*60)+float(time[2:8])

tracks = {
    "1010":"ALI_",
    "1011":"BAH_",
    "1012":"CHI_",
    "1013":"AZE_",
    "1014":"SPA_",
    "1015":"MON_",
    "1016":"CAN_",
    "1017":"FRA_",
    "1018":"AUS_",
    "1019":"UKS_",
    "1020":"GER_",
    "1021":"HUN_",
    "1022":"BEL_",
    "1023":"ITA_",
    "1024":"SIN_",
    "1025":"RUS_",
    "1026":"JAP_",
    "1027":"MEX_",
    "1028":"USA_",
    "1029":"BRA_",
    "1030":"ABU_",
}

# teams = {
#     {"0" : "alfaromeo", "driver00" : "8" , "driver01" : "841"}
#     {"1" : "ferrari", "driver00" : "20" , "driver01" : "844"}
#     {"2" : "haas", "driver00" : "825" , "driver01" : "154"}
#     {"3" : "maclaren", "driver00" : "846" , "driver01" : "832"}
#     {"4" : "mercedes", "driver00" : "1" , "driver01" : "822"}
#     {"5" : "racingpoint", "driver00" : "815" , "driver01" : "840"}
#     {"6" : "redbull", "driver00" : "830" , "driver01" : ""}
#     {"7" : "renault", "driver00" : "817" , "driver01" : "807"}
#     {"8" : "torrorosso", "driver00" : "826" , "driver01" : ""}
#     {"9" : "williams", "driver00" : "847" , "driver01" : "9"}
# }



driversAll='./drivers.json'
laptimes2019='./2019lap_times.json'
processedlaptimes2019='./processed2019lap_times.json'
laptimesAllcsv='./f1/lap_times.csv'
modifiedlaptimes2019='./modifiedlaptimes2019.json'
teams='../teams.json'

engines='./engines.json'

## Isolates races from 2019 and gives each json element a tag of "raceID_driverID_lap#"
## Input file: f1/lap_times.csv
## Output file: 2019lap_times.json
def isolate2019Season(filename, exitfile):
    data = {}
    with open(filename) as csvFile:
        laptimes_csv = csv.DictReader(csvFile)
        i=0
        for lap in laptimes_csv:
            if(int(lap['raceId'])>=1010 and int(lap['raceId'])<=1030):
                id=lap['raceId']+"_"+lap['driverId']+"_"+lap['lap']
                data[id]=lap

    with open(exitfile, 'w') as jsonFile:
         jsonFile.write(json.dumps(data, indent=4))




def create2019Profiles(filename, exitfile):
    data={}
    with open(filename, 'r') as jsonFile:
        2019_lap_times = json.load(jsonFile)
        i=0
        prev_lap="1010_822_1"
        circuit_lap_number=[]
        circuit_lap_times=[]
        circuit_lap_position=[]
        ## rows = "1010_1_1"
        for lap in 2019_lap_times:

            if(2019_lap_times[prev_lap]["driverId"]==2019_lap_times[lap]["driverId"]):
                circuit_lap_number.append(2019_lap_times[lap]["lap"])
                circuit_lap_times.append(time_to_num(2019_lap_times[lap]["time"]))
                circuit_lap_position.append(2019_lap_times[lap]["position"])
            else:
                circ_prefix=tracks[2019_lap_times[prev_lap]["raceId"]]
                print(circ_prefix)
                if(len(data)<20): data[2019_lap_times[prev_lap]["driverId"]] = {}

                ##data[2019_lap_times[prev_lap]["driverId"]]["driverId"] = 2019_lap_times[prev_lap]["driverId"]
                data[2019_lap_times[prev_lap]["driverId"]][circ_prefix+"2019_lap_times"] = circuit_lap_number
                data[2019_lap_times[prev_lap]["driverId"]][circ_prefix+"time"] =circuit_lap_times
                data[2019_lap_times[prev_lap]["driverId"]][circ_prefix+"position"] =circuit_lap_position
                circuit_lap_number=[]
                circuit_lap_times=[]
                circuit_lap_position=[]
                circuit_lap_number.append(2019_lap_times[lap]["lap"])
                circuit_lap_times.append(time_to_num(2019_lap_times[lap]["time"]))
                circuit_lap_position.append(2019_lap_times[lap]["position"])


            prev_lap = lap

    print("filewritten")
    with open(exitfile, 'w') as jsonFile:
         jsonFile.write(json.dumps(data, indent=4))

def modify2019Profiles(filename, exitfile):
    dr_nums = {
     "1" : {"name":  "Hamilton", "team" : "4"},
     "8":  {"name": "Raikkonen", "team" : "0"},
     "9":  {"name": "Kubica", "team" : "9"},
     "20": {"name": "Vettel", "team" : "1"},
     "154":{"name": "Grosjean", "team" : "2"},
     "807":{"name": "Hulkenberg", "team" : "7"},
     "815":{"name": "Perez", "team" : "5"},
     "817":{"name": "Ricciardo", "team" : "7"},
     "822":{"name": "Bottas", "team" : "4"},
     "825":{"name": "Magnussen", "team" : "2"},
     "826":{"name": "Kvyat", "team" : "8"},
     "830":{"name": "Verstappen", "team" : "6"},
     "832":{"name": "Sainz", "team" : "3"},
     "840":{"name": "Stroll", "team" : "5"},
     "841":{"name": "Giovinazzi", "team" : "0"},
     "842":{"name":"Gasly", "team" : "610218"}, #including 1021
     "844":{"name":"Leclerc", "team" : "1"},
     "846":{"name":"Norris", "team" : "3"},
     "847":{"name":"Russell", "team" : "9"},
     "848":{"name":"Albon", "team" : "810216"}, #including 1021
     }

    circuits = {
         "ALI_":{"key" : "1010", "total_laps" : "58"},
         "BAH_":{"key" : "1011", "total_laps" : "57"},
         "CHI_":{"key" : "1012", "total_laps" : "56"},
         "AZE_":{"key" : "1013", "total_laps" : "51"},
         "SPA_":{"key" : "1014", "total_laps" : "66"},
         "MON_":{"key" : "1015", "total_laps" : "78"},
         "CAN_":{"key" : "1016", "total_laps" : "70"},
         "FRA_":{"key" : "1017", "total_laps" : "53"},
         "AUS_":{"key" : "1018", "total_laps" : "71"},
         "UKS_":{"key" : "1019", "total_laps" : "52"},
         "GER_":{"key" : "1020", "total_laps" : "64"},
         "HUN_":{"key" : "1021", "total_laps" : "70"},
         "BEL_":{"key" : "1022", "total_laps" : "44"},
         "ITA_":{"key" : "1023", "total_laps" : "53"},
         "SIN_":{"key" : "1024", "total_laps" : "61"},
         "RUS_":{"key" : "1025", "total_laps" : "53"},
         "JAP_":{"key" : "1026", "total_laps" : "52"},
         "MEX_":{"key" : "1027", "total_laps" : "71"},
         "USA_":{"key" : "1028", "total_laps" : "56"},
         "BRA_":{"key" : "1029", "total_laps" : "71"},
         "ABU_":{"key" : "1030", "total_laps" : "55"},
     }

    with open(filename, 'r') as jsonFile:
        laps = json.load(jsonFile)
        i=0
        for prefix in circuits:
            maxi=0
            best=300
            for rows in laps:
                if(prefix+"laps" in laps[rows] and max(laps[rows][prefix+"time"])>maxi):
                    maxi=max(laps[rows][prefix+"time"])
                if(prefix+"laps" in laps[rows] and min(laps[rows][prefix+"time"])<best):
                    best = min(laps[rows][prefix+"time"])
            print(prefix+" best lap="+str(best))

        for rows in laps:
                laps[rows]["driverName"] = dr_nums[rows]["name"]
                laps[rows]["team"] = dr_nums[rows]["team"]
                for prefix in circuits:
                    if prefix+"laps" in laps[rows]:
                        if(prefix=="BRA_"):
                            laps[rows][prefix+"laps"].reverse()
                            laps[rows][prefix+"time"].reverse()
                            laps[rows][prefix+"position"].reverse()
                        if(len(laps[rows][prefix+"laps"])==int(circuits[prefix]["total_laps"])):
                            laps[rows][prefix+"finalpos"]=laps[rows][prefix+"position"][-1]
                        #    print("completed")
                            i=i+1
                        else:
                            laps[rows][prefix+"finalpos"]="0"
                        ##    print("retired")
                            i=i+1
                    else:
                    #    print("Annom: ", prefix, " Did: ", rows )
                    #    print("no laps")
                        laps[rows][prefix+"time"]=[0]
                        laps[rows][prefix+"position"]=["-1"]
                        laps[rows][prefix+"laps"]=["0"]
                        laps[rows][prefix+"finalpos"]="-1"
                i=i+1

    with open(exitfile, 'w') as jsonFile:
      jsonFile.write(json.dumps(laps, indent=4))


def initList(n, m):
    listofzeros = [m] * n
    return listofzeros


def addEngine(filename, extrafile, exitfile):
    circuits = {
             "ALI_":{"key" : "1010", "total_laps" : "58"},
             "BAH_":{"key" : "1011", "total_laps" : "57"},
             "CHI_":{"key" : "1012", "total_laps" : "56"},
             "AZE_":{"key" : "1013", "total_laps" : "51"},
             "SPA_":{"key" : "1014", "total_laps" : "66"},
             "MON_":{"key" : "1015", "total_laps" : "78"},
             "CAN_":{"key" : "1016", "total_laps" : "70"},
             "FRA_":{"key" : "1017", "total_laps" : "53"},
             "AUS_":{"key" : "1018", "total_laps" : "71"},
             "UKS_":{"key" : "1019", "total_laps" : "52"},
             "GER_":{"key" : "1020", "total_laps" : "64"},
             "HUN_":{"key" : "1021", "total_laps" : "70"},
             "BEL_":{"key" : "1022", "total_laps" : "44"},
             "ITA_":{"key" : "1023", "total_laps" : "53"},
             "SIN_":{"key" : "1024", "total_laps" : "61"},
             "RUS_":{"key" : "1025", "total_laps" : "53"},
             "JAP_":{"key" : "1026", "total_laps" : "52"},
             "MEX_":{"key" : "1027", "total_laps" : "71"},
             "USA_":{"key" : "1028", "total_laps" : "56"},
             "BRA_":{"key" : "1029", "total_laps" : "71"},
             "ABU_":{"key" : "1030", "total_laps" : "55"},
         }
    with open(filename, 'r') as jsonFile:
        drivers = json.load(jsonFile)
        data={}
        data["ferrari"]={"team":"10"}
        data["mercedes"]={"team": "12"}
        data["renault"]={"team":"13"}
        data["honda"]={"team":"11"}
        for engines in data:
            ### FIX this ! and add longest lap to engines
            for prefix in circuits:
                data[engines][prefix+"time"] = initList(int(circuits[prefix]["total_laps"]),0)
                data[engines][prefix+"total_laps"] = circuits[prefix]["total_laps"]
                data[engines][prefix+"divisor"] = initList(int(circuits[prefix]["total_laps"]),0)
                data[engines][prefix+"longest_lap"] = drivers["1"][prefix+"longest_lap"]


        with open(extrafile, 'r') as jFile:
            teams = json.load(jFile)
            for driverId in drivers:
                if(int(drivers[driverId]["team"])<10 or int(drivers[driverId]["team"][0])==8 or int(drivers[driverId]["team"][0])==6):
                    if(int(drivers[driverId]["team"][0])==6 or int(drivers[driverId]["team"][0])==8):
                        for prefix in circuits:
                            if(drivers[driverId][prefix+"finalpos"]!="-1"):
                                lapsComplete = initList(len(drivers[driverId][prefix+"laps"]),1)
                                data["honda"][prefix+"divisor"] = [sum(n) for n in zip_longest(data["honda"][prefix+"divisor"], lapsComplete, fillvalue=0)]
                            b = drivers[driverId][prefix+"time"]
                            data["honda"][prefix+"time"]=[sum(n) for n in zip_longest(data["honda"][prefix+"time"], b, fillvalue=0)]
                    else:
                        for prefix in circuits:
                            if(drivers[driverId][prefix+"finalpos"]!="-1"):
                                lapsComplete = initList(len(drivers[driverId][prefix+"laps"]),1)
                                data[teams[drivers[driverId]["team"]]["engine"]][prefix+"divisor"] = [sum(n) for n in zip_longest(data[teams[drivers[driverId]["team"]]["engine"]][prefix+"divisor"], lapsComplete, fillvalue=0)]
                            b =drivers[driverId][prefix+"time"]
                            data[teams[drivers[driverId]["team"]]["engine"]][prefix+"time"]=[sum(n) for n in zip_longest(data[teams[drivers[driverId]["team"]]["engine"]][prefix+"time"], b, fillvalue=0)]
                        ## you have what is in engines.json so far

    for prefix in circuits:
        data["ferrari"][prefix+"time"]= [a/(b if b>0 else 1) for a,b in zip(data["ferrari"][prefix+"time"],(data["ferrari"][prefix+"divisor"]))]
        data["mercedes"][prefix+"time"]= [a/(b if b>0 else 1) for a,b in zip(data["mercedes"][prefix+"time"], (data["mercedes"][prefix+"divisor"]))]
        data["honda"][prefix+"time"]= [a/(b if b>0 else 1) for a,b in zip(data["honda"][prefix+"time"], (data["honda"][prefix+"divisor"]))]
        data["renault"][prefix+"time"]= [a/(b if b>0 else 1) for a,b in zip(data["renault"][prefix+"time"],(data["renault"][prefix+"divisor"]))]
        avg_lap = [(a+b+c+d)/4 for a,b,c,d in zip(data["ferrari"][prefix+"time"], data["mercedes"][prefix+"time"], data["renault"][prefix+"time"], data["honda"][prefix+"time"])]
        avg_lap=sum(avg_lap)/int(circuits[prefix]["total_laps"])
        print(prefix+" "+str(avg_lap))
    with open(exitfile, 'w') as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))





                        # if(teams[drivers[driverId]["team"]]["engine"]=="renault"):
                        #     b = [x/4 for x in drivers[driverId][prefix+"time"]]
                        # else:
                        #     b = [x/6 for x in drivers[driverId][prefix+"time"]]

#isolate2019(laptimesAllcsv, laptimes2019)
#create2019proflies(laptimes2019, processedlaptimes2019)
#modify2019profiles(processedlaptimes2019, modifiedlaptimes2019)
addEngine(modifiedlaptimes2019, teams, engines)


# write json
# with open(jsonExitFilePath, 'w') as jsonFile:
#      jsonFile.write(json.dumps(data, indent=4))
