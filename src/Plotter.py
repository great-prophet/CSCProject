import matplotlib.pyplot as plt
import numpy as np
from src.DataModels import RegressionModelStats, PointsXYVectors


class Plotter:
    """
    A system that creates a graph plotting normalized cases and deaths against tweet sentiment.
    """

    def __init__(self) -> None:
        plt.xlabel("Normalized Cases/Deaths", fontsize=30)
        plt.ylabel("Average Weekly Sentiment on Twitter", fontsize=30)
        plt.xticks(fontsize=25)
        plt.yticks(fontsize=25)


    def plot_points(self, points: PointsXYVectors) -> None:
        """
        Plots the relevant points on a graph
        """
        plt.scatter(points.x, points.y)

    def plot_line(self, reg: RegressionModelStats) -> None:
        """
        Plots a line of best fit using the points from the plot_points graph.
        """

        axes = plt.gca()
        x_vals = np.array(axes.get_xlim())
        y_vals = reg.intercept + reg.slope * x_vals
        plt.plot(x_vals, y_vals, '--')

    def set_reg_test(self, c_reg: RegressionModelStats, d_reg: RegressionModelStats) -> None:
        """
        Adds a subtitle to the graph containing the cases and deaths r squared.
        """
        plt.title("Normalized Cases/Deaths Versus Average Weekly Sentiment on Twitter", fontsize=30, y=1.02)
        plt.suptitle(f"Cases (Orange): y = {c_reg.slope:.3f}x + {c_reg.intercept:.3f}, $R^2$ = {c_reg.r_sq:.3f} \n Deaths (Blue): y = {d_reg.slope:.3f}x + {d_reg.intercept:.3f}, $R^2$ = {d_reg.r_sq:.3f}", y=0.865, x=0.72, fontsize=25)


    def show(self) -> None:
        """
        Shows the graph.
        """
        plt.show()
