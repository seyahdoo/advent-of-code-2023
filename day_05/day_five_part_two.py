import multiprocessing

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

    def pairwise(iterable):
        "s -> (s0, s1), (s2, s3), (s4, s5), ..."
        a = iter(iterable)
        return zip(a, a)
    
    # do it with ranges

    seed_to_soil = list(map(lambda x: (int(x.split()[0]), int(x.split()[1]),int(x.split()[2])), lines[3:31]))
    soil_to_fertilizer = list(map(lambda x: (int(x.split()[0]), int(x.split()[1]),int(x.split()[2])), lines[33:43]))
    fertilizer_to_water = list(map(lambda x: (int(x.split()[0]), int(x.split()[1]),int(x.split()[2])), lines[45:54]))
    water_to_light = list(map(lambda x: (int(x.split()[0]), int(x.split()[1]),int(x.split()[2])), lines[56:79]))
    light_to_temprature = list(map(lambda x: (int(x.split()[0]), int(x.split()[1]),int(x.split()[2])), lines[81:113]))
    temprature_to_humidity = list(map(lambda x: (int(x.split()[0]), int(x.split()[1]),int(x.split()[2])), lines[115:160]))
    humidity_to_location = list(map(lambda x: (int(x.split()[0]), int(x.split()[1]),int(x.split()[2])), lines[162:211]))
    list_of_maps = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temprature, temprature_to_humidity, humidity_to_location]

    lowest_location = 0
    seeds = []
    seeds_info = list(map(lambda x: int(x), lines[0].split(":")[1].strip().split()))
    threads = []
    thread_results = []
    result_lock = multiprocessing.Lock()
    
    for seed_start, seed_length in pairwise(seeds_info):
        def find_lowest_location(list_of_maps, seed_start, seed_length, thread_results:list):
            lowest_location_in_thread = 0
            seeds = range(seed_start, seed_start + seed_length)
            for seed in seeds:
                location = get_location_from_seed(list_of_maps, seed)
                if location <= lowest_location_in_thread:
                    lowest_location_in_thread = location
            with result_lock:
                thread_results.append(lowest_location_in_thread)
            print("done with thread")
            return
        max_length = 10000000
        
        while seed_length > max_length:
            thread = multiprocessing.Process(target=find_lowest_location, args=(list_of_maps, seed_start, max_length, thread_results))
            threads.append(thread)
            thread.start()
            seed_start += max_length
            seed_length -= max_length
        thread = multiprocessing.Process(target=find_lowest_location, args=(list_of_maps, seed_start, seed_length, thread_results))
        threads.append(thread)
        thread.start()
    
    total_thread_count = len(threads)
    done_thread_count = 0
    print(total_thread_count)
    for thread in threads:
        thread.join()
        done_thread_count += 1
        print(done_thread_count/done_thread_count)

    thread_results.sort()
    print(thread_results[0])
    return 
    
        
if __name__ == '__main__':
    main()        