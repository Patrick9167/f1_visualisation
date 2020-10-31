import csv
import json
from itertools import zip_longest
import numpy as np


## The data to use:
# driverID (lap_times.csv)
# constructorID (results.csv)
# lap# (lap_times.csv)
# laps since pitstop (pit_stops.csv & lap_times.csv)
# pos (lap_times.csv)
# 
# *time/milliseconds* (lap_times.csv)
# *q_times* (qualifying.csv)

def createLaptimeDataset(exitfile):
    data = []
    pits={}
    # Get pitstops and the lap# into dict
    with open("f1_data_csv/pit_stops.csv") as csvFile:
        p_csv = csv.DictReader(csvFile)
        for p in p_csv:
            if p["raceId"]=="1010":
                if p["driverId"] not in pits:
                    pits[p["driverId"]]={}
                pits[p["driverId"]][p["stop"]]=p["lap"]
    print(pits)
    teams_and_engines={}
    # open constructors csv
    with open("f1_data_csv/results.csv") as csvFile:
        results = csv.DictReader(csvFile)
        for r in results:
            if r["raceId"]=="1010":
                d_id = r["driverId"]
                if d_id not in teams_and_engines:
                    teams_and_engines[d_id]={}
                teams_and_engines[d_id]["team"]=r["constructorId"]
                t = int(teams_and_engines[d_id]["team"])
                if t==131 or t==211 or t==3:
                    teams_and_engines[d_id]["engine"]="0"
                elif t==6 or t==210 or t==51:
                    teams_and_engines[d_id]["engine"]="1"
                elif t==4 or t==1:        
                    teams_and_engines[d_id]["engine"]="2"
                elif t==9 or t==5:
                    teams_and_engines[d_id]["engine"]="3"
                else:
                    teams_and_engines[d_id]["engine"]="4"
                

                
    # open laptimes csv
    with open("f1_data_csv/lap_times.csv") as csvFile:
        laptimes_csv = csv.DictReader(csvFile)
        # open csv file to write to
        with open('aus_2019.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            # set headers
            writer.writerow(["driverId", "constructorId", "engineId", "lap#","pit", "laps after pit", "pos", "time(min)", "time(ms)"])
            # loop through laps for race 1010
            for lap in laptimes_csv:
                if lap["raceId"]=="1010":
                    current_lap = int(lap["lap"])
                    d_id=lap["driverId"]
                    did_pit=0
                    ## calculate laps since a pitstop (start of race is treated as pitstop)
                    if d_id in pits:
                        if "3" in pits[d_id] and current_lap>=int(pits[d_id]["3"]):
                            pitlap=int(pits[d_id]["3"])
                            if current_lap==pitlap:did_pit=1 
                            since_box = current_lap-pitlap
                        elif "2" in pits[d_id] and current_lap>=int(pits[d_id]["2"]):
                            pitlap=int(pits[d_id]["2"])
                            if current_lap==pitlap:did_pit=1 
                            since_box = current_lap-pitlap
                        elif "1" in pits[d_id] and current_lap>=int(pits[d_id]["1"]):
                            pitlap=int(pits[d_id]["1"])
                            if current_lap==pitlap:did_pit=1 
                            since_box = current_lap-pitlap
                        else:
                            since_box = current_lap
                    else:
                        since_box=-1
                    
                    ## write data line to csv
                    writer.writerow([d_id,teams_and_engines[d_id]["team"],teams_and_engines[d_id]["engine"],
                    lap["lap"],did_pit, str(since_box),
                    lap["position"], lap["time"], lap["milliseconds"]])
                    
        
    # with open(exitfile, 'w') as csvFile:
    #      csvFile.write(json.dumps(data, indent=4))

createLaptimeDataset("predictors.csv")