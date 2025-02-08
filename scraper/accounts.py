import sqlalchemy
from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class for our model
Base = declarative_base()

# Define the User model with id, email, username, and password fields
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

def setup_database():
    # Create an SQLite database file named 'users.db'
    engine = create_engine('sqlite:///users.db', echo=True)
  
    # Create the users table (and any other defined tables)
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # List of 5 sample user entries
    users_data = [
        {'email': 'user1@example.com', 'username': 'user1', 'password': 'pass1'},
        {'email': 'user2@example.com', 'username': 'user2', 'password': 'pass2'},
        {'email': 'user3@example.com', 'username': 'user3', 'password': 'pass3'},
        {'email': 'user4@example.com', 'username': 'user4', 'password': 'pass4'},
        {'email': 'user5@example.com', 'username': 'user5', 'password': 'pass5'},
    ]

    # Insert the user records into the database
    for data in users_data:
        user = User(email=data['email'], username=data['username'], password=data['password'])
        session.add(user)
  
    session.commit()

    # Verify the records have been inserted
    print("Users in the database:")
    for user in session.query(User).all():
        print(f"id: {user.id}, email: {user.email}, username: {user.username}, password: {user.password}")

def get_accounts():
    engine = create_engine('sqlite:///users.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session.query(User).all()

if __name__ == '__main__':
    setup_database()


