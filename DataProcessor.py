import datetime
from statistics import mean


class DataProcessor:
    """
    A system that processes cleaned data by averaging and normalizing the information.
    """

    def __init__(self):
        pass

    def average_by_group(self, data: list[tuple[datetime.date, float]]) -> dict[int, float]:
        """
        Returns a dictionary mapping the date to an average data value.
        """
        grouped = {}

        for date, val in self.normalize_dates(data):
            if date in grouped:
                grouped[date].append(val)
            else:
                grouped[date] = [val]

        averaged = {d: mean(v) for d, v in grouped.items()}

        return averaged

    def normalize_covid_data(self, data: list[tuple[datetime.date, int]]) -> list[tuple[datetime.date, float]]:
        """
        Returns a list of tuples containing normalized COVID-19 data.
        """
        all_vals = [v for d, v in data]
        max_v = max(all_vals)
        min_v = min(all_vals)

        norm_data = []

        for date, val in data:
            norm_val = (val - min_v) / (max_v - min_v)
            norm_data.append((date, norm_val))

        return norm_data

    def normalize_dates(self, data: list[tuple[datetime.date, float]]) -> list[tuple[int, float]]:
        """
        Returns a list of normalized dates from the cleaned data.
        """
        norm_data = []

        for date, val in data:
            # approximate number of weeks from 2020
            norm_date = ((date.year - 2020) * 12) + (date.month * 4) + (date.day // 4)
            norm_data.append((norm_date, val))

        return norm_data

    def merge_data(self, grouped_sentiment_data: dict[int, float], grouped_covid_data: dict[int, float]) -> tuple[list[float], list[float]]:
        """
        Returns a tuple of lists containing COVID-19 data and the related sentiment data.
        """
        sentiment_data = []
        covid_data = []

        for date, val in grouped_covid_data.items():
            if date in grouped_sentiment_data:
                sentiment_data.append(grouped_sentiment_data[date])
                covid_data.append(val)

        return (covid_data, sentiment_data)
