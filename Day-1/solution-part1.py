input = open('input.txt', 'r')
lines = input.readlines()
sum = 0
for line in lines:
    firstDigit = 0
    lastDigit = len(line) - 1
    while firstDigit < len(line):
        if line[firstDigit].isnumeric():
            break
        else:
            firstDigit += 1
    while lastDigit > 0:
        if line[lastDigit].isnumeric():
            break
        else:
            lastDigit -= 1
    sum += int(line[firstDigit] + line[lastDigit])
print(sum)