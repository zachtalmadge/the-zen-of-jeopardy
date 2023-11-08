# lib/helpers.py
from models.User import User
from models.Category import Category
from models.Question import Question
from rich.console import Console
from rich.console import Theme
from rich.table import Table
import random
from threading import Timer
import ipdb

custom_theme = Theme({
    "heading": "bold bright_white",
    "table_head": "bold bright_white on blue1",
    "subhead": "bold gold3",
    "tile": "bold gold3 on blue1",
    "table": "on blue1"
})

console = Console(theme=custom_theme)
timer_expired_flag = False

EXIT_WORDS = ["0", "exit", "quit"]

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
    print("4. Reset game")
    print("5. Delete User")

def exit_program():
    console.print("Goodbye!", style="subhead")
    exit()
    
def view_rules():
        console.print("Welcome to Jeopardy!", style="subhead")
        console.print("Here are the rules:", style="subhead")
        print("1. There are categories with questions of varying point values.")
        print("2. Select a category and point value.")
        print("3. Answer the question correctly to earn points.")
        print("4. Incorrect answers result in point deduction.")
        print("5. The player will earn a score at the end of the game.")
        print("6. High scores will be added to the leaderboard.")

def find_or_create_player():
    name = input("Enter your name: ").strip()

    if name.lower() in EXIT_WORDS:
        exit_program()

    player = User.find_by_name(name)

    if player is None:
        new_player = User.create(name)
        console.print(f"Welcome, {new_player.name}!", style="subhead")
        play_game(new_player)
    else:
        console.print(f"Welcome back, {player.name}!", style="subhead")
        play_game(player)

def view_scoreboard():
    table = Table(title="Jeopardy Leaders!", border_style="black", show_lines=True, style="table")
    table.add_column("Player", style="table_head")
    table.add_column("Score", style="table_head")

    winners = [player for player in User.get_top_three()]
    for player in winners:
        table.add_row(player.name, str(player.score), style="tile")

    console.print(table)
    
def delete_user():
    name = input("Enter your name: ").strip()

    if name.lower() in EXIT_WORDS:
        exit_program()
    
    player = User.find_by_name(name)
    if player:
        player.delete()
    else:
        console.print(f"Could not find {name}.", style="subhead")

def make_table():
    table = Table(title="Play the Zen of Jeopardy!", border_style="black", show_lines=True, style="table")

    categories = [category.name for category in Category.get_all()]
    
    for category in categories:
        table.add_column(category.title(), style="table_head")

    for num in range(1,6):
        row = [question.point_value for question in Question.get_questions_by_level(num)]
        table.add_row(f"${row[0]}", f"${row[1]}", f"${row[2]}", f"${row[3]}", f"${row[4]}", f"${row[5]}", style="tile")
        
    console.print(table)
    
def play_game(player):
    make_table()
    select_category(player)

def add_points(selected_question, player, doubleJeopardy):
    if doubleJeopardy:
        player.score += selected_question.point_value * 2
    else:
        player.score += selected_question.point_value
    
    player.update()
    
def subtract_points(selected_question, player, doubleJeopardy):
    if doubleJeopardy:
        player.score -= selected_question.point_value * 2
    else:
        player.score -= selected_question.point_value
        
    player.update()
    
def end_game(player):
    console.print(f"Congratulations! Your final score is {player.score}!")
    menu()

def check_answer(selected_question, answer, player, doubleJeopardy):
    global timer_expired_flag
    timer_expired_flag = False

    if selected_question.answer == answer:
        add_points(selected_question, player, doubleJeopardy)
        
        console.print(f"Great job! You won {selected_question.point_value} points!", style="subhead")
        console.print(f"Your current score is {player.score}.")
        
    else:
        subtract_points(selected_question, player, doubleJeopardy)
        
        console.print(f"Sorry, the answer was {selected_question.answer}, you lost {selected_question.point_value} points.", style="subhead")
        console.print(f"Your current score is {player.score}.")
        
        
    selected_question.point_value = ""
    selected_question.save()

    if player.questions_answered() < 30:
        play_game(player)
    else:
        end_game(player)

def select_category(player):

    console.print("Select a question: ", style="subhead")
    
    selected_category = input("Type a category name: ").strip()
    selected_category = selected_category.lower()

    if selected_category in EXIT_WORDS:
        exit_program()
    
    # if input category is not one of our categories, re-run the function
    if selected_category not in ['javascript', 'react', 'python', 'sql', 'comp sci', 'git']:
        console.print('Invalid category selection!')
        return select_category(player)

    # if input points it not a valid point value, re-run the function
    selected_points = input("Type a question amount: $").strip()
    
    try:
        if selected_points in EXIT_WORDS:
            exit_program()

        # if input cannot be converted to an integer, function will be run back
        points = int(selected_points)
    
    except ValueError:
        print('You must input a valid number!')
        select_category(player)
        
    category = Category.find_by_name(selected_category)
    
    # if player enters an invalid question amount
    if points not in [question.point_value for question in category.category_questions() if question.point_value]:
        console.print('Invalid question amount!')
        return select_category(player)
    
    select_question(category, points, player)

def select_question(category, points, player):
    global timer_expired_flag
      
    selected_question = next((question for question in category.category_questions() 
                              if question.point_value == points), None)
    
    if selected_question:

        doubleJeopardy = False
         # Create a 10-second timer
        timer = Timer(15, timer_expired, args=(selected_question, player, doubleJeopardy))
        timer.start()
        
        # 8% chance that double jeopardy will be set to True
        if random.randint(1, 100) <= 8:
            console.print('DOUBLE JEOPARDY!!!', style="subhead")
            doubleJeopardy = True
        
        console.print("You have 15 seconds to answer the question.", style="subhead")
        console.print(selected_question.question_text, style="subhead")
        
        user_answer = ""
        
        while not timer_expired_flag and not user_answer:
            user_answer = input("What is... ").strip()

        if not timer_expired_flag:
            timer.cancel()

        if user_answer in EXIT_WORDS:
            timer.cancel()
            exit_program()

    else:
        console.print("You've already answered that one! Please pick another one.")
        select_category(player)
        
    check_answer(selected_question, user_answer, player, doubleJeopardy)

def timer_expired(selected_question, player, doubleJeopardy):
    global timer_expired_flag  # Declare that you're using the global variable
    
    console.print("Time's up! Press Enter to continue", style="subhead")
    
    user_answer = ""
    
    timer_expired_flag = True  # Set the flag to True

    if user_answer in EXIT_WORDS:
        exit_program()
    