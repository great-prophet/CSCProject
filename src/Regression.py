import numpy as np
from sklearn.linear_model import LinearRegression
from src.DataModels import RegressionModelStats, PointsXYVectors


class Regression:

    """
    A system that creates a simple linear regression model.
    """
    def simple_regression(self, points: PointsXYVectors) -> RegressionModelStats:
        """Return a RegressionModelStats object containing the result of a
        simple linear regression on the given points.
        """
        x = np.array(points.x).reshape((-1, 1))
        y = np.array(points.y)

        model = LinearRegression()
        model.fit(x, y)

        r_sq = model.score(x, y)
        slope = model.coef_[0]
        intercept = model.intercept_

        return RegressionModelStats(slope, intercept, r_sq)
