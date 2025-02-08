from accounts import setup_database, get_accounts

class Database:

    def __init__(self):
        setup_database()
    
    def get_accounts(self):
        return get_accounts()