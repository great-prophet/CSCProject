import csv
import datetime
from DataModels import TweetsRaw, CovidStatsRaw


class Reader:

    def __init__(self, tweets_data_path: str, covid_canada_data_path: str, covid_us_data_path):
        self.tweets_data_path = tweets_data_path
        self.covid_canada_data_path = covid_canada_data_path
        self.covid_us_data_path = covid_us_data_path

    def load_tweet_data(self) -> TweetsRaw:
        """Return a list of tuples containing dates and relevant tweets.

        The data in the file is in a csv format with 13 columns. The second column consists of the
        user's location. The ninth column has the date of the tweet. The tenth column has the tweet
        itself.
        """
        tweets_times = []
        tweets_text = []
        na = ['canada', 'us', 'seattle', 'vancouver', 'toronto', 'california',
              'alabama', 'alaska', 'american samoa', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut',
              'belaware',
              'district of columbia', 'florida', 'georgia', 'guam', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa',
              'kansas',
              'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota',
              'minor outlying islands',
              'mississippi', 'missouri', 'montana', 'nebraska', 'nevada', 'new hampshire', 'new jersey', 'new mexico',
              'new york', 'north carolina', 'north dakota', 'northern mariana islands', 'ohio', 'oklahoma', 'oregon',
              'pennsylvania', 'puerto rico', 'rhode island', 'south carolina', 'south dakota', 'tennessee', 'texas',
              'u.s. virgin islands', 'utah', 'vermont', 'virginia', 'washington', 'west virginia', 'wisconsin',
              'wyoming',
              'alberta', 'british columbia', 'manitoba', 'new brunswick', 'newfoundland and labrador',
              'northwest territories',
              'nova scotia', 'nunavut', 'ontario', 'prince edward island', 'quebec', 'saskatchewan', 'yukon']

        with open(self.tweets_data_path, encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',')
            next(reader)  # skip the header

            for row in reader:
                if row[1].lower() in na:
                    date = datetime.date(int(row[8][0:4]), int(row[8][5:7]), int(row[8][8:10]))
                    tweet = row[9]
                    tweets_times.append(date)
                    tweets_text.append(tweet)
        return TweetsRaw(tweets_times, tweets_text)

    def load_cases_data(self) -> CovidStatsRaw:
        """Return a list of tuples containing dates and North American case counts.

        The data in the files are in a csv format with 40 and 3 columns respectively. In the first file,
        the second column consists of the region's name and the fourth column has the date. The ninth
        column has the total confirmed cases. In the second file, the first column is the date and the second
        column has the confirmed cases.
        """
        cases = {}
        previous_date = datetime.date(2020, 1, 30)
        with open(self.covid_canada_data_path) as f:
            reader = csv.reader(f, delimiter=',')
            next(reader)  # skip the header

            for row in reader:
                if 'Canada' in str(row[1]):
                    date = datetime.date(int(row[3][0:4]), int(row[3][5:7]), int(row[3][8:10]))
                    timediff = date - previous_date
                    if timediff != datetime.timedelta(days=1):
                        for i in range(int(timediff.days)):
                            cases[date + datetime.timedelta(days=i + 1)] = case_count
                    case_count = int(row[8])
                    cases[date] = case_count
                    previous_date = date

        with open(self.covid_us_data_path) as f:
            reader = csv.reader(f, delimiter=',')
            next(reader)  # skip the header

            for row in reader:
                date = datetime.date(int(row[0][0:4]), int(row[0][5:7]), int(row[0][8:10]))
                case_count = int(row[1])
                if date in cases:
                    cases[date] += case_count
                else:
                    cases[date] = case_count

        total = [(day, cases[day]) for day in cases]
        total.sort()

        stats_times = [t[0] for t in total]
        stats_stats = [t[1] for t in total]

        return CovidStatsRaw(stats_times, stats_stats)

    def load_deaths_data(self) -> CovidStatsRaw:
        """Return a list of tuples containing dates and North American deaths.

        The data in the files are in a csv format with 40 and 3 columns respectively. In the first file,
        the second column consists of the region's name and the fourth column has the date. The eighth
        column has the confirmed deaths. In the second file, the first column is the date and the third
        column has the confirmed deaths.
        """
        deaths = {}
        count = 0
        previous_date = datetime.date(2020, 1, 30)
        with open(self.covid_canada_data_path) as f:
            reader = csv.reader(f, delimiter=',')
            next(reader)  # skip the header

            for row in reader:
                if 'Canada' in str(row[1]):
                    date = datetime.date(int(row[3][0:4]), int(row[3][5:7]), int(row[3][8:10]))
                    timediff = date - previous_date
                    if timediff != datetime.timedelta(days=1):
                        for i in range(int(timediff.days)):
                            deaths[date + datetime.timedelta(days=i + 1)] = death_count
                    death_count = int(row[7])
                    count += death_count
                    deaths[date] = count
                    previous_date = date

        with open(self.covid_us_data_path) as f:
            reader = csv.reader(f, delimiter=',')
            next(reader)  # skip the header

            for row in reader:
                date = datetime.date(int(row[0][0:4]), int(row[0][5:7]), int(row[0][8:10]))
                death_count = int(row[2])
                if date in deaths:
                    deaths[date] += death_count
                else:
                    deaths[date] = death_count

        total = [(day, deaths[day]) for day in deaths]
        total.sort()

        stats_times = [t[0] for t in total]
        stats_stats = [t[1] for t in total]

        return CovidStatsRaw(stats_times, stats_stats)
