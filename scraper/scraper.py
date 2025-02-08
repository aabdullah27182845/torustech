import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level
from database import Database

async def main():
    # Retrieve accounts from the database
    db = Database()
    accounts = db.get_accounts()

    print("Accounts fetched from the database:")
    for account in accounts:
        print(f"ID: {account.id}, Email: {account.email}, Username: {account.username}")

    # Continue with the rest of your scraper logic:
    api = API()
    cookies = "abc=12; ct0=xyz"
    for account in accounts:
        await api.pool.add_account(username=account.username, 
                                   password=account.u_pass, 
                                   email=account.email, 
                                   email_password=account.email_password, 
                                   cookies=cookies)
    
    # API Usage for real

    await gather(api.search("crypto", limit=1, kv={"product": "List"}))
    tweet_id = 1
    await api.tweet_details(tweet_id)
    await gather(api.tweet_replies(tweet_id, limit=20))






if __name__ == '__main__':
    asyncio.run(main())