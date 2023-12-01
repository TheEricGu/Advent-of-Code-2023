input = open('input.txt', 'r')
lines = input.readlines()
number_mapping = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
sum = 0
for line in lines:
    firstDigitIndex, lastDigitIndex = len(line), 0
    for number_key in number_mapping.keys():
        firstDigitFindIndex = line.find(number_key)
        if firstDigitFindIndex > -1 and firstDigitFindIndex < firstDigitIndex:
            firstDigitIndex = firstDigitFindIndex
            firstDigit = number_mapping[number_key]
    for number_key in number_mapping.keys():
        lastDigitFindIndex = line.rfind(number_key)
        if lastDigitFindIndex > -1 and lastDigitFindIndex >= lastDigitIndex:
            lastDigitIndex = lastDigitFindIndex
            lastDigit = number_mapping[number_key]
    sum += int(firstDigit + lastDigit)
print(sum)