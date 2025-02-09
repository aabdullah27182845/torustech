import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level
from database import Database

async def main():

    # Continue with the rest of your scraper logic:
    api = API()
    
    # API Usage for real

    await gather(api.search("crypto", limit=1, kv={"product": "List"}))
    tweet_id = 1
    await api.tweet_details(tweet_id)
    await gather(api.tweet_replies(tweet_id, limit=20))






if __name__ == '__main__':
    asyncio.run(main())