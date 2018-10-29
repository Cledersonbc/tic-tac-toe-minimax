package br.edu.tictactoe.cbc.view;

import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

import br.edu.tictactoe.cbc.util.i18n.Country;
import br.edu.tictactoe.cbc.util.i18n.Language;
import br.edu.tictactoe.cbc.util.i18n.MessagesBundle;

public class Window extends JFrame implements ActionListener {
	private static final long serialVersionUID = 1L;
	private MessagesBundle msgBundle;
	private JLabel systemMessage;
	private JButton play;
	private JButton aiStart;
	
	public Window() {
		msgBundle = new MessagesBundle(Language.EN, Country.US);
		JPanel mainPanel = new JPanel(new BorderLayout());
		JPanel headerPanel = buildHeaderPanel();
		JPanel bodyPanel = buildBodyPanel();
		JPanel footerPanel= buildFooterPanel();
		
		mainPanel.add(headerPanel, BorderLayout.NORTH);
		mainPanel.add(bodyPanel, BorderLayout.CENTER);
		mainPanel.add(footerPanel, BorderLayout.SOUTH);
		
		this.setContentPane(mainPanel);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setTitle(msgBundle.getMessage("title"));
		this.pack();
		this.setSize(430, 400);
		this.setLocationRelativeTo(null);
		this.setResizable(false);
		this.setVisible(true);
	}
	
	private JPanel buildHeaderPanel() {
		JPanel headerPanel = new JPanel(new GridLayout(1, 2, 2, 2));
		JComboBox<String> combobox = new JComboBox<>();
		systemMessage = new JLabel();
		
		combobox.addItem(msgBundle.getMessage("en_us"));
		combobox.addItem(msgBundle.getMessage("pt_br"));
		
		headerPanel.add(combobox);
		headerPanel.add(systemMessage);
		
		return headerPanel;
	}
	
	private JPanel buildBodyPanel() {
		JPanel bodyPanel = new JPanel(new GridLayout(3, 3, 10, 10));
		
		for (int i = 0; i < 9; ++i) {
			JButton button = new JButton();
			button.addActionListener(this);
			button.setActionCommand(String.valueOf(i));
			bodyPanel.add(button);
		}
		
		return bodyPanel;
	}
	
	private JPanel buildFooterPanel() {
		JPanel footerPanel= new JPanel(new GridLayout(1, 2, 2, 2));
		play = new JButton();
		aiStart = new JButton();
		
		play.setText(msgBundle.getMessage("play"));
		aiStart.setText(msgBundle.getMessage("ai_start"));
		
		play.addActionListener(this);
		aiStart.addActionListener(this);
		
		footerPanel.add(aiStart);
		footerPanel.add(play);
		
		return footerPanel;
	}

	

	public static void main(String[] args) {
		new Window();
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		System.out.println(e.getActionCommand().toString());
		
	}

}
