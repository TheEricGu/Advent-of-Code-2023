with open('scratchcards-input.txt', 'r') as input_file:
    lines = input_file.readlines()
card_dict = {}
card_copies = {card_number: 1 for card_number in range(1, len(lines) + 1)}
for line in (lines):
    card_info, numbers = line.split(':')
    cur_card_number = int(card_info.split()[1])
    winning_numbers, your_numbers = numbers.split('|')

    card_dict[cur_card_number] = [set(winning_numbers.strip().split()), set(your_numbers.strip().split())] 
    num_matches = len(set(winning_numbers.strip().split()) & set(your_numbers.strip().split()))

    for copy_num in range(card_copies[cur_card_number]): # for each copy of the current card
        for i in range(num_matches):
            card_copies[cur_card_number + 1 + i] += 1 # update the next num_matches cards
print(sum(card_copies.values()))

