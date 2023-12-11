# Movie Guesser 3000

## Overview

Welcome to Movie Guesser 3000, a simple and entertaining Python console game where players guess a movie name letter by letter. The game supports both single and multiplayer modes, allowing players to compete for the highest score. Players have the chance to guess up to five incorrect letters before losing the game.

## Instructions

1. ### Number of Players:
   - Enter the number of players who will participate in the game. You can have a solo adventure or challenge your friends.

2. ### Player Names:
   - If there is only one player, enter their name when prompted. For multiple players, provide names for each participant.

3. ### Language Selection:
   - Choose between English (E) and Hindi (H) for the movie language. Movie names will be randomly selected based on your choice.

4. ### Gameplay:
   - Players guess one letter at a time.
   - Avoid guessing special characters or numbers.
   - Players have a maximum of five incorrect guesses.
   - A correct guess reveals the letter's position in the movie name.
   - Two hints are available after the second and fourth incorrect guesses.

5. ### Scoring:
   - Players earn points based on the percentage of the movie name correctly guessed.
   - The game ends when a player guesses incorrectly five times, revealing the correct movie name.

6. ### Play Again:
   - After each player completes their turn, the option to play again is provided.
   - Enter "YES" to start a new round or any other input to exit the game.

## File Structure

- **EnglishMovies.csv:** Contains a list of English movies for the game.
- **MoviesHindi.csv:** Contains a list of Hindi movies for the game.
- **Moviesgame.py:** The main Python script containing the game logic.

## How to Run

1. Ensure you have Python installed on your machine.
2. Execute the `Moviesgame.py` script using a Python interpreter.

## Additional Notes

- The game randomly selects a movie from the provided CSV files for each round.
- Players receive hints to help them guess the movie name.
- The game tracks scores for each player and displays the results at the end of each round.

Enjoy playing Movie Guesser 3000!
