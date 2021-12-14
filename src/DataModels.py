from dataclasses import dataclass
from datetime import date

@dataclass
class TweetsRaw:
    """
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
    Representation Invariants:
        - times
        - tweets
        - len(times) == len(tweets)
    """
    times: list[int]
    stats: list[float]


@dataclass
class StatsGrouped:
    timed_stats: dict[int, float]


@dataclass
class PointsXYVectors:
    x: list[float]
    y: list[float]

@dataclass
class RegressionModelStats:
    slope: float
    intercept: float
    r_sq: float

