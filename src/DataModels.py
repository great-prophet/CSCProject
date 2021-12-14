from dataclasses import dataclass
from datetime import date


@dataclass
class TweetsRaw:
    """
    A custom data type that represents the text of tweets with the date that it was posted.

    Representation Invariants:
        - times
        - tweets
        - len(times) == len(tweets)
    """
    times: list[date]
    tweets: list[str]


@dataclass
class CovidStatsRaw:
    """
    A custom data type that represents covid stats (cases or deaths) with the date that it
    corresponds to.

    Representation Invariants:
        - times
        - stats
        - len(times) == len(stats)
    """
    times: list[date]
    stats: list[int]


@dataclass
class StatsNormed:
    """
    A custom data type that represents covid stats normalized to be between 0 and 1 with the date
    that it corresponds to.

    Representation Invariants:
        - times
        - stats
        - len(times) == len(stats)
    """
    times: list[date]
    stats: list[float]


@dataclass
class StatsDatesNormed:
    """
    A custom data type that represents float covid stats (tweet sentiment, normalized cases/deaths)
    with the date that it corresponds to represented as an integer.

    Representation Invariants:
        - times
        - stats
        - len(times) == len(stats)
    """
    times: list[int]
    stats: list[float]


@dataclass
class StatsGrouped:
    """
    A custom data type that represents an average covid stat grouped by a time group represented
    by an integer.

    Representation Invariants:
        - timed_stats
        - all({i >= 0 for i in timed_stats})
    """
    timed_stats: dict[int, float]


@dataclass
class PointsXYVectors:
    """
    A custom data type that represents points, with x and y components represented in two vectors.

    Representation Invariants:
        - x
        - y
        - len(x) == len(y)
    """
    x: list[float]
    y: list[float]


@dataclass
class RegressionModelStats:
    """
    A custom data type that represents the slope, intercept, and r_sq values of a regressoin model.

    Representation Invariants:
        - 0 <= r_sq <= 1
    """
    slope: float
    intercept: float
    r_sq: float

