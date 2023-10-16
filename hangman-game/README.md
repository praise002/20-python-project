# Hangman Game

## Overview:

Hangman is a classic word-guessing game that is both entertaining and educational. It is typically played by two or more players, where one player thinks of a word, phrase, or a sentence, and the other player(s) attempt to guess it one letter at a time. The game is called **Hangman** because a drawing of a hanging man is often used as a visual aid to track incorrect guesses. The challenge for the players is to guess the word correctly before the drawing is completed.

## How to Play:

1. **Select a Word**: One player thinks of a word and keeps it secret from the other player(s). This word can be related to a specific category or theme, such as animals, fruits, or movies.

2. **Display Blank Spaces**: For each letter in the word, a blank space is displayed, representing each letter's position. For example, "_ _ _ _ _" for a five-letter word.

3. **Guessing Letters**: The player(s) take turns guessing letters. They can guess one letter at a time. If the guessed letter is in the word, it is revealed in its correct position(s). If not, a part of the "hangman" is drawn.

4. **Hangman Progress**: As incorrect guesses accumulate, the drawing of the hangman progresses. Commonly, a hangman has components like a head, body, arms, and legs. The game typically ends when the hangman is fully drawn or when the word is guessed correctly.

5. **Win or Lose**: The game can end in two ways:

- **Win**: If the players successfully guess the word before the hangman is fully drawn, they win.
- **Lose**: If the hangman is fully drawn before they guess the word, they lose.

## Educational Benefits:

Hangman offers several educational benefits:

1. **Vocabulary Building**: Players learn new words and expand their vocabulary as they guess and reveal letters.

2. **Spelling Practice**: The game encourages players to practice their spelling skills.

3. **Strategic Thinking**: Players develop strategies for guessing letters efficiently and increasing their chances of success.

4. **Word Recognition**: The game enhances word recognition skills as players work to decipher the word based on revealed letters.

5. **Fun Learning**: Hangman is an enjoyable way to learn and reinforce language skills.

## Variations:

Hangman can be adapted in various ways to suit different preferences and educational goals. Some variations include:

- **Topic-Based**: Choose words related to a specific topic, such as science, history, or geography.
- **Multiplayer**: Allow multiple players to guess the word collectively.
- **Online Games**: Play Hangman online with friends or against computer opponents.
- **Time Challenges**: Set a time limit for guessing each letter or the entire word.
- **Picture-Based**: Use pictures or symbols instead of a traditional hangman drawing.

## Usage
1. **Run the Script**: Execute the script by running the following command:
```python main.py```

2. **Start Guessing**: The game will randomly select a word, display underscores for hidden letters, and provide you with the number of remaining attempts (lives).

3. **Guess a Letter**: Input a letter to guess. If the letter is in the word, it will be revealed; otherwise, you will lose a life.
```sh
Word: _ _ _ _ _
Lives: 6
Guess a letter: E
```

4. **Continue Guessing**: Keep guessing letters until you either successfully guess the word or run out of lives.

5. **Win or Lose**: If you guess the word, you win! If you run out of lives, the hangman is complete, and you lose.