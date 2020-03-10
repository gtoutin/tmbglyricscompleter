import twitter
import os

# keys and secrets are pulled from .env file

def getApi():
  return twitter.Api(consumer_key=os.getenv("cons_key"), 
                      consumer_secret=os.getenv("cons_secret"),
                      access_token_key=os.getenv("access_token"),
                      access_token_secret=os.getenv("access_secret"))