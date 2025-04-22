import tweepy
import pandas as pd
import os

# Twitter API credentials
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
CSV_FILE = "jetblue_tweets.csv"

# Twitter client
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def get_jetblue_tweets():
    query = "JetBlue -is:retweet lang:en"
    tweets = client.search_recent_tweets(query=query, max_results=10, tweet_fields=["created_at", "text"])

    tweet_list = []

    if tweets.data:
        for tweet in tweets.data:
            tweet_list.append({
                "created_at": tweet.created_at,
                "text": tweet.text
            })

        # Read existing local file if available
        try:
            existing_df = pd.read_csv(CSV_FILE)
        except FileNotFoundError:
            existing_df = pd.DataFrame()

        # Append new data
        new_df = pd.DataFrame(tweet_list)
        combined_df = pd.concat([existing_df, new_df], ignore_index=True)

        # Remove duplicates
        combined_df.drop_duplicates(subset=["text"], inplace=True)

        # Save locally to repo
        combined_df.to_csv(CSV_FILE, index=False)
        print("Tweets saved locally.")
    else:
        print("No recent tweets found.")

if __name__ == "__main__":
    get_jetblue_tweets()
