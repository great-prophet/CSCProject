import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from src.DataModels import TweetsRaw, StatsNormed


class SentimentProcessor:
    """
    A system that calculates sentiment based on tweets from the relevant dataset.
    """

    def __init__(self) -> None:

        # download sentiment analysis data models
        nltk.download('vader_lexicon')

        self.sia = SentimentIntensityAnalyzer()


    def convert_tweets_to_sentiment(self, tweets_data: TweetsRaw) -> StatsNormed:
        """Returns a StatsNormed object containing the sentiment data calculated using nltk's sentiment analysis
        model.
        """  
        sentiment_data_times = []
        sentiment_data_stats = []


        for date, text in zip(tweets_data.times, tweets_data.tweets):
            sentiment_score = self.score_text(text)
            sentiment_data_times.append(date)
            sentiment_data_stats.append(sentiment_score)

        return StatsNormed(sentiment_data_times, sentiment_data_stats)

    def score_text(self, text: str) -> float:
        """
        Returns a float representing the sentiment score of the tweet.
        """
        scores = self.sia.polarity_scores(text)
        return scores['compound']

