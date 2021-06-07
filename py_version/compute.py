# File Name: compute.py
# Description: Provides game algorithm for Cross & Nut game
#
# Written by Rutuparn Pawar (InputBlackBoxOutput)
# Created on 5 Sept 2019
# Last modified on 2 Nov 2020

import random, time, minimax

class Tic_Tac_Toe:

	def __init__(self):
		# self.grid_map = [['O', 'X', 'X'], ['O', 'X', 'O'], ['O', 'O', 'O']]  # Use for testing purpose
		self.grid_map = [['  ', '  ', '  '], ['  ', '  ', '  '], ['  ', '  ', '  ']]
		self.cross_nut_map = {'cross': 'X', 'empty': '  ', 'nut': 'O'}
		self.winner_string = None

	"""Function to place cross/nut in grid if place is empty"""

	def place_cross_nut(self, x, y, place):
		if place == 'cross':
			if self.grid_map[x][y] == '  ':
				self.grid_map[x][y] = self.cross_nut_map[place]
				# Cross placed at ({x},{y})
				return True
			else:
				# Cross cannot be placed at ({x},{y}) since place is not empty
				return False
		elif place == 'nut':
			if self.grid_map[x][y] == '  ':
				self.grid_map[x][y] = self.cross_nut_map[place]
				# Nut placed at ({x},{y})
				return True
			else:
				# Nut cannot be placed at ({x},{y}) since place is not empty
				return False
		else:
			self.grid_map[x][y] = self.cross_nut_map['empty']

	"""Function to check if the player/computer has won"""

	def winner_check(self, player):

		# Check for 3 cross/nut in a row
		for x in range(0, 3):
			win_count = 0
			for y in range(0, 3):
				if self.cross_nut_map[player] == self.grid_map[x][y]:
					win_count = win_count + 1
			if win_count == 3:
				# print('Complete Row', end='\n\n')
				return 'Winner is ' + player

		# Check for 3 cross/nut in a column
		for y in range(0, 3):
			win_count = 0
			for x in range(0, 3):
				if self.cross_nut_map[player] == self.grid_map[x][y]:
					win_count = win_count + 1
			if win_count == 3:
				# print('Complete column', end='\n\n')
				return 'Winner is ' + player

		# Check for 3 cross/nut across diagonals
		win_count = 0
		for i in range(0, 3):
			if self.cross_nut_map[player] == self.grid_map[i][i]:
				win_count = win_count + 1
		if win_count == 3:
			# print('Complete Diagonal \\', end='\n\n')
			return 'Winner is ' + player

		win_count = 0
		
		if self.cross_nut_map[player] == self.grid_map[0][2]:
			win_count = win_count + 1
		if self.cross_nut_map[player] == self.grid_map[1][1]:
			win_count = win_count + 1
		if self.cross_nut_map[player] == self.grid_map[2][0]:
			win_count = win_count + 1

		if win_count == 3:
			# print('Complete Diagonal /', end='\n\n')
			return 'Winner is ' + player

		return None

	'''Function to check if  '''

	def game_tied(self):
		if self.winner_string is None: 
			for row in range(0, 3):
				if self.cross_nut_map['empty'] in self.grid_map[row]:
					return False
		return True

	'''Function to clear grid_map'''

	def clear_cross_nut(self):
		for each_r in range(0, 3):
			for each_c in range(0, 3):
				self.grid_map[each_r][each_c] = self.cross_nut_map['empty']

	""" Function to display grid on console for testing """

	def display_for_testing(self):
		index = [0, 1, 2]
		for x in index:
			for y in index:
				print(self.grid_map[x][y], end=' ')
		print()

	""" Function to run gameloop in console for testing """

	def gameloop_for_testing(self):
		# print("Tic Tac Toe")
		# print('@Attention - !!!!! GRID MAY BEEN PREDEFINED !!!!!')

		while self.winner_string is None:

			self.display_for_testing()
			# print("Player X")
			x = input("Enter x coordinate :")
			y = input("Enter y coordinate :")
			self.place_cross_nut(int(x), int(y), 'cross')
			self.winner_string = self.winner_check('cross')

			if self.winner_string is not None:
				break

			self.display_for_testing()

			# print("Player O")
			x = input("Enter x coordinate :")
			y = input("Enter y coordinate :")
			self.place_cross_nut(int(x), int(y), 'nut')
			self.winner_string = self.winner_check('nut')

		self.display_for_testing()
		# print(self.winner_string)

		return

	# Player is always cross hence begins the game

	""""Function to generate random unoccupied position"""
	def random_position(self):
		position = [-1, -1]
		found_position = True

		retries = 0
		while found_position:
			x = random.randint(0, 2)
			y = random.randint(0, 2)
			if self.grid_map[x][y] == self.cross_nut_map['empty']:
				position[0] = x
				position[1] = y
				found_position = False

			retries = retries + 1
			if retries == 25:
				print("Error: random_position tries exceeded")
				break

		return position

	"""Function to get vacant grid positions"""
	def get_vacant_pos(self):
		vacant = []
		for r in range(0,3):
			for c in range(0,3):
				if self.grid_map[r][c] == self.cross_nut_map['empty']:
					vacant.append((r, c))
		return vacant

	"""Function to get computer's move in a game vs computer"""
	# Uses hand-crafted rules for AI
	def bot_move(self):
		if not self.game_tied() and self.winner_string is None:
			# Wait for some time
			time.sleep(0.1)
			random.seed(random.randint(20, 120))
			# 75% chance of best move
			chance = random.randint(0, 3)

			if chance > 0 :
				best_move = False
				# Check if winning move possible
				for each in self.get_vacant_pos():
					self.grid_map[each[0]][each[1]] = self.cross_nut_map['nut']

					if self.winner_check('nut') is None:
						self.grid_map[each[0]][each[1]] = self.cross_nut_map['empty']
					else:
						best_move = True
						break

				if best_move:
					return

				# Check if blocking move possible
				for each in self.get_vacant_pos():
					self.grid_map[each[0]][each[1]] = self.cross_nut_map['cross']

					if self.winner_check('cross') is None:
						self.grid_map[each[0]][each[1]] = self.cross_nut_map['empty']
					else:
						self.grid_map[each[0]][each[1]] = self.cross_nut_map['nut']
						best_move = True
						break
				if best_move:
					return
				else:
					position = self.random_position()
					self.place_cross_nut(position[0], position[1], 'nut')

			# Play random move
			if chance == 0:
				position = self.random_position()
				self.place_cross_nut(position[0], position[1], 'nut')

	def bot_move_minimax(self):
		for i in range(3): 
			for j in range(3):
				if self.grid_map[i][j] == self.cross_nut_map['cross']:
					minimax.board[i][j] = -1

				elif self.grid_map[i][j] == self.cross_nut_map['nut']:
					minimax.board[i][j] = 1

				else:
					minimax.board[i][j] = 0


		depth = len(minimax.empty_cells(minimax.board))
		if depth == 0 or minimax.game_over(minimax.board):
		    return

		if depth == 9:
		    x = minimax.choice([0, 1, 2])
		    y = minimax.choice([0, 1, 2])
		else:
		    move = minimax.minimax(minimax.board, depth, minimax.COMP)
		    x, y = move[0], move[1]

		self.place_cross_nut(x, y, 'nut')


# For testing game vs person
# game=Tic_Tac_Toe()
# game.gameloop_for_testing()

# For testing game vs computer
# game.display_for_testing()
# game.bot_move()
# game.display_for_testing()