import csv
import matplotlib.pyplot as plt
def read_tweets(file_path:str) -> list[dict[str,str]]:
    try:
        with open(file_path,"r",encoding="utf-8") as file:
            reader=csv.DictReader(file)
            list_of_tweets=list(reader)
    except UnicodeDecodeError:
        with open(file_path, "r", encoding="ISO-8859-1", errors="ignore") as file:
            reader = csv.DictReader(file)
            list_of_tweets = list(reader)
    return list_of_tweets
tweets=read_tweets("./tweet_sentiments.csv")
score_bjp = {'positive': 0, 'negative': 0, 'neutral': 0}
score_congress = {'positive': 0, 'negative': 0, 'neutral': 0}
bjp_keywords = ["BJP", "Mahayuti","Modi","Eknath Shinde","Ajit Pawar"]
congress_keywords = ["Aghadi", "MVA", "INC", "Thackeray","Sharad Pawar"]
for tweet in tweets:
    tweet_text, likes, sentiment,retweets = tweet["text"], tweet["likes"], tweet["sentiment"],tweet["retweets"]
    try:
        likes_count = int(float(likes)) if likes else 0  
    except ValueError:
        likes_count = 0 
    
    if any(keyword in tweet_text for keyword in bjp_keywords):
        if sentiment == "positive":
            score_bjp['positive'] += 1
        elif sentiment == "negative":
            score_bjp['negative'] +=1
        elif sentiment == "neutral":
            score_bjp['neutral'] += 1
            
    elif any(keyword in tweet_text for keyword in congress_keywords):
        if sentiment == "positive":
            score_congress['positive'] += 1
        elif sentiment == "negative":
            score_congress['negative'] += 1
        elif sentiment == "neutral":
            score_congress['neutral'] += 1

print("BJP Scores:", score_bjp)
print("Congress Scores:", score_congress)
labels = ['Positive', 'Negative', 'Neutral']
bjp_scores = [score_bjp['positive'], score_bjp['negative'], score_bjp['neutral']]
congress_scores = [score_congress['positive'], score_congress['negative'], score_congress['neutral']]
x = range(len(labels))
plt.bar(x, bjp_scores, width=0.4, label='BJP', color='blue', align='center')
plt.bar([p + 0.4 for p in x], congress_scores, width=0.4, label='Congress', color='orange', align='center')
plt.xlabel('Sentiment Types')
plt.ylabel('Score')
plt.title('Sentiment Analysis of Tweets for Maharashtra Elections 2024')
plt.xticks([p + 0.2 for p in x], labels)
plt.legend()
plt.ylim(0, max(max(bjp_scores), max(congress_scores)) + 10)  
plt.show()

    