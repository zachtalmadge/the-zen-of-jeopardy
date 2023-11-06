# question.py
from __init__ import CONN

class Question:
    def __init__(self, text, point_value, category_id):
        self.text = text
        self.point_value = point_value
        self.category_id = category_id


    def create_question(text, point_value, category_id):
        # Create a new question in the database.
        CURSOR = CONN.CURSOR()
        CURSOR.execute("INSERT INTO questions (text, point_value, category_id) VALUES (?, ?, ?)",
                       (text, point_value, category_id))
        CONN.commit()


    def delete_question(question_id):
        # Delete a question from the database.
        CURSOR = CONN.CURSOR()
        CURSOR.execute("DELETE FROM questions WHERE id = ?", (question_id,))
        CONN.commit()
        
    def save(self):
        """Save the current instance to the database."""
        cursor = CONN.cursor()
        if self.id is None:
            cursor.execute('INSERT INTO questions (text) VALUES (?)', (self.text,))
            self.id = cursor.lastrowid
        else:
            cursor.execute('UPDATE questions SET text = ? WHERE id = ?', (self.text, self.id))
        CONN.commit()

    
    def find_question_by_id(question_id):
        # Find a question by its ID.
        CURSOR = CONN.CURSOR()
        CURSOR.execute("SELECT * FROM questions WHERE id = ?", (question_id,))
        question = CURSOR.fetchone()
        return question


    def get_all():
        # Retrieve all questions from the database.
        CURSOR = CONN.CURSOR()
        CURSOR.execute("SELECT * FROM questions")
        questions = CURSOR.fetchall()
        return questions
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY,
                text TEXT,
                point_value INT,
                
                
            )
        """
        
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS questions
        """

