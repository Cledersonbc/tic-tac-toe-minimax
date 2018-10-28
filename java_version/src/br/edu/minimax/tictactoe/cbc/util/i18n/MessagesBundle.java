package br.edu.minimax.tictactoe.cbc.util.i18n;

import java.util.Locale;
import java.util.ResourceBundle;

/**
 * MessageBundle for internacionalization (I18N)
 * This class provides a way to get messages accord to locale.
 * @author Cledersonbc
 *
 */

public class MessagesBundle {
	private Locale currentLocale;
	private String language;
	private String country;
	private ResourceBundle messages;

	public MessagesBundle(String language, String country) {
		this.language = language;
		this.country = country;
		loadResourceBundle();
	}

	public MessagesBundle() {
		this("en", "US");
	}

	private void loadResourceBundle() {
		currentLocale = new Locale(language, country);
		messages = ResourceBundle.getBundle("MessagesBundle", currentLocale);
	}

	public String getLanguage() {
		return language;
	}

	public void setLanguage(String language) {
		this.language = language;
		loadResourceBundle();
	}

	public String getCountry() {
		return country;
	}

	public void setCountry(String country) {
		this.country = country;
		loadResourceBundle();
	}

	public String getMessage(String key) {
		return messages.getString(key);
	}
}
