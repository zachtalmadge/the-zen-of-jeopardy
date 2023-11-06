# category.py
from models.__init__ import CONN  # Import the connection from the __init__.py module within the same package

class Category:
    """Represents a category for quiz questions."""

    def __init__(self, name, questions=None, category_id=None):
        """Initialize a new Category instance."""
        self.id = category_id
        self.name = name
        self.questions = questions if questions is not None else []

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
    def create(cls, name, questions=None):
        new_category = cls(name, questions)
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

    @staticmethod
    def get_all():
        """Retrieve all categories from the database."""
        cursor = CONN.cursor()
        cursor.execute('SELECT * FROM categories')
        return cursor.fetchall()

    @staticmethod
    def find_by_id(category_id):
        """Find a category by its ID."""
        cursor = CONN.cursor()
        cursor.execute('SELECT * FROM categories WHERE id = ?', (category_id,))
        return cursor.fetchone()

    @staticmethod
    def find_by_name(name):
        """Find a category by its name."""
        cursor = CONN.cursor()
        cursor.execute('SELECT * FROM categories WHERE name = ?', (name,))
        return cursor.fetchone()

    @staticmethod
    def delete(category_id):
        """Delete a category by its ID."""
        with CONN:
            cursor = CONN.cursor()
            cursor.execute('DELETE FROM categories WHERE id = ?', (category_id,))
    
        

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