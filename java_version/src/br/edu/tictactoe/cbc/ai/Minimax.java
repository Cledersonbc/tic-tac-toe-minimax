package br.edu.tictactoe.cbc.ai;

import br.edu.tictactoe.cbc.model.Table;

public class Minimax implements AI {
	
	private Table table;
	
	public Minimax() {
		table = new Table();
	}

	@Override
	public void start() {
//		int[] r;
//		r = callAI(
//				table,
//				table.getEmptyCells(table.BOARD).size(),
//				Table.COMPUTER
//		);

	}
	
	private int[] callAI(Table state, int depth, int player) {
		int[] best;
		state = (Table) state.clone();
		
		if (player == Table.COMPUTER) {
			best = new int[] {-1, -1, Integer.MIN_VALUE};
		} else {
			best = new int[] {-1, -1, Integer.MAX_VALUE};
		}
		
		if (depth == 0 || state.gameOver(state.BOARD)) {
			int score = state.evaluate(state.BOARD);
			int values[] = {-1, -1, score};
			
			return values;
		}
		
		for (int[] cell : state.getEmptyCells(state.BOARD)) {
			int x = cell[0];
			int y = cell[1];
			int[] score;
			
			state.BOARD[x][y] = player;
			score = callAI(state, depth - 1, -player);
			state.BOARD[x][y] = 0;
			score[0] = x;
			score[1] = y;
			
			if (player == Table.COMPUTER) {
				if (score[2] > best[2]) {
					best = score;
				}
			}  else {
				if (score[2] < best[2]) {
					best = score;
				}
			}
		}
		
		return best;
	}

}
