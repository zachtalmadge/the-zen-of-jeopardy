from helpers import (
    welcome,
    menu,
    exit_program,
    find_or_create_player,
    view_scoreboard,
    view_rules,
    delete_user
)

from seed import resetGame

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            find_or_create_player()
        elif choice == "2":
            view_scoreboard()
        elif choice == "3":
            view_rules()
        elif choice == "4":
            resetGame()
        elif choice == "5":
            delete_user()
        else:
            print("Invalid choice")
        
if __name__ == "__main__":
    welcome()
    main()
   