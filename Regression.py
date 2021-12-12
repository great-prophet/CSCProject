import numpy as np
from sklearn.linear_model import LinearRegression


class Regression:
    """
    A system that creates a simple linear regression model.
    """
    def simple_regression(self, x_raw: list[int], y_raw: list[int]) -> (float, float, float):
        """Return a tuple with the regression line slope, intercept, and
           coefficient of determination for the data.

        """
        x = np.array(x_raw).reshape((-1, 1))
        y = np.array(y_raw)

        model = LinearRegression()
        model.fit(x, y)

        r_sq = model.score(x, y)
        slope = model.coef_[0]
        intercept = model.intercept_

        return (slope, intercept, r_sq)
