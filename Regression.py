import numpy as np
from sklearn.linear_model import LinearRegression
from DataModels import RegressionModelStats, PointsXYVectors


class Regression:
    
    def simple_regression(self, points: PointsXYVectors) -> RegressionModelStats:
        """

        """
        x = np.array(points.x).reshape((-1, 1))
        y = np.array(points.y)

        model = LinearRegression()
        model.fit(x, y)

        r_sq = model.score(x, y)
        slope = model.coef_[0]
        intercept = model.intercept_

        return RegressionModelStats(slope, intercept, r_sq)
