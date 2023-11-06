# question.py
from models.__init__ import CONN

class Question:
    def __init__(self, question_text, answer, point_value, category_id):
        self.id = None
        self.question_text = question_text
        self.answer = answer
        self.point_value = point_value
        self.category_id = category_id

    @staticmethod
    def create_question(question_text, answer, point_value, category_id):
        # Create a new question in the database.
        cursor = CONN.cursor()
        cursor.execute("INSERT INTO questions (question_text, answer, point_value, category_id) VALUES (?, ?, ?, ?)",
                       (question_text, answer, point_value, category_id))
        CONN.commit()

    @staticmethod
    def delete_question(question_id):
        # Delete a question from the database.
        cursor = CONN.cursor()
        cursor.execute("DELETE FROM questions WHERE id = ?", (question_id,))
        CONN.commit()
        
    def save(self):
        """Save the current instance to the database."""
        cursor = CONN.cursor()
        if self.id is None:
            cursor.execute('INSERT INTO questions (question_text, answer, point_value, category_id) VALUES (?, ?, ?, ?)',
                           (self.question_text, self.answer, self.point_value, self.category_id))
            self.id = cursor.lastrowid
        else:
            cursor.execute('UPDATE questions SET question_text = ?, answer = ?, point_value = ?, category_id = ? WHERE id = ?',
                           (self.question_text, self.answer, self.point_value, self.category_id, self.id))
        CONN.commit()

    @staticmethod
    def find_question_by_id(question_id):
        # Find a question by its ID.
        cursor = CONN.cursor()
        cursor.execute("SELECT * FROM questions WHERE id = ?", (question_id,))
        question = cursor.fetchone()
        return question

    @staticmethod
    def get_all():
        # Retrieve all questions from the database.
        cursor = CONN.cursor()
        cursor.execute("SELECT * FROM questions")
        questions = cursor.fetchall()
        return questions
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY,
                question_text TEXT,
                answer TEXT,
                point_value INT,
                category_id INT
            )
        """
        cursor = CONN.cursor()
        cursor.execute(sql)
        CONN.commit()
        
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS questions
        """
        cursor = CONN.cursor()
        cursor.execute(sql)
        CONN.commit()
