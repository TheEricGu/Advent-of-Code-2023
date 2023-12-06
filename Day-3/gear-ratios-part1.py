with open('gear-ratios-input.txt', 'r') as input_file:
    array = [list(line.strip()) for line in input_file.readlines()]
numbers = {(row, col): char for row, line in enumerate(array) for col, char in enumerate(line) if char.isdigit()}
symbols = [(row, col) for row, line in enumerate(array) for col, char in enumerate(line) if char in {'*', '@', '&', '=', '+', '/', '%', '#', '$', '-'}]
i = 0   
keyList = list(numbers.keys())
numberIndices = {} # key: full number, value: digit indices
while i < len(keyList): 
    number = array[keyList[i][0]][keyList[i][1]]
    indices = [keyList[i]]
    while i < len(keyList)-1 and keyList[i][1] == keyList[i+1][1]-1:
        number += (array[keyList[i+1][0]][keyList[i+1][1]])
        indices.append(keyList[i+1])
        i+=1
    if number in numberIndices:
        numberIndices[number] += indices
    else:
        numberIndices[number] = indices
    i+=1
sum = 0
for item in list(numberIndices.items()): # checks if number is valid
    numberLength = len(item[0])
    numberOccurrences = int(len(item[1])/numberLength)
    for occurrence in range(numberOccurrences): 
        for digitIndex in range(numberLength):
            row, col = item[1][numberLength * occurrence + digitIndex]
            if (any((row + deltaRow, col + deltaCol) in symbols for deltaRow in [-1, 0, 1] for deltaCol in [-1, 0, 1] if (deltaRow, deltaCol) != (0, 0))):
                sum += int(item[0])
                break  
print(sum)