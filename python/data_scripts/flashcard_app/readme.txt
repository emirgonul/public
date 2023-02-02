#flashcard study app
1.Read the data from the french_words.csv file in the data folder.
2.Pick a random French word/translation and put the word into the flashcard.
3.Every time user press the ❌ or ✅ buttons, it generates a new random word to display.
4.After a delay of 3s (3000ms), the card flips and display the English translation for the current word.
5.The card image change to the card_back.png and the text colour change to white. 
6.When the user presses on the ✅ button, it means that they know the current word on the flashcard and that word is removed from the list of words that might come up.
7.The updated data is saved to a new file called words_to_learn.csv
8.The next time the program is run, it checks if there is a words_to_learn.csv file. If it exists, the program uses those words to put on the flashcards. 
9. If the words_to_learn.csv does not exist (i.e., the first time the program is run), then it uses the words in the french_words.csv