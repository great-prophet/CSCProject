import datetime

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


class SentimentProcessor:
    """
    A system that calculates sentiment based on tweets from the relevant dataset.
    """

    def __init__(self) -> None:

        # download sentiment analysis data models
        nltk.download('vader_lexicon')

        self.sia = SentimentIntensityAnalyzer()

    def convert_tweets_to_sentiment(self, tweets_data: list[tuple[datetime.date, str]]) -> list[tuple[datetime.date, float]]:
        """
        Returns a list of tuples containing the sentiment data calculated using nltk's sentiment analysis
        model.
        """
        sentiment_data = []

        for date, text in tweets_data:
            sentiment_score = self.score_text(text)
            sentiment_data.append((date, sentiment_score))

        return sentiment_data

    def score_text(self, text: str) -> float:
        """
        Returns a float representing the sentiment score of the tweet.
        """
        scores = self.sia.polarity_scores(text)
        return scores['compound']

    def test(self) -> None:
        """
        A test of the scoring model.
        """
        scores = self.sia.polarity_scores("Wow! Hyunjin is so cool.")
        return scores


if __name__ == "__main__":
    sp = SentimentProcessor()
    print(sp.test())
