import matplotlib.pyplot as plt
import numpy as np


class Plotter:
    """
    A system that creates a graph plotting normalized cases and deaths against tweet sentiment.
    """

    def __init__(self) -> None:
        plt.xlabel("Normalized cases/deaths")
        plt.ylabel("Tweet Sentiment")

    def plot_points(self, x: float, y: float) -> None:
        """
        Plots the relevant points on a graph
        """
        plt.scatter(x, y)

    def plot_line(self, slope: float, intercept: float) -> None:
        """
        Plots a line of best fit using the points from the plot_points graph.
        """
        axes = plt.gca()
        x_vals = np.array(axes.get_xlim())
        y_vals = intercept + slope * x_vals
        plt.plot(x_vals, y_vals, '--')

    def set_r_sq(self, c_r_sq, d_r_sq) -> None:
        """
        Adds a subtitle to the graph containing the cases and deaths r squared.
        """
        plt.suptitle(f"cases r squared = {c_r_sq}, deaths r squared = {d_r_sq}")

    def show(self) -> None:
        """
        Shows the graph.
        """
        plt.show()
