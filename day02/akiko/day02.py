# Data cleaning -> get game data for Parts 1 and 2
def make_set_result_dict(input_result_list):
	set_result = {'red' : 0, 'green' : 0, 'blue' : 0}
	for x in input_result_list:
		# ['1', 'red']
		cube_number = x[0]
		cube_colour = x[1]
		set_result[cube_colour] = int(cube_number)
	return set_result

# Part 1
def is_game_result_invalid(bag_content, game_result):
	bag_result_comparison_var = [(bag_cube_colour, game_result[bag_cube_colour], bag_cube_num) for bag_cube_colour, bag_cube_num in bag_content.items()]
	# bag_result_comparison_var = [('red', 20, 12), ('green', 8, 13), ('blue', 6, 14)]
	for colour_comparison in bag_result_comparison_var:
		game_cube_num = colour_comparison[1]
		bag_cube_num = colour_comparison[2]
		# print(colour_comparison, game_cube_num > bag_cube_num)
		if game_cube_num > bag_cube_num:
			result = True
			return result # TODO: I don't think this bit is working - I want this function to stop and this for loop to break
		else:
			result = False
	return result

# Part 2
def get_min_cubes_per_game(game_result):
	# game_result = [{'red' : 4, 'green' : 0, 'blue' : 3}, 
# 		 {'red' : 1, 'green' : 2, 'blue' : 6}, 
# 		 {'red' : 0, 'green' : 2, 'blue' : 0}]
	min_cube_per_game = {'red' : 0, 'green' : 0, 'blue' : 0}
	for cube_results in game_result:
		# {'red' : 4, 'green' : 0, 'blue' : 3}
		if cube_results['red'] > min_cube_per_game['red']:
			min_cube_per_game['red'] = cube_results['red']
		if cube_results['blue'] > min_cube_per_game['blue']:
			min_cube_per_game['blue'] = cube_results['blue']
		if cube_results['green'] > min_cube_per_game['green']:
			min_cube_per_game['green'] = cube_results['green']
	return min_cube_per_game

# path = '/Users/akiko/Projects/adventofcode2023/adventofcode2023/day02/akiko/sample.csv'
path = '/Users/akiko/Projects/adventofcode2023/adventofcode2023/day02/akiko/input.csv'
raw_data = open(path, "r").read().splitlines()

temp = []
for to_split_each_game in raw_data:
	each_game_result = to_split_each_game.split(': ')
	temp.append(each_game_result)

temp2 = []
for temp_game_result in temp:
	for to_split_game_result in temp_game_result:
		game_result_split = to_split_game_result.split('; ')
	temp2.append(game_result_split)

temp3 = []
for temp2_game_result in temp2:
	# ['3 blue, 4 red', '1 red, 2 green, 6 blue', '2 green']
	foo = []
	for bar in temp2_game_result:
		# '3 blue, 4 red'
		bar_split = bar.split(', ')
		foo.append(bar_split)
	temp3.append(foo)

temp4 = []
for temp3_game_result in temp3:
	# [['3 blue', '4 red'], ['1 red', '2 green', '6 blue'], ['2 green']]
	foo3 = []
	for x in temp3_game_result:
		# ['3 blue', '4 red']
		foo2 = []
		for a in x:
			# '3 blue'
			a_split = a.split(' ')
			foo2.append(a_split)
		foo3.append(foo2)
	temp4.append(foo3)

games = []
for level1 in temp4:
	# [[['3', 'blue'], ['4', 'red']], [['1', 'red'], ['2', 'green'], ['6', 'blue']], [['2', 'green']]]
	temp5 = []
	for input_result in level1:
		# [['3', 'blue'], ['4', 'red']]
		# print(make_set_result_dict(input_result))
		temp5.append(make_set_result_dict(input_result))
	games.append(temp5)


# Part 1
# 12 red cubes, 13 green cubes, and 14 blue cubes
bag_content = {'red' : 12, 'green' : 13, 'blue' : 14}

invalid_game_ids = []
all_game_ids = []
for index, game in enumerate(games):
	game_id = index + 1
	all_game_ids.append(game_id)
	for outcome in game:
		if is_game_result_invalid(bag_content, outcome):
			invalid_game_ids.append(game_id)

print(invalid_game_ids)
set_invalid_game_ids = set(invalid_game_ids) # TODO: fix this to have a deduped list!
# currently cheating by using set ><

sum_valid_game_ids = sum(all_game_ids) - sum(set_invalid_game_ids)
print(sum_valid_game_ids)
# 2369

# Part 2
# fewest number of cubes of each color
power_per_game = []
for each_game in games:
	min_cubes = get_min_cubes_per_game(each_game)
	power_of_min_set_of_cubes_per_game = min_cubes['red'] * min_cubes['blue'] * min_cubes['green']
	power_per_game.append(power_of_min_set_of_cubes_per_game)

print(sum(power_per_game))
# 66363