import java.io.Console;
import java.util.Arrays;

public class Hangman {

  public static void main(String[] args) {
    Console console = System.console();

    console.printf("WELCOME TO HANGMAN\n");
    String word = console.readLine("List a word: ");
    String guessed_letters = "";
    String guessed_word = "";
    int guesses_left = 7;
    String guess;
    String[] letters = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
    "r", "s", "t", "u", "v", "w", "x", "y", "z"};

    for (char letter: word.toCharArray()) {
      guessed_word += " - ";
    }
    console.printf("\nGuessed word so far: %s\n", guessed_word);

    while (guesses_left > 0) {
      if (word.equals(guessed_word)) {
        console.printf("Nice job! You guessed the word with %s guesses remaining!\n", guesses_left);
        break;
      } else {
        guessed_word = "";
        console.printf("Guesses left: %s\n",guesses_left);
        guess = console.readLine("Guess a letter: ");
        while (guess.length() > 1 || Arrays.asList(letters).indexOf(guess) == -1) {
          guess = console.readLine("Guesses must be letter and must be one character long, guess again: ");
        }
        if (word.indexOf(guess) == -1) {
          console.printf("Sorry, \'%s' is not in the word. You lost a guess!\n\n", guess);
          guesses_left -=1;
        } else {
          console.printf("Good job! \'%s' is in the word.\n\n", guess);
        }
        guessed_letters += guess;
        for (char letter : word.toCharArray()) {
          if (guessed_letters.indexOf(letter) > -1) {
            guessed_word += letter;
          } else {
            guessed_word += " - ";
          }
        }
        console.printf("Guessed word so far: %s\n",guessed_word);
    }
  }
  if (guesses_left == 0) {
    console.printf("Sorry, you lost. The word was \'%s\'. Better luck next time!\n",word);
  }
}
}
