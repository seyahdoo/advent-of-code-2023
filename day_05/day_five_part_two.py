
def main():
    with open("maps.txt", encoding="utf-8") as f:
        lines = f.readlines()
    lines = list(map(lambda x: x.strip().strip("\ufeff"), lines))

    def pairwise(iterable):
        "s -> (s0, s1), (s2, s3), (s4, s5), ..."
        a = iter(iterable)
        return zip(a, a)

    seed_ranges = list(pairwise(list(map(lambda x: int(x), lines[0].split(":")[1].strip().split()))))
    seed_to_soil = list(map(lambda x: (int(x.split()[0]), int(x.split()[1]),int(x.split()[2])), lines[3:31]))
    soil_to_fertilizer = list(map(lambda x: (int(x.split()[0]), int(x.split()[1]),int(x.split()[2])), lines[33:43]))
    fertilizer_to_water = list(map(lambda x: (int(x.split()[0]), int(x.split()[1]),int(x.split()[2])), lines[45:54]))
    water_to_light = list(map(lambda x: (int(x.split()[0]), int(x.split()[1]),int(x.split()[2])), lines[56:79]))
    light_to_temprature = list(map(lambda x: (int(x.split()[0]), int(x.split()[1]),int(x.split()[2])), lines[81:113]))
    temprature_to_humidity = list(map(lambda x: (int(x.split()[0]), int(x.split()[1]),int(x.split()[2])), lines[115:160]))
    humidity_to_location = list(map(lambda x: (int(x.split()[0]), int(x.split()[1]),int(x.split()[2])), lines[162:211]))
    list_of_maps = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temprature, temprature_to_humidity, humidity_to_location]
    
    ranges = seed_ranges
    for maps in list_of_maps:
        ranges = convert_ranges(maps, ranges)
    
    lowest = find_lowest_on_ranges(ranges)
    print(lowest)
    return 
    
def convert_ranges(maps, ranges):
    new_ranges = []
    for map in maps:
        destination_range_start = map[0]
        source_range_start = map[1]
        range_length = map[2]
        
        # if source >= source_range_start and source <= source_range_start + range_length:
        #     return source - source_range_start + destination_range_start
    return ranges

def find_lowest_on_ranges(ranges):
    return 0
      
if __name__ == '__main__':
    main()        