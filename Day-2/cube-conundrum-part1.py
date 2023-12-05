input = open('cube-conundrum-input.txt', 'r')
lines = input.readlines()
id_sum = 0
for line in lines:
    line_split = line.split(': ')
    game_number = int(line_split[0][5:])
    game = line_split[1].split(' ')
    valid_game = True
    for i in range(len(game)):
        if 'red' in game[i] and int(game[i-1]) > 12:
            valid_game = False
            break
        elif 'green' in game[i] and int(game[i-1]) > 13:
            valid_game = False
            break
        elif 'blue' in game[i] and int(game[i-1]) > 14:
            valid_game = False
            break
    if valid_game:
        id_sum += game_number
print(id_sum)