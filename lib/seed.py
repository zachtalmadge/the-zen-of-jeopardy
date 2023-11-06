from models.User import User
from models.Category import Category
from models.Question import Question

def drop_tables():
    User.drop_table()
    Category.drop_table()

def create_tables():
    User.create_table()
    Category.create_table()

def seed_jeopardy_board():
    js_category = Category.create("Javascript")
    react_category = Category.create("React")
    python_category = Category.create("Python")
    sql_category = Category.create("SQL")
    comp_sci_category = Category.create("Comp Sci")
    git_category = Category.create("Git")
    
    js_q1 = Question.create_question('This data type is used to store true or false values', 'boolean', 200, js_category.id)
    js_q2 = Question.create_question('This operator is used to compare both value and type.', 'strict equality operator', 400, js_category.id)
    js_q3 = Question.create_question('This global function parses a string argument and returns an integer of the specified radix or base.', 'parseInt', 600, js_category.id)
    js_q4 = Question.create_question('This data type is used to store true or false values', 'boolean', 800, js_category.id)
    js_q5 = Question.create_question('This data type is used to store true or false values', 'boolean', 100, js_category.id)
    
    js_category.questions = [js_q1, js_q2, js_q3, js_q4, js_q5]
    
    react_q1 = Question.create_question('This React-specific syntax allows you to write HTML structures within JavaScript code.', 'JSX', 200, react_category.id)
    react_q2 = Question.create_question('This React feature allows you to return multiple elements from a component’s render method without creating an additional DOM element.', 'fragments', 400, react_category.id)
    react_q3 = Question.create_question('This term refers to React\'s way of converting elements and components into DOM nodes and objects.', 'rendering', 600, react_category.id)
    react_q4 = Question.create_question('This is a pattern used in React to share functionality between components without having to maintain a parent-child relationship.', 'higher-order components', 800, react_category.id)
    react_q5 = Question.create_question('This new feature, introduced in React 16.8, allows you to use state and other React features without writing a class.', 'hooks', 1000, react_category.id)
    
    react_category.questions = [react_q1, react_q2, react_q3, react_q4, react_q5]
    
    python_q1 = Question.create_question('This function creates a new list where each element is the result of applying a given function to the corresponding item of an iterable.', 'map()', 200, python_category.id)
    python_q2 = Question.create_question('This type of loop iterates over a sequence of numbers generated by the range() function.', 'map()', 'for loop', python_category.id)
    python_q3 = Question.create_question('This error is raised when you try to access an index that is out of bounds for a sequence.', 'IndexError', 600, python_category.id)
    python_q4 = Question.create_question('This term refers to an object\'s ability to take on multiple forms depending on the context.', 'polymorphism', 800, python_category.id)
    python_q5 = Question.create_question('This method is called to initialize a new object when a class is instantiated.', '__init__', 1000, python_category.id)
    
    python_category.questions = [python_q1, python_q2, python_q3, python_q4, python_q5]
    
    sql_q1 = Question.create_question('This SQL clause is used to specify a condition while fetching data from a single table or joining with multiple tables.', 'where', 200, sql_category.id)
    sql_q2 = Question.create_question('This statement is used to remove a record from a table.', 'delete', 400, sql_category.id)
    sql_q3 = Question.create_question('This clause is used to sort the result set in ascending or descending order.', 'order by', 600, sql_category.id)
    sql_q4 = Question.create_question('This clause is used to arrange identical data into groups with the data summary.', 'group by', 800, sql_category.id)
    sql_q5 = Question.create_question('This function returns the number of rows that matches a specified criterion.', 'count()', 1000, sql_category.id)
    
    sql_category.questions = [sql_q1, sql_q2, sql_q3, sql_q4, sql_q5]
    
    comp_sci_q1 = Question.create_question('This is the basic building block of all programs, consisting of a sequence of instructions executed sequentially by a CPU.', 'algorithm', 200, comp_sci_category.id)
    comp_sci_q2 = Question.create_question('This common data structure operates on a First In, First Out (FIFO) principle.', 'queue', 400, comp_sci_category.id)
    comp_sci_q3 = Question.create_question('This is the term for an error in a program that prevents it from running as expected.', 'bug', 600, comp_sci_category.id)
    comp_sci_q4 = Question.create_question('This search algorithm sequentially checks each element of the list until a match is found or the whole list has been searched.', 'linear search', 800, comp_sci_category.id)
    comp_sci_q5 = Question.create_question('This type of memory is temporary and volatile, and is used to store data that is actively being worked on by the CPU.', 'ram', 1000, comp_sci_category.id)
    
    comp_sci_category.questions = [comp_sci_q1, comp_sci_q2, comp_sci_q3, comp_sci_q4, comp_sci_q5]
    
    git_q1 = Question.create_question('This Git command is used to create a copy of a repository on your local machine.', 'git clone', 200, git_category.id)
    git_q2 = Question.create_question('This Git command shows the file differences which are not yet staged.', 'git diff', 400, git_category.id)
    git_q3 = Question.create_question('This command is used to save changes to the local repository after staging with git add.', 'git commit', 600, git_category.id)
    git_q4 = Question.create_question('This Git command is used to connect a local repository to a remote server, setting the remote as the default for future pushes.', 'git remote add origin', 800, git_category.id)
    git_q5 = Question.create_question('This Git command is used to download changes from the remote repository to your local working directory.', 'git pull', 1000, git_category.id)
    
    git_category.questions = [git_q1, git_q2, git_q3, git_q4, git_q5]
    

if __name__ == "__main__":
    drop_tables()
    print("Tables dropped!")
    create_tables()
    print("Tables created!")
    seed_tables()
    print("Seed data complete!")