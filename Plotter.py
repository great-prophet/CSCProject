import matplotlib.pyplot as plt
import numpy as np
from DataModels import RegressionModelStats, PointsXYVectors

class Plotter:

    def __init__(self):
        plt.xlabel("Normalized cases/deaths")
        plt.ylabel("Tweet Sentiment")

    def plot_points(self, points: PointsXYVectors) -> None:
        plt.scatter(points.x, points.y)

    def plot_line(self, reg: RegressionModelStats) -> None:
        axes = plt.gca()
        x_vals = np.array(axes.get_xlim())
        y_vals = reg.intercept + reg.slope * x_vals
        plt.plot(x_vals, y_vals, '--')

    def set_r_sq(self, c_r_sq, d_r_sq):
        plt.suptitle(f"cases r squared = {c_r_sq}, deaths r squared = {d_r_sq}")

    def show(self) -> None:
        plt.show()