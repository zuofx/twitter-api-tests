import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
queryInput = input("Enter search query: ")
if (queryInput != "--"):
    query = (queryInput + " -is:retweet lang:en")
    response = client.search_recent_tweets(query=query, max_results=10, tweet_fields=["created_at", "lang", "source"], expansions=["author_id"])
    users = {u["id"]: u for u in response.includes["users"]}
    for tweet in response.data:
        if users[tweet.author_id]:
            user = users[tweet.author_id]
            print("Tweeter: " + user.username.upper())
            print("------- CONTENTS -------")
            print(tweet.text)
            print("------- OTHER INFORMATION -------")
            print("Tweet ID: " + str(tweet.id))
            print("Tweet Date: " + str(tweet.created_at))
            print("Tweet Source: " + str(tweet.source))
            print("Tweet URL: https://twitter.com/" + user.username + "/status/" + str(tweet.id))
            print("")