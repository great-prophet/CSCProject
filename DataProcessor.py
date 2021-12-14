import datetime
from statistics import mean
from DataModels import *

class DataProcessor:

    def __init__(self):
        pass

    def average_by_group(self, data: StatsNormed) -> StatsGrouped:

        grouped = {}
        normed_dates = self.normalize_dates(data)

        for date, val in zip(normed_dates.times, normed_dates.stats):
            if date in grouped:
                grouped[date].append(val)
            else:
                grouped[date] = [val]

        averaged = {d: mean(v) for d, v in grouped.items()}

        return StatsGrouped(averaged)


    def normalize_covid_data(self, data: CovidStatsRaw) -> StatsNormed:
        all_vals = [v for d, v in zip(data.times, data.stats)]
        max_v = max(all_vals)
        min_v = min(all_vals)

        norm_data_times = []
        norm_data_stats = []

        for date, val in zip(data.times, data.stats):
            norm_val = (val - min_v) / (max_v - min_v)
            norm_data_times.append(date)
            norm_data_stats.append(norm_val)

        return StatsNormed(norm_data_times, norm_data_stats)


    def normalize_dates(self, data: StatsNormed) -> StatsDatesNormed:

        norm_data_times = []
        norm_data_stats = []

        for date, val in zip(data.times, data.stats):
            # week number
            norm_date = (date.month * 4) + (date.day // 4)
            norm_data_times.append(norm_date)
            norm_data_stats.append(val)

        return StatsDatesNormed(norm_data_times, norm_data_stats)


    def merge_data(self, grouped_sentiment_data: StatsGrouped, grouped_covid_data: StatsGrouped) -> PointsXYVectors:

        sentiment_data = []
        covid_data = []

        for date, val in grouped_covid_data.timed_stats.items():
            if date in grouped_sentiment_data.timed_stats:
                sentiment_data.append(grouped_sentiment_data.timed_stats[date])
                covid_data.append(val)

        return PointsXYVectors(covid_data, sentiment_data)
