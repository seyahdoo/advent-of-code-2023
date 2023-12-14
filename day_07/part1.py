import math


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
    with open("input.txt", encoding="utf-8") as f:
        lines = f.readlines()
    lines = list(map(lambda x: x.strip().strip("\ufeff"), lines))
    times = list(map(lambda x: int(x), lines[0].split(":")[1].strip().split()))
    distances = list(map(lambda x: int(x), lines[1].split(":")[1].strip().split()))
    
    get_number_of_ways_to_defeat(7, 9)
    
    sum = 1
    for time, distance in zip(times, distances):
        sum *= get_number_of_ways_to_defeat(time, distance)
    print(sum)
    return 

def get_number_of_ways_to_defeat(total_time, current_record):
    x_bot = (total_time / 2) - math.sqrt(-current_record + (math.pow(total_time, 2) / 4))
    x_top = (total_time / 2) + math.sqrt(-current_record + (math.pow(total_time, 2) / 4))
    x_top = math.floor(x_top)
    x_bot = math.ceil(x_bot)
    return x_top - x_bot  + 1
    
        
if __name__ == '__main__':
    main()        