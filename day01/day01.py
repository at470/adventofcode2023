import re

# path = '/Users/akiko/Projects/adventofcode2023/adventofcode2023/day01/partonesample.csv'
path = '/Users/akiko/Projects/adventofcode2023/adventofcode2023/day01/input.csv'
raw_data = open(path, "r").read().splitlines()
# raw_data = ['foureight48sbkkvc17zbksgvcbb', '4sixfiveone76jctmjsxdh5jrkv', 'nine296']

def find_numbers_in_data_list(data_list):
	extracted_numbers_from_string = []
	for line in data_list:
		temp = re.findall(r'\d+', line)
		extracted_numbers_from_string.append(list(map(str, temp)))
	return extracted_numbers_from_string

def extract_two_digits_from_line(extracted_numbers_from_string):
	extracted_two_digit_numbers = []
	for all_numbers_in_line in extracted_numbers_from_string:
		if len(all_numbers_in_line[0]) > 1:
			first_digit = str(all_numbers_in_line[0][0])
		else:
			first_digit = str(all_numbers_in_line[0])
		last_digit = all_numbers_in_line[len(all_numbers_in_line)-1][-1]
		two_digit_number_from_line = first_digit + last_digit
		extracted_two_digit_numbers.append(int(two_digit_number_from_line))
	return sum(extracted_two_digit_numbers)

# Part 1
extracted_numbers_from_string = find_numbers_in_data_list(raw_data)
print(extract_two_digits_from_line(extracted_numbers_from_string))
# 55386


#Part 2

#Approach
#Take string and look for strings that are numbers
#Transpose string -> int
#WANT: list of digits per line of input
#Then apply same method as Part 1 -> TODO: make Part1 into a function, apply to output for Part 2