import twitter

def getApi():
  return twitter.Api(consumer_key='HERE', 
                      consumer_secret='HERE',
                      access_token_key='HERE',
                      access_token_secret='HERE')