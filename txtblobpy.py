from textblob import TextBlob

data= "chirag is a boy"

blob= TextBlob(data)

#print(dir(blob))

print(blob.sentiment.polarity)


import tweepy


bearer_token = "AAAAAAAAAAAAAAAAAAAAAEmScQEAAAAA1jCSvfkqrUly%2BKw0EoMXx2IGl0c%3D2YyRI3TyA9iTQSxIczNzvcf6sII2nXjP7k12PLxha6aLBJRkmY"


consumer_key = "K9w5YYmEybknTVuDtHxekND9B"
consumer_secret = "PVJ24PVC7DUAIS0nugR6JZW7EMSUeoXvBMAEPHWBrqVWymbMEV"


access_token = "909258293960257536-p6G2bhIS0i1sPqePuMups8Lugk7X6zL"
access_token_secret = "Dizyzd3lTDH8zGLSocJDiYLfzTVbHYApo0RlbbaMCV9vE"

# You can authenticate as your app with just your bearer token
client = tweepy.Client(bearer_token=bearer_token)

# You can provide the consumer key and secret with the access token and access
# token secret to authenticate as a user
client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)


print(dir(client))

client.get_tweets()
print(client.get_tweets)