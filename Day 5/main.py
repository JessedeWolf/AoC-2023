oldSeeds = ['3127166940', '3265086325', '86449584', '1581539098', '205205726', '3646327835', '184743451', '2671979893', '17148151', '305618297', '40401857', '2462071712', '203075200', '358806266', '131147346', '1802185716', '538526744', '635790399', '705979250']
# oldSeeds = ['79', '14', '55', '13']
oldSeeds = [int(seed) for seed in oldSeeds]

with open("Day 5/input.txt", "r") as file:
    content = file.read()
seeds = []
start = oldSeeds[0]
uppies = oldSeeds[1]
for i in range(start, start + uppies):
    seeds.append(i)


print("List done")

oldSeeds = oldSeeds[2:]

seeds = [int(seed) for seed in seeds]

maps = [map.strip() for map in content.split('\n\n')]
seeds_to_soil_map = None
for map_str in maps:
    lines = map_str.split('\n')
    header = lines[0].strip(':')
    if header == 'seed-to-soil map':
        seeds_to_soil_map = [list(map(int, line.split())) for line in lines[1:]]
        break

for seed in seeds:
    new_seed = seed
    for entry in seeds_to_soil_map:
        lower_bound = entry[1]
        upper_bound = lower_bound + entry[2]
        if lower_bound <= seed <= upper_bound:
            difference = entry[0] - entry[1]
            new_seed = seed + difference
            break
    seeds[seeds.index(seed)] = new_seed

seeds_to_fertilizer_map = None
for map_str in maps:
    lines = map_str.split('\n')
    header = lines[0].strip(':')
    if header == 'soil-to-fertilizer map':
        seeds_to_fertilizer_map = [list(map(int, line.split())) for line in lines[1:]]
        break

for seed in seeds:
    new_seed = seed
    for entry in seeds_to_fertilizer_map:
        lower_bound = entry[1]
        upper_bound = lower_bound + entry[2]
        if lower_bound <= seed <= upper_bound:
            difference = entry[0] - entry[1]
            new_seed = seed + difference
            break
    seeds[seeds.index(seed)] = new_seed

fertilizer_to_water_map = None
for map_str in maps:
    lines = map_str.split('\n')
    header = lines[0].strip(':')
    if header == 'fertilizer-to-water map':
        fertilizer_to_water_map = [list(map(int, line.split())) for line in lines[1:]]
        break

for seed in seeds:
    new_seed = seed
    for entry in fertilizer_to_water_map:
        lower_bound = entry[1]
        upper_bound = lower_bound + entry[2]
        if lower_bound <= seed <= upper_bound:
            difference = entry[0] - entry[1]
            new_seed = seed + difference
            break
    seeds[seeds.index(seed)] = new_seed

water_to_light_map = None
for map_str in maps:
    lines = map_str.split('\n')
    header = lines[0].strip(':')
    if header == 'water-to-light map':
        water_to_light_map = [list(map(int, line.split())) for line in lines[1:]]
        break

for seed in seeds:
    new_seed = seed
    for entry in water_to_light_map:
        lower_bound = entry[1]
        upper_bound = lower_bound + entry[2]
        if lower_bound <= seed <= upper_bound:
            difference = entry[0] - entry[1]
            new_seed = seed + difference
            break
    seeds[seeds.index(seed)] = new_seed

light_to_temperature_map = None
for map_str in maps:
    lines = map_str.split('\n')
    header = lines[0].strip(':')
    if header == 'light-to-temperature map':
        light_to_temperature_map = [list(map(int, line.split())) for line in lines[1:]]
        break

for seed in seeds:
    new_seed = seed
    for entry in light_to_temperature_map:
        lower_bound = entry[1]
        upper_bound = lower_bound + entry[2]
        if lower_bound <= seed <= upper_bound:
            difference = entry[0] - entry[1]
            new_seed = seed + difference
            break
    seeds[seeds.index(seed)] = new_seed

temperature_to_humidity_map = None
for map_str in maps:
    lines = map_str.split('\n')
    header = lines[0].strip(':')
    if header == 'temperature-to-humidity map':
        temperature_to_humidity_map = [list(map(int, line.split())) for line in lines[1:]]
        break

for seed in seeds:
    new_seed = seed
    for entry in temperature_to_humidity_map:
        lower_bound = entry[1]
        upper_bound = lower_bound + entry[2]
        if lower_bound <= seed <= upper_bound:
            difference = entry[0] - entry[1]
            new_seed = seed + difference
            break
    seeds[seeds.index(seed)] = new_seed

humidity_to_location_map = None
for map_str in maps:
    lines = map_str.split('\n')
    header = lines[0].strip(':')
    if header == 'humidity-to-location map':
        humidity_to_location_map = [list(map(int, line.split())) for line in lines[1:]]
        break

for seed in seeds:
    new_seed = seed
    for entry in humidity_to_location_map:
        lower_bound = entry[1]
        upper_bound = lower_bound + entry[2]
        if lower_bound <= seed <= upper_bound:
            difference = entry[0] - entry[1]
            new_seed = seed + difference
            break
    seeds[seeds.index(seed)] = new_seed
print(f"{min(seeds)} is minimum location")

