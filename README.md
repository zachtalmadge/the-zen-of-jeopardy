# The Zen of Jeopardy!

The Zen of Jeopardy! is a Command Line Interface (CLI) game that brings the excitement and challenge of the classic game show Jeopardy to your terminal. Get ready to test your knowledge across a variety of topics and buzz in with your answers!

## Description

This CLI game is designed to simulate the experience of the popular TV show Jeopardy. Players can choose their categories, answer questions, and keep score, all within the comfort of their terminal environment. Perfect for trivia enthusiasts and those looking to sharpen their knowledge while having fun!

## How to Install

Before installing, ensure you have Python installed on your system.

To install The Zen of Jeopardy!, open your terminal and follow these steps:

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/your-username/the-zen-of-jeopardy.git
   ```
2. Navigate to the cloned directory:
   ```
   cd the-zen-of-jeopardy
   ```
3. Install the necessary dependencies and enter Python shell:
   ```
   pipenv install && pipenv shell
   ```

## How to Use

After installation, you can run The Zen of Jeopardy! with the following command from the terminal:

```
python lib/cli.py
```

Upon starting the game, you will be presented with a menu:

0. Exit the program
1. Play a game
2. View scoreboard
3. View rules
4. Reset game

If you need to brush up on the rules, enter 3. 

If you are a new or returning player, enter 1. Your profile will be retrieved or a new one will be created for you, and the game will begin!

A board containing the categories and questions will appear on screen.

To select a question, type the category (e.g., `Javascript`), and then the desired point value (e.g. `200`) when prompted.

A timer will start as soon as your question is selected, so be ready!

To answer a question, simply type in your answer after the prompt (No need to add the `What is..` as we provided it).

Once a question is answered, its square on the board will be cleared and you will be unable to select it again.

Once all questions have been answered, check your final score!

Head over to the scoreboard to view the leaders with the highest scores!

Select option 4 from the menu to reset the game and play again.

## Contributors

A special thanks to the individuals who have contributed to making The Zen of Jeopardy! a fun and educational experience:

- Kat Tannehill
- Wesley Smith
- Zachary Talmadge

We appreciate the time and expertise each contributor has brought to this project. If you're interested in contributing too, please feel free to submit a pull request or reach out to one of our contributors.

Enjoy playing The Zen of Jeopardy! and may the best trivia mind win!
