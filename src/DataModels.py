from dataclasses import dataclass
from datetime import date

@dataclass
class TweetsRaw:
    times: list[date]
    tweets: list[str]


@dataclass
class CovidStatsRaw:
    times: list[date]
    stats: list[int]


@dataclass
class StatsNormed:
    times: list[date]
    stats: list[float]


@dataclass
class StatsDatesNormed:
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

