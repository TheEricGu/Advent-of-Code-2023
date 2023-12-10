with open('toyboats-input.txt', 'r') as input_file:
    lines = input_file.readlines()
times = list(map(int,lines[0].split(':')[1].split()))
distances = list(map(int,lines[1].split(':')[1].split()))
win_methods = [sum(1 for boat_speed in range(1, 1 + times[race]) if boat_speed * (times[race] - boat_speed) > distances[race]) for race in range(len(times))]
result = 1
for mult in win_methods:
    result *= mult
print(result)