total_matches_per_card = []
def number_of_matches_for_card(card):
	winning_numbers = card[0]
	my_scratchcard = card[1]
	num_matches = 0
	for index, winning_number in enumerate(winning_numbers):
		for j, scratchcard_num in enumerate(my_scratchcard):
			if my_scratchcard[j] == winning_numbers[index]:
				num_matches += 1
	return num_matches

def calculate_points(num_matches):
	points = 1
	if num_matches > 1:
		count = 1
		while count in range(num_matches):
			points = points * 2
			count+= 1
	return points

# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
card = [[41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]]

all_scratchcards = [[[41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]], 
			 [[13, 32, 20, 16, 61],[61, 30, 68, 82, 17, 32, 24, 19]]]
for card in all_scratchcards:
	total_matches_per_card.append(number_of_matches_for_card(card))

cumulative_points = 0
for each_match in total_matches_per_card:
	cumulative_points = cumulative_points + calculate_points(each_match)
print(cumulative_points)