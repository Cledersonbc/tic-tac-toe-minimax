from math import inf as infinity

board = [
		[ 0, 0, 0 ],
		[ 0, 0, 0 ],
		[ 0, 0, 0 ],
]
HUMAN = -1
COMP  = +1

# Heuristic evaluation function
def evaluate(state):
	"""
	Function to heuristic evaluation of state.
	"""
	score = 0
	score = score + eval_line(0, 0, 0, 1, 0, 2, state) # row 0
	score = score + eval_line(1, 0, 1, 1, 1, 2, state) # row 1
	score = score + eval_line(2, 0, 2, 1, 2, 2, state) # row 2
	score = score + eval_line(0, 0, 1, 0, 2, 0, state) # col 0
	score = score + eval_line(0, 1, 1, 1, 2, 1, state) # col 1
	score = score + eval_line(0, 2, 1, 2, 2, 2, state) # col 2
	score = score + eval_line(0, 0, 1, 1, 2, 2, state) # diag
	score = score + eval_line(0, 2, 1, 1, 2, 0, state) # inv. diag
	return score


def eval_line(r1, c1, r2, c2, r3, c3, state):
	"""
	This function evaluates a line and it returns:
	* +1 or +10 or +100 for a computer player
	* -1 or -10 or -100 for a human player
	"""
	score = 0

	# First cell
	# Suppose X is a computer and O is a human
	# X ? ?; score = +1
	# O ? ?; score = -1
	# ? ? ?; score = 0
	if COMP == state[r1][c1]:
		score = +1
	elif HUMAN == state[r1][c1]:
		score = -1

	# Second cell
	# X X ?; score = +10 instead of +1 (more chances to win)
	# O O ?; score = -10 instead of -1
	# below **otherwise**
	if COMP == state[r2][c2]:
		if score == 1:
			score = +10 # X X ?; may win
		elif score == -1:
			return 0 # O X ?; no chances to win, draw
		else:
			score = +1 # ? X ?; cell1 is empty
	elif HUMAN == state[r2][c2]:
		if score == -1:
			score = -10 # O O ?; may lose
		elif score == 1:
			return 0 # X O ?; draw
		else:
			score = -1 # ? O ?; cell1 is empty

	# Third cell
	# X X X; score = +100 (win)
	# O O O; score = -100 (lose)
	# below **otherwise**
	if COMP == state[r3][c3]:
		if score > 0:
			# X X X; new score = +100
			# ? X X; new score = +10
			score *= 10
		elif score < 0:
			# O O X
			# O ? X
			return 0 # draw
		else:
			# ? ? X; cell1 and cell2 are empty
			score = +1
	elif HUMAN == state[r3][c3]:
		if score < 0:
			# O O O; new score = -100
			# ? O O; new score = -10
			score *= 10
		elif score > 1:
			# X X O; draw
			# X ? O; draw
			return 0
		else:
			# ? ? O; cell1 and cell2 are empty
			score = -1

	return score


def gameover(state, player):
	"""
	Gameover function returns True if the player wins in the Tic-Tac-Toe
	State is the board. To win, the player has 8 possibilities:
	* Three rows 	[X X X] or [O O O]
	* Three cols 	[X X X] or [O O O]
	* Two diagonals [X X X] or [O O O]
	"""
	winstate = [
		[state[0][0], state[0][1], state[0][2]],
		[state[1][0], state[1][1], state[1][2]],
		[state[2][0], state[2][1], state[2][2]],
		[state[0][0], state[1][0], state[2][0]],
		[state[0][1], state[1][1], state[2][1]],
		[state[0][2], state[1][2], state[2][2]],
		[state[0][0], state[1][1], state[2][2]],
		[state[2][0], state[1][1], state[0][2]],
	]
	if [player, player, player] in winstate:
		return True
	else:
		return False


def empty_cells(state):
	"""
	Each cell empty will be added into cells' list
	"""
	cells = []

	for x, row in enumerate(state):
		for y, cell in enumerate(row):
			if cell == 0:
				cells.append([x, y])
	return cells

def minimax(state, depth, player):
	if depth == 0 or gameover(state, player):
		score = evaluate(state)
		return [-1, -1, score]

	for cell in empty_cells(state):
	# ** --- *** In progress *** --- ** #

# DEBUG
def render(state):
	print('{:2} | {:2} | {:2}'.format(state[0][0], state[0][1], state[0][2]))
	print('{:2} | {:2} | {:2}'.format(state[1][0], state[1][1], state[1][2]))
	print('{:2} | {:2} | {:2}'.format(state[2][0], state[2][1], state[2][2]))

# DEBUG
# print('Minimax: ', minimax(board, 9, 1))
# print('Score: ', evaluate(board))
# print(empty_cells(board))
