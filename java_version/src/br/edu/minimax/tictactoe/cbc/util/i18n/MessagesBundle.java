package br.edu.minimax.tictactoe.cbc.util.i18n;

import java.util.Locale;
import java.util.ResourceBundle;

/**
 * MessageBundle for internationalization (I18N)
 * This class provides a way to get messages accord to locale.
 * @author Cledersonbc
 *
 */

public class MessagesBundle {
	private Locale currentLocale;
	private String language;
	private String country;
	private ResourceBundle messages;

	public MessagesBundle(Enum<Language> language, Enum<Country> country) {
		this.language = language.name();
		this.country = country.name();
		loadResourceBundle();
	}

	public MessagesBundle() {
		this(Language.EN, Country.US);
	}

	private void loadResourceBundle() {
		currentLocale = new Locale(language, country);
		messages = ResourceBundle.getBundle("MessagesBundle", currentLocale);
	}

	public String getLanguage() {
		return language;
	}

	public void setLanguage(Enum<Language> language) {
		this.language = language.name();
		loadResourceBundle();
	}

	public String getCountry() {
		return country;
	}

	public void setCountry(Enum<Country> country) {
		this.country = country.name();
		loadResourceBundle();
	}

	public String getMessage(String key) {
		return messages.getString(key);
	}
}
