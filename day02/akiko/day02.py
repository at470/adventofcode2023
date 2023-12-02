#'12 red cubes, 13 green cubes, and 14 blue cubes'
bag_content = {'red' : 12,
			   'green' : 13,
			   'blue' : 14}

# wanted input
# NB.  index of games = game id - 1
games = [[{'red' : 4, 'green' : 0, 'blue' : 3}, 
		 {'red' : 1, 'green' : 2, 'blue' : 6}, 
		 {'red' : 0, 'green' : 2, 'blue' : 0}], 
		[{'red' : 0, 'green' : 2, 'blue' : 1}, 
		 {'red' : 1, 'green' : 3, 'blue' : 4}, 
		 {'red' : 0, 'green' : 1, 'blue' : 1}],
		[{'red' : 20, 'green' : 8, 'blue' : 6}, 
		 {'red' : 4, 'green' : 13, 'blue' : 5}, 
		 {'red' : 1, 'green' : 5, 'blue' : 0}],
		[{'red' : 3, 'green' : 1, 'blue' : 6}, 
		 {'red' : 6, 'green' : 3, 'blue' : 0}, 
		 {'red' : 14, 'green' : 3, 'blue' : 15}],
		[{'red' : 6, 'green' : 3, 'blue' : 1}, 
		 {'red' : 1, 'green' : 2, 'blue' : 2}] ]

# for game_index, all_game_results in enumerate(games):
# 	print('game id: ', game_index+1, all_game_results)

# TODO
# check that bag_content['red'] >= all_game_results[index]['red']
# if False: 
# 	game invalid
# else:
# 	bag_content['green'] >= all_game_results[index]['green']
# 	if False:
# 		game_invalid
# 	else:
# 		bag_content['blue'] >= all_game_results[index]['blue']
# 		if False: 
# 			game_invalid
# 		else:
# 			return game_index -> game_id = game_index+1


def is_game_result_valid(bag_content, game_result):
	# bag_content = {'red' : 12, 'green' : 13, 'blue' : 14}
	# game_result = {'red' : 4, 'green' : 0, 'blue' : 3}
	bag_result_comparison_var = [(bag_cube_colour, game_result[bag_cube_colour], bag_cube_num) for bag_cube_colour, bag_cube_num in bag_content.items()]
	# bag_result_comparison_var = [('red', 20, 12), ('green', 8, 13), ('blue', 6, 14)]
	for colour_comparison in bag_result_comparison_var:
		print(colour_comparison, colour_comparison[1] > colour_comparison[2])
		if colour_comparison[1] > colour_comparison[2]:
			result = True
			return result
		else:
			result = False
	return result





bag_content = {'red' : 12, 'green' : 13,'blue' : 14}
# game_result = {'red' : 4, 'green' : 0, 'blue' : 3}
game_result = {'red' : 20, 'green' : 8, 'blue' : 6}

print(is_game_result_valid(bag_content, game_result))