import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

matplotlib.use('Agg')

class CreateGraph:
    def __init__(self, data, column):
        self.data = data
        self.column = column
        self.actual_results = None
        self.expected_results = None


    def process_data(self):

        list_of_firsts = []
        for num in self.data[self.column].values:
            # convert num to str to get first digit, return as int
            first_num = int(str(num)[0])
            # add digits to list of all firsts
            list_of_firsts.append(first_num)

        # convert list to pandas series
        actual_counts = pd.Series(list_of_firsts).value_counts()[:9]
        self.actual_results = actual_counts

        benford_percentages = [.301, .176, .125, .097, .079, .067, .058, .051, .046]
        benford_results = [(i * self.data.size).round() for i in benford_percentages]
        self.expected_results = benford_results

        self.create_graph_image()


    def create_graph_image(self):

        digits = (1,2,3,4,5,6,7,8,9)
        plotdata = {
            "Benford": self.expected_results,
            "Actual": self.actual_results
        }

        x = np.arange(len(self.expected_results))  # the label locations
        width = 0.3  # the width of the bars
        multiplier = 0

        fig, ax = plt.subplots(figsize=(15, 8))

        for attribute, measurement in plotdata.items():
            offset = width * multiplier
            rects = ax.bar(x + offset, measurement, width, label=attribute)
            ax.bar_label(rects, padding=3)
            multiplier += 1

        ax.set_xlabel("Leading Digit")
        ax.set_ylabel("Total Count")
        ax.set_title("Benford's Law vs. Actual Counts")
        ax.set_xticks(x + 0.15, digits)
        ax.legend(loc='upper right', ncols=3)

        fig.savefig('app/static/images/plot.png', dpi=200)

