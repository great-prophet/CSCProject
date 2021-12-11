import matplotlib.pyplot as plt
import numpy as np

class Plotter:

    def __init__(self):
        plt.xlabel("Normalized cases/deaths")
        plt.ylabel("Tweet Sentiment")

    def plot_points(self, x: float, y: float) -> None:
        plt.scatter(x, y)

    def plot_line(self, slope: float, intercept: float) -> None:
        axes = plt.gca()
        x_vals = np.array(axes.get_xlim())
        y_vals = intercept + slope * x_vals
        plt.plot(x_vals, y_vals, '--')

    def set_r_sq(self, c_r_sq, d_r_sq):
        plt.suptitle(f"cases r squared = {c_r_sq}, deaths r squared = {d_r_sq}")

    def show(self) -> None:
        plt.show()