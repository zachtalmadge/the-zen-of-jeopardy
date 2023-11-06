# question.py
from models.__init__ import CONN

class Question:
    def __init__(self, question_text, answer, point_value, level, category_id, id=None):
        self.id = id
        self.question_text = question_text
        self.answer = answer
        self.point_value = point_value
        self.level = level
        self.category_id = category_id

    def create_question(question_text, answer, point_value, level, category_id):
        # Create a new question in the database.
        cursor = CONN.cursor()
        cursor.execute("INSERT INTO questions (question_text, answer, point_value, level, category_id) VALUES (?, ?, ?, ?, ?)",
                       (question_text, answer, point_value, level, category_id))
        CONN.commit()

    def delete_question(question_id):
        # Delete a question from the database.
        cursor = CONN.cursor()
        cursor.execute("DELETE FROM questions WHERE id = ?", (question_id,))
        CONN.commit()
        
    def save(self):
        """Save the current instance to the database."""
        cursor = CONN.cursor()
        if self.id is None:
            cursor.execute('INSERT INTO questions (question_text, answer, point_value, level, category_id) VALUES (?, ?, ?, ?, ?)',
                           (self.question_text, self.answer, self.point_value, self.level, self.category_id))
            self.id = cursor.lastrowid
        else:
            cursor.execute('UPDATE questions SET question_text = ?, answer = ?, point_value = ?, level = ?, category_id = ? WHERE id = ?',
                           (self.question_text, self.answer, self.point_value, self.level, self.category_id, self.id))
        CONN.commit()

    def find_question_by_id(question_id):
        # Find a question by its ID.
        cursor = CONN.cursor()
        cursor.execute("SELECT * FROM questions WHERE id = ?", (question_id,))
        question = cursor.fetchone()
        return question

    @classmethod
    def get_all(cls):
        # Retrieve all questions from the database.
        cursor = CONN.cursor()
        cursor.execute("SELECT * FROM questions")
        rows = cursor.fetchall()
        return [cls(row[1], row[2], row[3], row[4], row[5], row[0]) for row in rows]
    
    @classmethod
    def get_questions_by_level(cls, level):
        # Retrieve a list of questions based on point_value.
        cursor = CONN.cursor()
        cursor.execute("""SELECT * FROM questions 
                        WHERE level = ? 
                       """, (level,))
        rows = cursor.fetchall()

        if rows:
            # If a question is found, create a Question object and return it
            return [cls(row[1], row[2], row[3], row[4], row[5], row[0]) for row in rows]
        else:
            # If no question is found, return None
            return None
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY,
                question_text TEXT,
                answer TEXT,
                point_value INT,
                level INT,
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

    def find_question(self, points):
        return self if self.point_value == points else None
    
