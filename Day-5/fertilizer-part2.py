with open('fertilizer-input.txt', 'r') as input_file:
    lines = input_file.readlines()
map_names = ['seed_to_soil', 'soil_to_fertilizer', 'fertilizer_to_water', 
                 'water_to_light', 'light_to_temperature', 'temperature_to_humidity',
                 'humidity_to_location']
maps = {name: set() for name in map_names} # initialize maps as empty sets
def read_map(line, current_map): # ingest map information into current map
    if list(line.split()) != []:
        dst_start, src_start, src_range = map(int, line.split())
        current_map.add((dst_start, src_start, src_range))
current_map = None
for line in lines:
    if 'seeds' in line:
        seed_ranges_list = list(map(int, lines[0].split(':')[1].strip().split())) # create starting seed list
        seed_ranges = set()
        for seed_index in range(len(seed_ranges_list)):
            if seed_index % 2 == 0:
                seed_ranges.add((seed_ranges_list[seed_index], seed_ranges_list[seed_index] + seed_ranges_list[seed_index+1]))
    elif 'map' in line:
        current_map = maps[line.split()[0].replace('-', '_')] # change the current map on lines with 'map' 
    else:
        read_map(line, current_map) # add (dst_start, src_start, src_range) into current map
def map_src_to_dest(map, number): # re-map the current number
    for dst_start, src_start, src_range in map:
        if dst_start <= number <= dst_start + src_range:
            return number + (src_start - dst_start)
    return number
map_names.reverse()
location_number = 0
# location_number = 26714515 # why is my answer the correct answer + 1?
seed_not_found = True
while seed_not_found: # test all location numbers from 0 until one reverse mapped location number originates from a valid seed
    location_number += 1
    current_number = location_number
    for map_name in map_names:
        current_number = map_src_to_dest(maps[map_name], current_number) 
    if any(seed_range[0] <= current_number <= seed_range[1] for seed_range in seed_ranges):
        print(location_number)
        seed_not_found = False