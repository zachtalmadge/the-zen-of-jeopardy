# lib/helpers.py
from models.User import User
from models.Category import Category
from models.Question import Question
from rich.console import Console
from rich.console import Theme
from rich.table import Table
import ipdb

custom_theme = Theme({
    "heading": "bold bright_white",
    "subhead": "bold gold3",
    "tile": "bold gold3 on blue1"
})

console = Console(theme=custom_theme)

def welcome():
    console.print("""
         _____ _          _____                ___ 
        |_   _| |_ ___   |__   |___ ___    ___|  _|
          | | |   | -_|  |   __| -_|   |  | . |  _|
          |_| |_|_|___|  |_____|___|_|_|  |___|_|  
              _ ______ ____  _____        _____  ______ _    _  _
             | |  ____/ __ \|  __ \ /\   |  __ \|  __  | |  | || |
             | | |__ | |  | | |__) /  \  | |__) | |  | | |__| || |
         _   | |  __|| |  | |  ___/ /\ \ |  _  /| |  | |\___  ||_|
        | |__| | |___| |__| | |  / ____ \| | \ \| |__| |  __| | _
         \____/|______\____/|_| /_/    \_\_|  \_\_____/  |___/ |_|
    """, style="heading")

def menu():
    console.print("Please select an option:", style="subhead")
    print("0. Exit the program")
    print("1. Play a game")
    print("2. View scoreboard")
    print("3. View rules")

def exit_program():
    console.print("Goodbye!", style="subhead")
    exit()

def find_or_create_player():
    name = input("Enter your name: ").strip()
    player = User.find_by_name(name)

    if player is None:
        new_player = User.create(name)
        console.print(f"Welcome, {new_player.name}!", style="subhead")
        play_game(new_player)
    else:
        console.print(f"Welcome back, {player.name}!", style="subhead")
        play_game(player)

table = Table(title="Play the Zen of Jeopardy!")
categories = [category.name for category in Category.get_all()]
for category in categories:
    table.add_column(category, style="heading")

table.add_row("$200", "$200", "$200", "$200", "$200", "$200", style="tile")
table.add_row("$400", "$400", "$400", "$400", "$400", "$400", style="tile")
table.add_row("$600", "$600", "$600", "$600", "$600", "$600", style="tile")
table.add_row("$800", "$800", "$800", "$800", "$800", "$800", style="tile")
table.add_row("$1000", "$1000", "$1000", "$1000", "$1000", "$1000", style="tile")

def play_game(player):
    console.print(table)
    select_category(player)

def check_answer(selected_question, answer):
    print(answer)
    if selected_question.answer == answer:
        print("Great job!")
        add_points()
        

def select_category(player):
    console.print("Select a question: ", style="subhead")
    selected_category = input("Type a category name: ")
    selected_question = input("Type a question amount: $")
    points = int(selected_question)
    select_question(selected_category, points, player)

def select_question(category_name, points, player):
    category = Category.find_by_name(category_name)
    selected_question = next((question for question in category.category_questions() if question.point_value == points), None)
    if selected_question:
        console.print(selected_question.question_text, style="subhead")
        answer = input("What is... ")
        check_answer(selected_question, answer)
    else:
        print("No question found")
        select_question(category_name, points, player)

