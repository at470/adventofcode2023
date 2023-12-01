import re
# used in part 1 only
def find_numbers_only_in_data_list(data_list):
	extracted_numbers_from_string = []
	for line in data_list:
		temp = re.findall(r'\d+', line)
		extracted_numbers_from_string.append(list(map(str, temp)))
	return extracted_numbers_from_string

# used in part 1 only
def extract_and_sum_two_digits_from_line(extracted_numbers_from_string):
	extracted_two_digit_numbers = []
	for all_numbers_in_line in extracted_numbers_from_string:
		first_digit = str(all_numbers_in_line[0][0])
		last_digit = all_numbers_in_line[len(all_numbers_in_line)-1][-1]
		two_digit_number_from_line = first_digit + last_digit
		extracted_two_digit_numbers.append(int(two_digit_number_from_line))
	return sum(extracted_two_digit_numbers)

# used in part 2
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
		temp = re.findall(r'\d{1}|one|two|three|four|five|six|seven|eight|nine', line) #only matching one digit with d{1}
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

# part 2
def find_all_numbers_backwards_in_reversed_data_list(data_list):
	reversed_string_to_digit_lookup = {'eno' : '1',
		   'owt' : '2',
		   'eerht' : '3',
		   'ruof' : '4',
		   'evif' : '5',
		   'xis' : '6',
		   'neves' : '7',
		   'thgie' : '8',
		   'enin' : '9'
		   }
	original_extracted_values_from_string = []
	for line in data_list:
		temp = re.findall(r'\d{1}|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin', line) #only matching one digit with d{1}
		original_extracted_values_from_string.append(list(map(str, temp)))
	output =[]
	for line in original_extracted_values_from_string:
		numbers_per_line = []
		for number in line:
			if number.isdigit():
				numbers_per_line.append(number)
			else:
				numbers_per_line.append(reversed_string_to_digit_lookup[number])
		output.append(numbers_per_line)
	return output

def return_list_of_one_digits(data):
	list_of_index_zero_values = []
	for i in data:
		list_of_index_zero_values.append(str(i[0]))
	return list_of_index_zero_values





# path = '/Users/akiko/Projects/adventofcode2023/adventofcode2023/day01/akiko/partonesample.csv'
# path = '/Users/akiko/Projects/adventofcode2023/adventofcode2023/day01/akiko/parttwosample.csv'
path = '/Users/akiko/Projects/adventofcode2023/adventofcode2023/day01/akiko/input.csv'
raw_data = open(path, "r").read().splitlines()



# Part 1
extracted_numbers_from_string = find_numbers_only_in_data_list(raw_data)
print(extract_and_sum_two_digits_from_line(extracted_numbers_from_string))
# 55386


# Part 2
# NB. 54807 IS NOT THE RIGHT ANSWER, TOO LOW -> had to rethink the whole approach, used reversing (thanks to Butch Wong)

all_first_digits_from_data = find_all_numbers_in_data_list(raw_data)
first_digit = return_list_of_one_digits(all_first_digits_from_data)

raw_data_reversed = []
for i in raw_data:
	raw_data_reversed.append(i[::-1])

all_last_digits_from_data = find_all_numbers_backwards_in_reversed_data_list(raw_data_reversed)
last_digit = return_list_of_one_digits(all_last_digits_from_data)

if len(first_digit) == len(last_digit):
	result = [first_digit[i]+last_digit[i] for i in range(len(first_digit))]
	print(sum(map(int, result)))

else:
	print('some error')

# 54824 is correct



#How to make this code better
#Improve the function so find_all_numbers_in_data_list and find_all_numbers_backwards_in_reversed_data_list are just one function that takes in a dictionary and a regex format
