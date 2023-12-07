with open('scratchcards-input.txt', 'r') as input_file:
    sum = 0
    for line in input_file.readlines():
        winning_numbers, your_numbers = line.split(':')[1].split('|')
        common_numbers_count = len(set(winning_numbers.strip().split()) & set(your_numbers.strip().split()))
        print(common_numbers_count)
        if common_numbers_count > 0:
            sum += 2 ** (common_numbers_count - 1)
    print(sum)