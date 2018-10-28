package br.edu.minimax.tictactoe.cbc.util.i18n;

public enum Country {
	US("us"), BR("br");
	
	private String name;
	Country(String name) {
		this.name = name;
	}
	
	public String getName() {
		return this.name;
	}
	
	public int getTotal() {
		return Country.values().length;
	}
}
