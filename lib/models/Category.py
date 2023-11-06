# category.py
from models.__init__ import CONN  # Import the connection from the __init__.py module within the same package

class Category:
    """Represents a category for quiz questions."""

    def __init__(self, name, id=None):
        """Initialize a new Category instance."""
        self.id = id
        self.name = name

    @staticmethod
    def create_table():
        """Create the category table in the database if it does not exist."""
        with CONN:
            cursor = CONN.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS categories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE
                )
            ''')

    @classmethod
    def drop_table(cls):
        with CONN:
            cursor = CONN.cursor()
            cursor.execute('DROP TABLE IF EXISTS categories')

    @classmethod
    def create(cls, name):
        new_category = cls(name)
        new_category.save()
        return new_category

    def save(self):
        """Save the current instance to the database."""
        with CONN:
            cursor = CONN.cursor()
            if self.id is None:
                cursor.execute('INSERT INTO categories (name) VALUES (?)', (self.name,))
                self.id = cursor.lastrowid
            else:
                cursor.execute('UPDATE categories SET name = ? WHERE id = ?', (self.name, self.id))

    @classmethod
    def get_all(cls):
        """Retrieve all categories from the database."""
        cursor = CONN.cursor()
        cursor.execute('SELECT * FROM categories')
        rows = cursor.fetchall()
        return [cls(row[1], row[0]) for row in rows]

    @classmethod
    def find_by_id(cls, category_id):
        """Find a category by its ID."""
        cursor = CONN.cursor()
        cursor.execute('SELECT * FROM categories WHERE id = ?', (category_id,))
        row = cursor.fetchone()
        return cls(row[1], row[0]) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Find a category by its name."""
        cursor = CONN.cursor()
        cursor.execute('SELECT * FROM categories WHERE name = ?', (name,))
        row = cursor.fetchone()
        return cls(row[1], row[0]) if row else None

    @staticmethod
    def delete(category_id):
        """Delete a category by its ID."""
        with CONN:
            cursor = CONN.cursor()
            cursor.execute('DELETE FROM categories WHERE id = ?', (category_id,))
    
    def category_questions(self):
        from models.Question import Question
        return [question for question in Question.get_all() if question.category_id == self.id]    

# Example usage
if __name__ == "__main__":
    # Create the categories table
    Category.create_table()

    # Create a new category
    new_category = Category('Science')
    new_category.save()  # Save the new category to the database

    # Get all categories
    all_categories = Category.get_all()
    print(all_categories)

    # Find a category by ID
    category = Category.find_by_id(1)
    print(category)

    # Find a category by name
    category = Category.find_by_name('Science')
    print(category)

    # Update a category
    category_to_update = Category('Mathematics', category_id=1)
    category_to_update.save()

    # Delete a category
    Category.delete(1)