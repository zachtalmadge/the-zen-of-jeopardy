from models.User import User
from models.Category import Category

def drop_tables():
    User.drop_table()
    Category.drop_table()

def create_tables():
    User.create_table()
    Category.create_table()

def seed_tables():
    cat1 = Category.create("Javascript")
    cat2 = Category.create("React")
    cat3 = Category.create("Python")
    cat4 = Category.create("SQL")
    cat5 = Category.create("Comp Sci")
    cat6 = Category.create("Git")

if __name__ == "__main__":
    drop_tables()
    print("Tables dropped!")
    create_tables()
    print("Tables created!")
    seed_tables()
    print("Seed data complete!")