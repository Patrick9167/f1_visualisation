import csv
import json
from itertools import zip_longest
import numpy as np

raceCSV="f1_data_csv/races.csv"
laptimesCSV="f1_data_csv/lap_times.csv"
resultsCSV="f1_data_csv/results.csv"
circuitCSV="f1_data_csv/circuits.csv"


def createLaptimeDataset(year: str):
    data = {}
    exitfile="../"+year+"f1data.json"

    raceIds=[]

    ## Adding raceId objects and circuit info
    # "1010": {
    #   name
    #   round
    #   circuitId 
    # }
    with open(raceCSV) as csvFile:
        races=csv.DictReader(csvFile)
        for r in races:
            if r["year"]==year:
                raceId = r["raceId"] 
                raceIds.append(raceId)
                data[raceId]={}
                data[raceId]["name"]=r["name"]
                # data[raceId]["round"]=r["round"]
                # data[raceId]["circuitId"]=r["circuitId"]
    
    # with open(exitfile, 'w') as jsonFile:
    #     jsonFile.write(json.dumps(data, indent=4))

    firstRace=int(raceIds[0])
    lastRace=int(raceIds[len(raceIds)-1])
    
    ## Adding driverId objects and laptimes, lapNumber, lapPosition
    # "1010": {
    #   name
    #   round
    #   circuitId 
    #   "1": {
    #       laptimes
    #       lapNumber
    #       position  
    #   }
    # }
    with open(laptimesCSV) as csvFile:
        laptimes=csv.DictReader(csvFile)
        for l in laptimes:
            raceId = int(l["raceId"])
            if raceId>=firstRace and raceId<=lastRace:
                if l["driverId"] not in data[l["raceId"]]:
                    data[l["raceId"]][l["driverId"]]={}
                    data[l["raceId"]][l["driverId"]]["laptimes"]=[] 
                    data[l["raceId"]][l["driverId"]]["lapNumber"]=[]  
                    data[l["raceId"]][l["driverId"]]["position"]=[]   
                data[l["raceId"]][l["driverId"]]["laptimes"].append(l["time"])
                data[l["raceId"]][l["driverId"]]["lapNumber"].append(l["lap"])
                data[l["raceId"]][l["driverId"]]["position"].append(l["position"])
       # print(data)
    
    # Add constructorId from results.csv
    # here you can add grid position/status(incident)/number/fastestLap/fLTime/fLSpeed
    #
    # "1010": {
    #   name:str
    #   round: str
    #   circuitId : str
    #   "1": {
    #       laptimes: []
    #       lapNumber: []
    #       position: []
    #       constructorId:str
    #       finalPosition:str  
    #       totalCompletedLaps:str
    #   }
    # }
    with open(resultsCSV) as csvFile:
        results=csv.DictReader(csvFile)
        for r in results:
            raceId = int(r["raceId"])
            if raceId>=firstRace and raceId<=lastRace:
                if r["driverId"] not in data[r["raceId"]]:
                    data[r["raceId"]][r["driverId"]]={}
           ##     if "constructor" not in data[r["raceId"]][r["driverId"]]:
                data[r["raceId"]][r["driverId"]]["constructor"] = r["constructorId"] 
           ##     if "finalPosition" not in data[r["raceId"]][r["driverId"]]:
                data[r["raceId"]][r["driverId"]]["finalPosition"] = r["position"] 
                data[r["raceId"]][r["driverId"]]["totalCompletedLaps"] = r["laps"] 
    with open(exitfile, 'w') as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))

createLaptimeDataset("2019")