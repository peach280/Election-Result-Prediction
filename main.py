
from translator import translate
import csv
from textblob import TextBlob

# Function to read tweets from CSV
def read_tweets(file_path: str) -> list[dict[str, str]]:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            list_of_tweets = list(reader)
    except UnicodeDecodeError:
        with open(file_path, "r", encoding="ISO-8859-1", errors="ignore") as file:
            reader = csv.DictReader(file)
            list_of_tweets = list(reader)
    return list_of_tweets


# Function to predict sentiment of a tweet
def predict_sentiment(text: str) -> str:
    # Create a TextBlob object and use sentiment analysis
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity  # Returns a score between -1 and 1
    if sentiment_score > 0:
        return "positive"
    elif sentiment_score < 0:
        return "negative"
    else:
        return "neutral"

# Main script
tweets = read_tweets("./merged_output.csv")
results = []

for tweet in tweets:
    tweet_text, language,likes,retweets = tweet["text"], tweet["lang"],tweet["likeCount"],tweet["retweetCount"]

    if language == "en":
        sentiment = predict_sentiment(tweet_text)
    else:
        translated_text, language = translate(tweet_text)
        sentiment = predict_sentiment(translated_text)

    # Store the result with tweet text and sentiment
    results.append({
        "text": tweet_text,
        "language": language,
        "sentiment": sentiment,
        "likes":likes,
        "retweets":retweets
    })

# Optionally, write the results to a new CSV file
with open("tweet_sentiments.csv", "w", newline="",encoding="utf-8") as file:
    fieldnames = ["text", "language", "sentiment","likes","retweets"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for result in results:
        writer.writerow(result)





