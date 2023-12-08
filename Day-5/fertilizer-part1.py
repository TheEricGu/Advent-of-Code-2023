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
        seed_list = list(map(int, lines[0].split(':')[1].strip().split())) # create starting seed list
    elif 'map' in line:
        current_map = maps[line.split()[0].replace('-', '_')] # change the current map on lines with 'map' 
    else:
        read_map(line, current_map) # add (dst_start, src_start, src_range) into current map
def map_src_to_dest(map, number): # re-map the current number
    for dst_start, src_start, src_range in map:
        if src_start <= number <= src_start + src_range:
            return number + (dst_start - src_start)
    return number
location_list = seed_list
for map_name in map_names: # for each map, all seeds are re-mapped
    location_list = [map_src_to_dest(maps[map_name], current_number) for current_number in location_list]
print(min(location_list))