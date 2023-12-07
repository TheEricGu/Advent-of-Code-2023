with open('gear-ratios-input.txt', 'r') as input_file:
    array = [list(line.strip()) for line in input_file.readlines()]
numbers = {(row, col): char for row, line in enumerate(array) for col, char in enumerate(line) if char.isdigit()}
symbols = [(row, col) for row, line in enumerate(array) for col, char in enumerate(line) if char == '*']
i = 0   
keyList = list(numbers.keys())
indicesNumber = {} # key: digit index, value: full number that digit is part of
while i < len(keyList): 
    number = array[keyList[i][0]][keyList[i][1]]
    indices = [keyList[i]]
    while i < len(keyList)-1 and keyList[i][1] == keyList[i+1][1]-1:
        number += (array[keyList[i+1][0]][keyList[i+1][1]])
        indices.append(keyList[i+1])
        i+=1
    for index in indices:
        indicesNumber[index] = number
    i+=1
sum = 0
for symbol in symbols:
    row, col = symbol
    nearbyNumbers = {indicesNumber[row + dr, col + dc] for dr in [-1, 0, 1] for dc in [-1, 0, 1] if (dr, dc) != (0, 0) and (row + dr, col + dc) in indicesNumber}
    if len(nearbyNumbers) == 2:
        sum += eval('*'.join(nearbyNumbers))
print(sum)