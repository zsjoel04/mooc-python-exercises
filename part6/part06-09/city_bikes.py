import math

def list_from_csv(filename):                   
    result = []
    with open(filename) as new_file:
        for line in new_file:
            line = line.strip()
            line = line.split(";")
            result.append(line)
    return result



def get_station_data(filename: str):           
    result_dict = {}
    my_list = list_from_csv(filename)
    for lista in my_list:
        if not lista[0] == "Longitude":
            result_dict[lista[3]] = (float(lista[0]), float(lista[1]))
    return result_dict

def distance(stations: dict, station1: str, station2: str):    
    longitude1 = stations[station1][0]
    latitude1 = stations[station1][1]
    longitude2 = stations[station2][0]
    latitude2 = stations[station2][1]
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km




def greatest_distance(stations: dict):
    greatest = 0
    for key in stations:
        for station in stations:
            result = distance(stations, key, station)
            if result > greatest:
                saved_station1 = key
                saved_station2 = station
                greatest = result
    return saved_station1, saved_station2, greatest
        

