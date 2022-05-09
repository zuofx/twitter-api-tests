import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

userInput = input("Enter username: ")
newuser = client.get_user(username=userInput)
newID = newuser.data.id
tweets = client.get_users_tweets(id=newID,max_results=10, tweet_fields=["lang"])
for tweet in tweets.data:
    print("Tweeter: " + userInput.upper())
    print("------- CONTENTS -------")
    print(tweet.text)
    print("------- OTHER INFORMATION -------")
    print("Tweet ID: " + str(tweet.id))
    print("Tweet Date: " + str(tweet.created_at))
    print("Tweet Source: " + str(tweet.source))
    print("Tweet URL: https://twitter.com/" + userInput + "/status/" + str(tweet.id))
    print("")