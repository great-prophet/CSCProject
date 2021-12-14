from Reader import Reader
from SentimentProcessor import SentimentProcessor
from DataProcessor import DataProcessor
from Plotter import Plotter
from Regression import Regression


class DataAnalysisSystem:
    """
    A system to analyze the data and graph findings.
    """

    def __init__(self, data_dir_path) -> None:

        # set data csv paths
        self.tweets_data_path = f"{data_dir_path}/covid19_tweets.csv"
        self.covid_canada_data_path = f"{data_dir_path}/covid19_canada.csv"
        self.covid_us_data_path = f"{data_dir_path}/covid19_us.csv"

        # data csv reader
        self.reader = Reader(self.tweets_data_path,
                             self.covid_canada_data_path,
                             self.covid_us_data_path)
        self.sp = SentimentProcessor()
        self.dp = DataProcessor()
        self.plt = Plotter()
        self.reg = Regression()

    def run_analysis_full(self) -> None:
        """
        Returns None. Computes sentiment from clean data, then creates a regression model
        to graph findings.
        """

        # load all data from reader
        tweets_raw_data = self.reader.load_tweet_data()
        cases_data = self.reader.load_cases_data()
        deaths_data = self.reader.load_deaths_data()

        # compute tweets sentiment
        tweets_sentiment_data = self.sp.convert_tweets_to_sentiment(tweets_raw_data)

        # normalize covid data
        n0_cases = self.dp.normalize_covid_data(cases_data)
        n0_deaths = self.dp.normalize_covid_data(deaths_data)

        # average groups
        n_tweets = self.dp.average_by_group(tweets_sentiment_data)
        n_cases = self.dp.average_by_group(n0_cases)
        n_deaths = self.dp.average_by_group(n0_deaths)

        # merge to point pairs
        p_cases = self.dp.merge_data(n_tweets, n_cases)
        p_deaths = self.dp.merge_data(n_tweets, n_deaths)

        # compute regression model
        c_reg = self.reg.simple_regression(p_cases)
        d_reg = self.reg.simple_regression(p_deaths)

        # plot points
        self.plt.plot_points(p_cases)
        self.plt.plot_line(c_reg)

        # plot regression lines
        self.plt.plot_points(p_deaths)
        self.plt.plot_line (d_reg)

        # set r_sq values
        self.plt.set_r_sq(c_reg.r_sq, d_reg.r_sq)

        self.plt.show()


if __name__ == "__main__":

    data_dir_path = "data"

    das = DataAnalysisSystem(data_dir_path)

    das.run_analysis_full()
