input = open('cube-conundrum-input.txt', 'r')
lines = input.readlines()
power_sum = 0
for line in lines:
    line_split = line.split(': ')
    game_number = int(line_split[0][5:])
    game = line_split[1].split(' ')
    red = green = blue = 0
    for i in range(len(game)):
        if 'red' in game[i] and int(game[i-1]) > red:
            red = int(game[i-1])
        elif 'green' in game[i] and int(game[i-1]) > green:
            green = int(game[i-1])
        elif 'blue' in game[i] and int(game[i-1]) > blue:
            blue = int(game[i-1])
    power_sum += (red * green * blue)
print(power_sum)