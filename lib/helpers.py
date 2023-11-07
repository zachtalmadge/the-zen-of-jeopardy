# lib/helpers.py
import time
import threading
from models.User import User
from models.Category import Category
from models.Question import Question
from rich.console import Console
from rich.console import Theme
from rich.table import Table
import ipdb

custom_theme = Theme({
    "heading": "bold bright_white",
    "table_head": "bold bright_white on blue1",
    "subhead": "bold gold3",
    "tile": "bold gold3 on blue1",
    "table": "on blue1"
})

console = Console(theme=custom_theme)
user_answer = None
answer_submitted = False
timer_completed = False

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

def make_table():
    table = Table(title="Play the Zen of Jeopardy!", border_style="black", show_lines=True, style="table")

    categories = [category.name for category in Category.get_all()]
    
    for category in categories:
        table.add_column(category, style="table_head")

    for num in range(1,6):
        row = [question.point_value for question in Question.get_questions_by_level(num)]
        table.add_row(f"${row[0]}", f"${row[1]}", f"${row[2]}", f"${row[3]}", f"${row[4]}", f"${row[5]}", style="tile")
        
    console.print(table)
    
def play_game(player):
    make_table()
    select_category(player)

def add_points(selected_question, player):
    player.score += selected_question.point_value
    player.update()
    
def end_game(player):
    pass

def check_answer(selected_question, answer, player):
    if selected_question.answer == answer:
        console.print("Great job!", style="subhead")
        add_points(selected_question, player)
    else:
        console.print(f"Sorry, the answer was {selected_question.answer}", style="subhead")
    selected_question.point_value = ""
    selected_question.save()
    play_game(player)

def select_category(player):

    console.print("Select a question: ", style="subhead")
    
    # re-assign selected_category from None to input 
    selected_category = input("Type a category name: ")
    
    # if input category is not one of our categories, re-run the function
    if selected_category.lower() not in ['javascript', 'react', 'python', 'sql', 'comp sci', 'git']:
        console.print('Invalid category selection!')
        return select_category(player)

    # if input points it not a valid point value, re-run the function
    selected_points = input("Type a question amount: $")
    points = int(selected_points)
    
    category = Category.find_by_name(selected_category)
    
    # if the user had already selected the points, restart the function
    if points not in [question.point_value for question in category.category_questions() if question.point_value]:
        console.print('Invalid question amount!')
        return select_category(player)
    
    select_question(category, points, player)

def countdown_timer():
    global timer_completed
    time_left = 10
    while time_left > 0 and not timer_completed:
        time_left -= 1
        time.sleep(1)
    timer_completed = True

def get_user_input():
    global user_answer, answer_submitted
    user_answer = input("What is... ")
    answer_submitted = True

def select_question(category, points, player):
      
    selected_question = next((question for question in category.category_questions() 
                              if question.point_value == points), None)
    
    if selected_question:
        global user_answer, timer_completed

        # Start the countdown timer in a separate thread
        timer_thread = threading.Thread(target=countdown_timer)
        timer_thread.start()

        # Initialize time_left
        console.print(f"You have 10 seconds to answer the question.", style="subhead")
        console.print(selected_question.question_text, style="subhead")

        # Start a thread to capture user input
        input_thread = threading.Thread(target=get_user_input)
        input_thread.start()

        # Wait for the timer thread to finish
        timer_thread.join()

        # Check if the timer completed or the user submitted an answer
        if timer_completed:
            console.print("\nTime's up!", style="subhead")
            # console.print(f"Sorry, the answer was {selected_question.answer}", style="subhead")
            user_answer = "" # Set the answer as empty
            check_answer(selected_question, user_answer, player)
            
        # Wait for the input thread to finish
        input_thread.join()

    else:
        console.print("No question found")
        select_category(player)

        select_category(player)