import re
def find_numbers_only_in_data_list(data_list):
	extracted_numbers_from_string = []
	for line in data_list:
		temp = re.findall(r'\d+', line)
		extracted_numbers_from_string.append(list(map(str, temp)))
	return extracted_numbers_from_string

def find_all_numbers_in_data_list(data_list):
	string_to_digit_lookup = {'one' : '1',
		   'two' : '2',
		   'three' : '3',
		   'four' : '4',
		   'five' : '5',
		   'six' : '6',
		   'seven' : '7',
		   'eight' : '8',
		   'nine' : '9'
		   }
	original_extracted_values_from_string = []
	for line in data_list:
		temp = re.findall(r'\d+|one|two|three|four|five|six|seven|eight|nine', line)
		original_extracted_values_from_string.append(list(map(str, temp)))

	output =[]
	for line in original_extracted_values_from_string:
		numbers_per_line = []
		for number in line:
			if number.isdigit():
				numbers_per_line.append(number)
			else:
				numbers_per_line.append(string_to_digit_lookup[number])
		output.append(numbers_per_line)
	return output

def extract_and_sum_two_digits_from_line(extracted_numbers_from_string):
	extracted_two_digit_numbers = []
	for all_numbers_in_line in extracted_numbers_from_string:
		first_digit = str(all_numbers_in_line[0][0])
		last_digit = all_numbers_in_line[len(all_numbers_in_line)-1][-1]
		two_digit_number_from_line = first_digit + last_digit
		extracted_two_digit_numbers.append(int(two_digit_number_from_line))
	return sum(extracted_two_digit_numbers)

# path = '/Users/akiko/Projects/adventofcode2023/adventofcode2023/day01/partonesample.csv'
# path = '/Users/akiko/Projects/adventofcode2023/adventofcode2023/day01/parttwosample.csv'
path = '/Users/akiko/Projects/adventofcode2023/adventofcode2023/day01/input.csv'
raw_data = open(path, "r").read().splitlines()
# raw_data = ['foureight48sbkkvc17zbksgvcbb', '4sixfiveone76jctmjsxdh5jrkv', 'nine296']
# raw_data = ['mdjphcm9', 'foureightmppchbgz8lqbzqbjztwo7cksqxns', '553fivethreefour8nine']

# Part 1
# extracted_numbers_from_string = find_numbers_only_in_data_list(raw_data)
# print(extract_and_sum_two_digits_from_line(extracted_numbers_from_string))
# 55386


#Part 2
# string_to_digit = {'one' : '1',
# 		   'two' : '2',
# 		   'three' : '3',
# 		   'four' : '4',
# 		   'five' : '5',
# 		   'six' : '6',
# 		   'seven' : '7',
# 		   'eight' : '8',
# 		   'nine' : '9'
# 		   }

# extracted_original_values = []
# for line in raw_data:
# 	temp = re.findall(r'\d+|one|two|three|four|five|six|seven|eight|nine', line)
# 	extracted_original_values.append(list(map(str, temp)))

# output =[]
# for line in extracted_original_values:
# 	print(line)
# 	x = []
# 	for number in line:
# 		if number.isdigit():
# 			x.append(number)
# 		else:
# 			x.append(string_to_digit[number])
# 	output.append(x)

output = find_all_numbers_in_data_list(raw_data)
print(extract_and_sum_two_digits_from_line(output))
# 54807 IS NOT THE RIGHT ANSWER, TOO LOW

# extracted_two_digit_numbers = []
# for all_numbers_in_line in output:
# 	print(all_numbers_in_line)
# 	first_digit = str(all_numbers_in_line[0][0])
# 	last_digit = all_numbers_in_line[len(all_numbers_in_line)-1][-1]
# 	two_digit_number_from_line = first_digit + last_digit
# 	extracted_two_digit_numbers.append(int(two_digit_number_from_line))


# troubleshooting
# count = 0
# while count < 1000:
# 	print(raw_data[count], extracted_original_values[count], output[count], extracted_two_digit_numbers[count])
# 	count+=1

# print(sum(extracted_two_digit_numbers))