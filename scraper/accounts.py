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
    u_pass = Column(String, nullable=False)
    email_password = Column(String, nullable=False)

def setup_database():
    # Create an SQLite database file named 'users.db'
    engine = create_engine('sqlite:///users.db', echo=True)
  
    # Create the users table (and any other defined tables)
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Check if the users table is empty
    if not session.query(User).first():
        users_data = [
            {'email': 'abdullahabdullah2104@gmail.com', 'username': 'HoudA3603188522', 'u_pass': '@Bdullah2100', 'email_password': '@Bdullah2100'},
            {'email': 'user2@example.com', 'username': 'user2', 'u_pass': 'pass2', 'email_password': 'pass2'},
            {'email': 'user3@example.com', 'username': 'user3', 'u_pass': 'pass3', 'email_password': 'pass3'},
            {'email': 'user4@example.com', 'username': 'user4', 'u_pass': 'pass4', 'email_password': 'pass4'},
            {'email': 'user5@example.com', 'username': 'user5', 'u_pass': 'pass5', 'email_password': 'pass5'},
        ]

        # Insert the user records into the database
        for data in users_data:
            user = User(email=data['email'], username=data['username'], u_pass=data['u_pass'], email_password=data['email_password'])
            session.add(user)
  
        session.commit()

    # Verify the records have been inserted
    print("Users in the database:")
    for user in session.query(User).all():
        print(f"id: {user.id}, email: {user.email}, username: {user.username}, username_password: {user.u_pass}, email_password: {user.email_password}")

def get_accounts():
    engine = create_engine('sqlite:///users.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session.query(User).all()

if __name__ == '__main__':
    setup_database()


