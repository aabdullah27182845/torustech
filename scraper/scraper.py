import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level
from accounts import get_accounts  # Import our get_accounts function

async def main():
    # Retrieve accounts from the database
    accounts = get_accounts()  # Synchronous call inside an async function
    print("Accounts fetched from the database:")
    for account in accounts:
        print(f"ID: {account.id}, Email: {account.email}, Username: {account.username}")

    # Continue with the rest of your scraper logic:
    api = API()
    await api.pool.add()

if __name__ == '__main__':
    asyncio.run(main())