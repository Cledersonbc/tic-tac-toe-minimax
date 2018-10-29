package br.edu.tictactoe.cbc.util.i18n;

public enum Language {
	EN("en"), PT("pt");
	
	private String name;
	Language(String name) {
		this.name = name;
	}
	
	public String getName() {
		return this.name.toLowerCase();
	}
	
	public int getTotal() {
		return Language.values().length;
	}
}
