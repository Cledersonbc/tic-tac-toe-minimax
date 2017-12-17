from math import inf as infinity

board = [
		[ 0, 0, 0 ],
		[ 0, 0, 0 ],
		[ 0, 0, 0 ],
]
HUMAN = -1
COMP  = +1

# Heuristic evaluation function
def evaluate():
	score = 0
	score = score + eval_line(0, 0, 0, 1, 0, 2) # row 0
	score = score + eval_line(1, 0, 1, 1, 1, 2) # row 1
	score = score + eval_line(2, 0, 2, 1, 2, 2) # row 2
	score = score + eval_line(0, 0, 1, 0, 2, 0) # col 0
	score = score + eval_line(0, 1, 1, 1, 2, 1) # col 1
	score = score + eval_line(0, 2, 1, 2, 2, 2) # col 2
	score = score + eval_line(0, 0, 1, 1, 2, 2) # diag
	score = score + eval_line(0, 2, 1, 1, 2, 0) # inv. diag
	return score


def eval_line(r1, c1, r2, c2, r3, c3):
	score = 0

	# First cell
	# Suppose X is a computer and O is a human
	# X ? ?; score = +1
	# O ? ?; score = -1
	# ? ? ?; score = 0
	if COMP == board[r1][c1]:
		score = +1
	elif HUMAN == board[r1][c1]:
		score = -1

	# Second cell
	# X X ?; score = +10 instead of +1 (more chances to win)
	# O O ?; score = -10 instead of -1
	# above **otherwise**
	if COMP == board[r2][c2]:
		if score == 1:
			# X X ?; may win
			score = +10
		elif score == -1:
			# O X ?; no chances to win, draw
			return 0
		else:
			# ? X ?; cell1 is empty
			score = +1
	elif HUMAN == board[r2][c2]:
		if score == -1:
			# O O ?; may lose
			score = -10
		elif score == 1:
			# X O ?; draw
			return 0
		else:
			# ? O ?; cell1 is empty
			score = -1

	# Third cell
	# X X X; score = +100 (win)
	# O O O; score = -100 (lose)
	# above **otherwise**
	if COMP == board[r3][c3]:
		if score > 0:
			# X X X; new score = +100
			# ? X X; new score = +10
			score *= 10
		elif score < 0:
			# O O X
			# O ? X
			# draw
			return 0
		else:
			# ? ? X; cell1 and cell2 are empty
			score = +1
	elif HUMAN == board[r3][c3]:
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
	if (
	state[0][0] == player and state[0][1] == player and state[0][2] == player or
	state[1][0] == player and state[1][1] == player and state[1][2] == player or
	state[2][0] == player and state[2][1] == player and state[2][2] == player or
	state[0][0] == player and state[1][0] == player and state[2][0] == player or
	state[0][1] == player and state[1][1] == player and state[2][1] == player or
	state[0][2] == player and state[1][2] == player and state[2][2] == player or
	state[0][0] == player and state[1][1] == player and state[2][2] == player or
	state[2][0] == player and state[1][1] == player and state[0][2] == player ):
		return True
	else:
		return False


def minimax(state, depth, player):
	if depth == 0 or gameover(state, player):
		score = evaluate()
		return score

print('Final Score: ', gameover(board, 1))

