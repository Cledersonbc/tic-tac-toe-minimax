// An implementation of Minimax AI Algorithm in Tic Tac Toe Game using C++

#include<bits/stdc++.h>
#include <unistd.h>
using namespace std;

const int inf = 1e9;

/*
	HUMAN is human
	COMP is computer

*/

int HUMAN = -1;
int COMP = 1;
int board[][3] = { { 0, 0, 0} ,
	{0, 0, 0} ,
	{0, 0, 0}
};


//function declaration

int evaluate (int state[][3]);
bool wins(int state[][3] , int player);
bool game_over(int state[][3]);
vector<pair<int , int>>  empty_cells(int state[][3]);
bool valid_move(int x , int y);
bool set_move(int x , int y , int player);
vector<int> minimax(int state[][3] , int depth , int player);
void clean();
void render(int state[][3] , char COMP_choice , char HUMAN_choice );
void COMP_turn(char COMP_choice , char HUMAN_choice );
void HUMAN_turn(char COMP_choice , char HUMAN_choice );




int evaluate (int state[][3]) {

	/*
		Function to heuristic evaluation of state.
	    :param state: the state of the current board
	    :return: +1 if the computer wins; -1 if the human wins; 0 draw
	*/
	if (wins(state , COMP)) {
		return 1;
	} else if (wins(state , HUMAN)) {
		return -1;
	} else {
		return 0;
	}
}



bool wins(int state[][3] , int player) {

	/*
		This function tests if a specific player wins. Possibilities:
	    * Three rows    [X X X] or [O O O]
	    * Three cols    [X X X] or [O O O]
	    * Two diagonals [X X X] or [O O O]
	    :param state: the state of the current board
	    :param player: a human or a computer
	    :return: True if the player wins

	*/


	int win_state[8][3] = {{state[0][0], state[0][1], state[0][2]},
		{state[1][0], state[1][1], state[1][2]},
		{state[2][0], state[2][1], state[2][2]},
		{state[0][0], state[1][0], state[2][0]},
		{state[0][1], state[1][1], state[2][1]},
		{state[0][2], state[1][2], state[2][2]},
		{state[0][0], state[1][1], state[2][2]},
		{state[2][0], state[1][1], state[0][2]}
	};

	int win_move[3] = {player, player, player};
	for (int i = 0; i < 8; ++i) {
		bool flag = true;
		for (int j = 0; j < 3; j++) {
			if (win_move[j] != win_state[i][j]) {
				flag = false;
				break;
			}
		}

		if (flag) {
			return true;
		}
	}
	return false;

}

bool game_over(int state[][3]) {
	/*
		This function test if the human or computer wins
	    :param state: the state of the current board
	    :return: True if the human or computer wins
	*/
	return (wins(state , COMP) || wins(state , HUMAN) );
}


vector<pair<int , int>>  empty_cells(int state[][3]) {

	/*
		Each empty cell will be added into cells vector as pair(x , y)
	    :param state: the state of the current board
	    :return: a vector of pair of (x , y) co-ordinate of empty cells
	*/


	vector<pair<int , int> > cells;

	for (int x = 0 ; x < 3 ; x++) {
		for (int y = 0 ; y < 3 ; y++) {
			if (state[x][y] == 0) {
				cells.push_back({x , y});
			}
		}
	}

	return cells;
}

bool valid_move(int x , int y) {
	/*
		 A move is valid if the chosen cell is empty
	    :param x: X coordinate
	    :param y: Y coordinate
	    :return: True if the board[x][y] is empty
	*/

	if (board[x][y] == 0) {
		return true;
	}

	return false;
}

bool set_move(int x , int y , int player) {
	/*
		Set the move on board, if the coordinates are valid
		:param x: X coordinate
		:param y: Y coordinate
		:param player: the current player
	*/

	if (valid_move(x , y)) {
		board[x][y] = player;
		return true;
	} else return false;
}

vector<int> minimax(int state[][3] , int depth , int player) {
	/*
		AI function that choice the best move
	    :param state: current state of the board
	    :param depth: node index in the tree (0 <= depth <= 9),
	    but never nine in this case (see iaturn() function)
	    :param player: an human or a computer
	    :return: a list with [the best row, best col, best score]
	*/


	std::vector<int> best(3 , -1);

	if (player == COMP) {
		best[2] = -1 * inf;
	} else {
		best[2] =  inf;
	}


	if (depth == 0 || game_over(state)) {
		best[2] = evaluate(state);
		return best;
	}

	std::vector<pair<int , int>> cells = empty_cells(state);

	for (int i = 0 ; i < (int)cells.size() ; i++) {
		int x = cells[i].first;
		int y = cells[i].second;

		state[x][y] = player;



		if (wins(state , COMP)) {
			state[x][y] = 0;
			best[0] = x;
			best[1] = y;
			best[2] = inf;
			return best;

		}



		vector<int> score = minimax(state , depth - 1 , -1 * player);

		state[x][y] = 0;
		score[0] = x; score[1] = y;

		if (player == COMP) {
			if (score[2] > best[2]) {
				for (int j = 0 ; j < 3; j++) {
					best[j] = score[j];
				}
			}

		} else {
			if (score[2] < best[2]) {
				for (int j = 0 ; j < 3; j++) {
					best[j] = score[j];
				}

			}
		}

	}

	return best;

}


void clean() {
	/*
		clears the terminal/console
	*/

	system("clear");
}

void render(int state[][3] , char COMP_choice , char HUMAN_choice ) {

	/*
		Print the board on console
		:param state: currebt state of board
	*/

	map<int , char> chars;
	chars.insert({ -1 , HUMAN_choice});
	chars.insert({1 , COMP_choice});
	chars.insert({0 , ' '});


	string str_line = "---------------";

	cout << "\n" << str_line << "\n";

	for (int i = 0 ; i < 3; i++) {
		for (int j = 0; j < 3 ; j++) {
			cout << "| " << chars[state[i][j]] << " |";
		}
		cout << "\n" << str_line << "\n";
	}

	cout << "\n";


}

void COMP_turn(char COMP_choice , char HUMAN_choice ) {
	/*
		It calls the minimax function if the depth < 9,
		else it choices a random coordinate.
		: param c_choice: computer's choice X or O
		:param h_choice: human's choice X or O
		: return:
	*/

	int depth = 0;
	for (int i = 0 ; i < 3; i++) {
		for (int j = 0 ; j < 3; j++) {
			if (board[i][j] == 0) {
				depth++;
			}
		}
	}

	if (depth == 0 || game_over(board)) {
		return;
	}

	clean();
	cout << "COMP turn [" << COMP_choice << "]\n";
	render(board , COMP_choice , HUMAN_choice );

	int x , y;
	if (depth == 9) {
		// we can choose any
		srand(time(0));
		x = rand();
		x = x % 3;
		y = rand();
		y = y % 3;

	} else {
		std::vector<int> move = minimax(board , depth , COMP );
		x = move[0];
		y = move[1];

	}

	set_move(x , y , COMP);
	// time.sleep(1);
	sleep(1);


}

void HUMAN_turn(char COMP_choice , char HUMAN_choice ) {

	/*
		The Human plays choosing a valid move.
	    :param c_choice: computer's choice X or O
	    :param h_choice: human's choice X or O
	    :return:
	    """
	*/

	int depth = 0;
	for (int i = 0 ; i < 3; i++) {
		for (int j = 0 ; j < 3; j++) {
			if (board[i][j] == 0) {
				depth++;
			}
		}
	}

	if (depth == 0 || game_over(board)) {
		return;
	}

	clean();
	cout << "HUMAN turn [" << HUMAN_choice << "]\n";
	render(board , COMP_choice , HUMAN_choice);



	int move = -1;

	while (move < 1 || move > 9) {
		cout << "Use numpad (1..9)\n";
		cin >> move;

		bool flag = true;

		int x = 0 , y = 0;

		//to calculatr x and y coordinate
		for (x = 0; x < 3; x++) {

			for (y = 0 ; y < 3; y++) {
				if (3 * x + y + 1 == move ) {

					flag = false;
					break;

				}

			}
			if (!flag)break;
		}

		bool can_move = set_move(x , y , HUMAN);

		if (!can_move) {
			cout << "Bad move\n";
			move = -1;
		}

	}


}


int main() {

	/*
		Main function that calls all functions

	*/

	clean();
	char COMP_choice = '_';
	char HUMAN_choice = '_';


	while (HUMAN_choice != 'O' && HUMAN_choice != 'X' ) {
		cout << "\nChoose X or O\nChosen:";
		cin >> HUMAN_choice;
		if (HUMAN_choice == 'o')HUMAN_choice = 'O';
		if (HUMAN_choice == 'x')HUMAN_choice = 'X';
	}

	// Setting computer's choice

	if (HUMAN_choice == 'X') {
		COMP_choice = 'O';
	} else {
		COMP_choice = 'X';
	}

	clean();

	// Human may start first
	char first = '_';
	while (first != 'Y' && first != 'N') {
		cout << "First to start?[Y/N]: ";
		cin >> first;
		if (first == 'y')first = 'Y';
		if (first == 'n')first = 'N';
	}


	// Main loop of this game
	while ((int)((empty_cells(board)).size()) > 0 and !(game_over(board)) ) {

		if (first == 'N') {
			COMP_turn(COMP_choice , HUMAN_choice);
			first = '_';
		}


		HUMAN_turn(COMP_choice , HUMAN_choice);
		COMP_turn(COMP_choice , HUMAN_choice);
	}

	// game over message
	if (wins(board , HUMAN)) {
		clean();
		cout << "HUMAN turn [" << HUMAN_choice << "]\n";
		render(board , COMP_choice , HUMAN_choice );
		printf("HUMAN WIN!\n");

	} else if (wins(board , COMP)) {
		clean();
		cout << "COMP turn [" << COMP_choice << "]\n";
		render(board , COMP_choice , HUMAN_choice );
		cout << "COMP WIN!\n";
	} else {
		clean();
		render(board , COMP_choice , HUMAN_choice );
		cout << "DRAW!\n";
	}



	return 0;
}