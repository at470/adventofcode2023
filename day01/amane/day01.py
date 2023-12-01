# %%
# import os
import re

# %%
# print(os.getcwd())

# %%
# Create functions
def sum_first_last_num(element:str):
    """
    Given a string, will find first and last instance a digit in integer representation is found 
    and returns the two digits appended as a string
    """
    # Get first digit
    find_first = re.search(r"\d", element)
    first_num = find_first.group(0)

    #Get last digit
    reverse_element = element[::-1]
    find_last = re.search(r"\d", reverse_element)
    last_num = find_last.group(0)

    # Get sum of digits, and capture in new list
    total = first_num + last_num

    print("For element {}, first digit is {}, last digit is {}, and total is {}".format(element, first_num, last_num, total))

    return total

# %%
## PART 1
# Import libraries
input_file = open("input", "r")
raw_list = []
for line in input_file.readlines():
    # Capture each element as line, ignore new line character
    raw_list.append(line.splitlines()[0]) 
    # print(line) #TODO DELETE ME
input_file.close()

# print(raw_list) #TODO DELETE ME

# %%
# Get first and last digits, sum and capture in new list
totals_list = []
for element in raw_list:
    total = sum_first_last_num(element)
    totals_list.append(int(total))

# %%
# Get and print grand total
grand_total = sum(totals_list)
print(grand_total)

# %%
## PART 2

# %%
# Convert text based numbers to numbers for each line in list

# Create dict converter for string to integer value
num_dict = [
    {'num_str' : 'one', 'int_str': '1'},
    {'num_str' : 'two', 'int_str': '2'},
    {'num_str' : 'three', 'int_str': '3'},
    {'num_str' : 'four', 'int_str': '4'},
    {'num_str' : 'five', 'int_str': '5'},
    {'num_str' : 'six', 'int_str': '6'},
    {'num_str' : 'seven', 'int_str': '7'},
    {'num_str' : 'eight', 'int_str': '8'},
    {'num_str' : 'nine', 'int_str': '9'},
]
# print(num_dict) #TODO Delete me

# %%
# #TODO DELETE ME. Find examples of multi matches
# index_with_multi_match = []
# for idx, line in enumerate(raw_list):
#     for dict in num_dict:
#         num_str = dict['num_str']
#         int_str = dict['int_str']
#         # print('For dict {}, string is {} and int is {}'.format(dict, num_str, int_str)) #TODO DELETE ME

#         find_all_num = re.findall(num_str,line)
#         if len(find_all_num) > 1:
#             print(idx)
#             # More than one match found
#             print(line)
#             index_with_multi_match.append(idx)
#         else:
#             num_line_with_multi_match.append(0)
            

# print(index_with_multi_match)

# %%
# #TODO DELETE ME. Create test list

# test_list = raw_list[0:12]
# print(test_list)

# %%
# For each line in list, run through check against num_dict, and replace with integer
num_line_with_multi_match = []
fixed_list = []
# for idx,line in enumerate(test_list): #TODO DELETE TESTING
for idx,line in enumerate(raw_list):
    print('For line {}, at index {}'.format(line,idx))
    for dict in num_dict:
        num_str = dict['num_str']
        int_str = dict['int_str']
        # print('For dict {}, string is {} and int is {}'.format(dict, num_str, int_str)) #TODO DELETE ME
        
        # Check for a match and replace with int if found
        check_match = re.search(num_str,line)
        if check_match is not None:
            new_line = line.replace(num_str,int_str)
            print('Within string {}, the value {} was found. This makes the new line {}'.format(line, num_str, new_line)) #TODO Delete me
            line = new_line # Replace the line value
    
    fixed_list.append(line)
    print('After updating, the line at index {} is now {}'.format(idx, line))
        

# %%
# print('Compare {} with {}'.format(raw_list[11], fixed_list[11])) #TODO Delete me

# %%
#TODO DELETE ME. Compare converted lists
print(raw_list)
# print(test_list)#TODO DELETE ME
print(fixed_list)

# %%
# Get first and last digits, sum and capture in new list
totals_list = []
for element in fixed_list:
    total = sum_first_last_num(element)
    totals_list.append(int(total))

# %%
print(len(raw_list))
print(len(fixed_list))
print(len(totals_list))

# %%
print(fixed_list)
print(totals_list)

# %%
# Get and print grand total
grand_total = sum(totals_list)
print(grand_total)

#TODO DELETE ME
#Get 54983, but too low

# %%


# %%


# %%



