import pandas as pd
from textblob import TextBlob
from datetime import datetime

# Load old labeled dataset
old_df = pd.read_csv('Tweets_old.csv', encoding='ISO-8859-1')

# Load new Twitter API dataset
new_df = pd.read_csv('jetblue_tweets.csv')  # This contains "created_at" and "text"

# Define sentiment analysis functions
def get_sentiment(text):
    if pd.isna(text):
        return None
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return 'positive'
    elif polarity < -0.1:
        return 'negative'
    return 'neutral'

def get_sentiment_confidence(text):
    if pd.isna(text):
        return None
    return abs(TextBlob(text).sentiment.polarity)

# Apply sentiment analysis to new tweets
sentiments = new_df['text'].apply(get_sentiment)
confidences = new_df['text'].apply(get_sentiment_confidence)

# Build a matching format for new_df
new_df_formatted = pd.DataFrame({
    'tweet_id': [None] * len(new_df),
    'airline_sentiment': sentiments,
    'airline_sentiment_confidence': confidences,
    'negativereason': [None] * len(new_df),
    'negativereason_confidence': [None] * len(new_df),
    'airline': ['JetBlue'] * len(new_df),
    'airline_sentiment_gold': [None] * len(new_df),
    'name': [None] * len(new_df),
    'negativereason_gold': [None] * len(new_df),
    'retweet_count': [0] * len(new_df),
    'text': new_df['text'],
    'tweet_coord': [None] * len(new_df),
    'tweet_created': pd.to_datetime(new_df['created_at']).dt.strftime('%m/%d/%y %H:%M'),
    'tweet_location': [None] * len(new_df),
    'user_timezone': [None] * len(new_df)
})

# Combine both datasets
combined_df = pd.concat([old_df, new_df_formatted.dropna(axis=1, how='all')], ignore_index=True)

# Save the result
combined_df.to_csv('updated_jetblue_dataset.csv', index=False)
