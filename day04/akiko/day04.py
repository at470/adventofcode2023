import os 

# def split_on_colon(input):
#     x = []
#     for i in input:
#         split_input = i.split(':')
#         x.append(split_input)
#     return x

# path = os.path.join(os.path.dirname(__file__), './sample.csv')
path = os.path.join(os.path.dirname(__file__), './input.csv')
with open(path,"r") as f:
    input = f.read().splitlines()

# Data cleaning
temp1 = []
for card in input:
	split_card = card.split(': ')
	temp1.append(split_card)
# [['Card 1', '41 48 83 86 17 | 83 86  6 31 17  9 48 53'], ['Card 2', '13 32 20 16 61 | 61 30 68 82 17 32 24 19'], ['Card 3', ' 1 21 53 59 44 | 69 82 63 72 16 21 14  1'], ['Card 4', '41 92 73 84 69 | 59 84 76 51 58  5 54 83'], ['Card 5', '87 83 26 28 32 | 88 30 70 12 93 22 82 36'], ['Card 6', '31 18 13 56 72 | 74 77 10 23 35 67 36 11']]

temp2 = []
for i in temp1:
	temp2.append(i[1])
# ['41 48 83 86 17 | 83 86  6 31 17  9 48 53', '13 32 20 16 61 | 61 30 68 82 17 32 24 19', ' 1 21 53 59 44 | 69 82 63 72 16 21 14  1', '41 92 73 84 69 | 59 84 76 51 58  5 54 83', '87 83 26 28 32 | 88 30 70 12 93 22 82 36', '31 18 13 56 72 | 74 77 10 23 35 67 36 11']

temp3 = []
for i in temp2:
	temp3.append(i.split(' | '))
# [['41 48 83 86 17', '83 86  6 31 17  9 48 53'], ['13 32 20 16 61', '61 30 68 82 17 32 24 19'], [' 1 21 53 59 44', '69 82 63 72 16 21 14  1'], ['41 92 73 84 69', '59 84 76 51 58  5 54 83'], ['87 83 26 28 32', '88 30 70 12 93 22 82 36'], ['31 18 13 56 72', '74 77 10 23 35 67 36 11']]

# handle double whitespaces
temp4 = []
for i in temp3:
	foo = []
	for string in i:
		cleaned_string = ' '.join(string.split())
		foo.append(cleaned_string)
	temp4.append(foo)
# [['41 48 83 86 17', '83 86 6 31 17 9 48 53'], ['13 32 20 16 61', '61 30 68 82 17 32 24 19'], ['1 21 53 59 44', '69 82 63 72 16 21 14 1'], ['41 92 73 84 69', '59 84 76 51 58 5 54 83'], ['87 83 26 28 32', '88 30 70 12 93 22 82 36'], ['31 18 13 56 72', '74 77 10 23 35 67 36 11']]

all_scratchcards = []
for i in temp4:
	bar = []
	for j in i:
		xs = j.split(' ')
		s = [int(x) for x in xs]
		bar.append(s)
	all_scratchcards.append(bar)

# [[[41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]], [[13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19]], [[1, 21, 53, 59, 44], [69, 82, 63, 72, 16, 21, 14, 1]], [[41, 92, 73, 84, 69], [59, 84, 76, 51, 58, 5, 54, 83]], [[87, 83, 26, 28, 32], [88, 30, 70, 12, 93, 22, 82, 36]], [[31, 18, 13, 56, 72], [74, 77, 10, 23, 35, 67, 36, 11]]]


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
	if num_matches == 0:
		points = 0
	if num_matches > 1:
		count = 1
		while count in range(num_matches):
			points = points * 2
			count+= 1
	return points

# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# card = [[41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]]
# all_scratchcards = [[[41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]], 
# 			 [[13, 32, 20, 16, 61],[61, 30, 68, 82, 17, 32, 24, 19]]]

total_matches_per_card = []
for card in all_scratchcards:
	total_matches_per_card.append(number_of_matches_for_card(card))

cumulative_points = 0
for each_match in total_matches_per_card:
	cumulative_points = cumulative_points + calculate_points(each_match)
print(cumulative_points)
# 18653