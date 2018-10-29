package br.edu.tictactoe.cbc.model;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Table implements Cloneable {
	public static final int HUMAN    = -1;
	public static final int COMPUTER = +1;
	public int BOARD[][] = {
			{+1, -1, +1},
			{+1, 0, 0},
			{0, 0, 0}
	};
	
	public int evaluate(int state[][]) {
		int score;
		
		if (isWin(state, COMPUTER)) {
			score = +1;
		} else if (isWin(state, HUMAN)) {
			score = -1;
		} else {
			score =  0;
		}
		
		return score;
	}
	
	public boolean isWin(int state[][], int player) {
		int winState[][] = {
				{state[0][0], state[0][1], state[0][2]},
		        {state[1][0], state[1][1], state[1][2]},
		        {state[2][0], state[2][1], state[2][2]},
		        {state[0][0], state[1][0], state[2][0]},
		        {state[0][1], state[1][1], state[2][1]},
		        {state[0][2], state[1][2], state[2][2]},
		        {state[0][0], state[1][1], state[2][2]},
		        {state[2][0], state[1][1], state[0][2]}
		};
		int winPlayer[] = {player, player, player};
		
		if (isEqualPlayer(winState, winPlayer)) {
			return true;
		} else {
			return false;
		}
	}
	
	private boolean isEqualPlayer(int[][] state, int winPlayer[]) {
		for (int row[] : state) {
			if (row[0] == winPlayer[0] &&
				row[1] == winPlayer[1] &&
				row[2] == winPlayer[2]) {
				
				return true;
			}
		}
		return false;
	}
	
	public boolean gameOver(int state[][]) {
		return isWin(state, HUMAN) || isWin(state, COMPUTER);
	}
	
	public List<int[]> getEmptyCells(int state[][]) {
		List<int[]> emptyCells = new ArrayList<>();
		
		for (int row = 0; row < state[0].length; row++) {
			for (int col = 0; col < state.length; col++) {
				int cell = state[row][col];
				
				if (cell == 0) {
					int emptyCell[] = {row, col};
					emptyCells.add(emptyCell);
				}
			}
		}
			
		return emptyCells;
	}
	
	public boolean move(int x, int y, int player) {
		int playerMove[] = {x, y};
		
		if (getEmptyCells(BOARD).containsAll(Arrays.asList(playerMove))) { // bad idea
			//TODO find a best way to check empty cells
			BOARD[x][y] = player;
			return true;
		} else {
			return false;
		}
	}
	
	@Override
	public Object clone() {
		
		try {
			Table table = (Table) super.clone();
			table.BOARD = this.BOARD.clone();
			return table;
		} catch (CloneNotSupportedException e) {
			e.printStackTrace();
			return (Table) this;
		}
	}
}
