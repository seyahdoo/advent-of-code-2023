﻿
def source_to_destination(maps, source):
    for map in maps:
        destination_range_start = map[0]
        source_range_start = map[1]
        range_length = map[2]
        if source >= source_range_start and source <= source_range_start + range_length:
            return source - source_range_start + destination_range_start
    return source

def get_location_from_seed(list_of_maps, seed):
    value = seed
    for maps in list_of_maps:
        value = source_to_destination(maps, value)
    return value

def main():
    with open("maps.txt", encoding="utf-8") as f:
        lines = f.readlines()
    lines = list(map(lambda x: x.strip().strip("\ufeff"), lines))
    seeds = list(map(lambda x: int(x), lines[0].split(":")[1].strip().split()))
    seed_to_soil = list(map(lambda x: (int(x.split()[0]), int(x.split()[1]),int(x.split()[2])), lines[3:31]))
    soil_to_fertilizer = list(map(lambda x: (int(x.split()[0]), int(x.split()[1]),int(x.split()[2])), lines[33:43]))
    fertilizer_to_water = list(map(lambda x: (int(x.split()[0]), int(x.split()[1]),int(x.split()[2])), lines[45:54]))
    water_to_light = list(map(lambda x: (int(x.split()[0]), int(x.split()[1]),int(x.split()[2])), lines[56:79]))
    light_to_temprature = list(map(lambda x: (int(x.split()[0]), int(x.split()[1]),int(x.split()[2])), lines[81:113]))
    temprature_to_humidity = list(map(lambda x: (int(x.split()[0]), int(x.split()[1]),int(x.split()[2])), lines[115:160]))
    humidity_to_location = list(map(lambda x: (int(x.split()[0]), int(x.split()[1]),int(x.split()[2])), lines[162:211]))
    list_of_maps = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temprature, temprature_to_humidity, humidity_to_location]
    locations = list(map(lambda x: get_location_from_seed(list_of_maps, x), seeds))
    locations.sort()
    print(locations[0])
    return 
    
        
if __name__ == '__main__':
    main()        