from models.User import User
from models.Category import Category
from models.Question import Question
from helpers import console

def drop_tables():
    Question.drop_table()
    Category.drop_table()

def create_tables():
    User.create_table()
    Category.create_table()
    Question.create_table()

def seed_jeopardy_board():
    js_category = Category.create("javascript")
    react_category = Category.create("react")
    python_category = Category.create("python")
    sql_category = Category.create("sql")
    comp_sci_category = Category.create("comp sci")
    git_category = Category.create("git")
    
    js_q1 = Question.create_question("It's the term for the phenomenon that occurs when you compare two objects in JavaScript using the loose equality operator '=='", 'type coercion', 200, 1,  js_category.id)
    js_q2 = Question.create_question('Every JavaScript object has this property, which is a reference to another object from which properties are inherited.', 'prototype', 400, 2, js_category.id)
    js_q3 = Question.create_question('This ES6 feature allows for the extraction of data from arrays or objects into distinct variables.', 'destructuring', 600, 3, js_category.id)
    js_q4 = Question.create_question('This term refers to a feature in JavaScript and other programming languages where a function retains access to its lexical scope even when it\'s invoked outside of that scope.', 'closure', 800, 4, js_category.id)
    js_q5 = Question.create_question('Everything in JavaScript that is not a primitive value is this', 'object', 1000, 5, js_category.id)
        
    react_q1 = Question.create_question('This React-specific syntax allows you to write HTML structures within JavaScript code.', 'JSX', 200, 1, react_category.id)
    react_q2 = Question.create_question('This React feature allows you to return multiple elements from a component’s render method without creating an additional DOM element.', 'fragments', 400, 2, react_category.id)
    react_q3 = Question.create_question('This term refers to React\'s way of converting elements and components into DOM nodes and objects.', 'rendering', 600, 3, react_category.id)
    react_q4 = Question.create_question('This is a pattern used in React to share functionality between components without having to maintain a parent-child relationship.', 'higher-order components', 800, 4, react_category.id)
    react_q5 = Question.create_question("It's the algorithm React uses to determine which changes need to be sent to the DOM.", 'reconciliation', 1000, 5, react_category.id)
        
    python_q1 = Question.create_question('This is the default Python memory management technique which reclaims blocks of memory that no longer are in use.', 'garbage collection', 200, 1, python_category.id)
    python_q2 = Question.create_question('In Python, this type of variable is one that is shared by all instances of a class. It is defined within a class but outside any instance methods.', 'class variable', 400, 2, python_category.id)
    python_q3 = Question.create_question('This error is raised when you try to access an index that is out of bounds for a sequence.', 'IndexError', 600, 3, python_category.id)
    python_q4 = Question.create_question('This term refers to an object\'s ability to take on multiple forms depending on the context.', 'polymorphism', 800, 4, python_category.id)
    python_q5 = Question.create_question('This method is called to initialize a new object when a class is instantiated.', '__init__', 1000, 5, python_category.id)
        
    sql_q1 = Question.create_question('This SQL clause is used to specify a condition while fetching data from a single table or joining with multiple tables.', 'where', 200, 1, sql_category.id)
    sql_q2 = Question.create_question('This statement is used to remove a record from a table.', 'delete', 400, 2, sql_category.id)
    sql_q3 = Question.create_question('This clause is used to sort the result set in ascending or descending order.', 'order by', 600, 3, sql_category.id)
    sql_q4 = Question.create_question('This clause is used to arrange identical data into groups with the data summary.', 'group by', 800, 4, sql_category.id)
    sql_q5 = Question.create_question('This function returns the number of rows that matches a specified criterion.', 'count()', 1000, 5, sql_category.id)
        
    comp_sci_q1 = Question.create_question('This is the basic building block of all programs, consisting of a sequence of instructions executed sequentially by a CPU.', 'algorithm', 200, 1, comp_sci_category.id)
    comp_sci_q2 = Question.create_question('This common data structure operates on a First In, First Out (FIFO) principle.', 'queue', 400, 2, comp_sci_category.id)
    comp_sci_q3 = Question.create_question('This is the term for an error in a program that prevents it from running as expected.', 'bug', 600, 3, comp_sci_category.id)
    comp_sci_q4 = Question.create_question('This search algorithm sequentially checks each element of the list until a match is found or the whole list has been searched.', 'linear search', 800, 4, comp_sci_category.id)
    comp_sci_q5 = Question.create_question('This type of memory is temporary and volatile, and is used to store data that is actively being worked on by the CPU.', 'ram', 1000, 5, comp_sci_category.id)
        
    git_q1 = Question.create_question('This Git command is used to create a copy of a repository on your local machine.', 'git clone', 200, 1, git_category.id)
    git_q2 = Question.create_question('This Git command shows the file differences which are not yet staged.', 'git diff', 400, 2, git_category.id)
    git_q3 = Question.create_question('This command is used to save changes to the local repository after staging with git add.', 'git commit', 600, 3, git_category.id)
    git_q4 = Question.create_question('This Git command is used to connect a local repository to a remote server, setting the remote as the default for future pushes.', 'git remote add origin', 800, 4, git_category.id)
    git_q5 = Question.create_question('This Git command is used to download changes from the remote repository to your local working directory.', 'git pull', 1000, 5, git_category.id)
        

def resetGame():
    drop_tables()
    create_tables()
    seed_jeopardy_board()
    console.print('Game has been reset', style="heading")

if __name__ == "__main__":
    resetGame()
    print("banana")