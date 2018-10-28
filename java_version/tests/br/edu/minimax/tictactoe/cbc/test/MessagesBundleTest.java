package br.edu.minimax.tictactoe.cbc.test;

import br.edu.minimax.tictactoe.cbc.util.i18n.Country;
import br.edu.minimax.tictactoe.cbc.util.i18n.Language;
import br.edu.minimax.tictactoe.cbc.util.i18n.MessagesBundle;

public class MessagesBundleTest {

	public static void main(String[] args) {
		MessagesBundle msgBundle = new MessagesBundle();
		
		System.out.println("Language: " + msgBundle.getLanguage());
		System.out.println("Country: " + msgBundle.getCountry());
		System.out.println("EN Title: " + msgBundle.getMessage("title"));
		
		System.out.print("\n");
		msgBundle.setLanguage(Language.PT);
		msgBundle.setCountry(Country.BR);
		
		System.out.println("Language: " + msgBundle.getLanguage());
		System.out.println("Country: " + msgBundle.getCountry());
		System.out.println("PT-BR Title: " + msgBundle.getMessage("title"));

	}

}
