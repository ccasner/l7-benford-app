import base64
import io
import os
from flask import Flask, render_template, request, Response
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

plt.ioff
matplotlib.use('MacOSX')
matplotlib.interactive(False)


class CreateGraph:
    def __init__(self, data, column):
        self.data = data
        self.column = column
        self.actual = None
        self.expected = None

    def process_data(self):
        print(self.data)

        list_of_firsts = []
        for num in self.data[self.column].values:
            # convert num to str to get first digit, return as int
            first_num = int(str(num)[0])
            # add digits to list of all firsts
            list_of_firsts.append(first_num)

        # convert list to pandas series
        sr_actual = pd.Series(list_of_firsts).value_counts()[:9]

        actual_results = sr_actual.to_dict()
        
        print('ACTUAL: ', actual_results)
        self.actual = actual_results

        benford_percentages = [.301, .176, .125, .097, .079, .067, .058, .051, .046]
        # print('BEFORE: ', benford_percentages)
        benford_results = [(i * self.data.size).round() for i in benford_percentages]
        # print('AFTER: ', benford_results)

        print('EXPECTED: ', benford_results)
        self.expected = benford_results


    def create_graph_image(self):
        benford = self.get_expected_counts()
        actual = self.get_actual_counts().to_numpy()

        digits = (1,2,3,4,5,6,7,8,9)
        plotdata = {
            "Benford": benford,
            "Actual": actual
        }

        x = np.arange(len(benford))  # the label locations
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

        fig.savefig('app/static/images/new_plot.png', dpi=200)


    # Returns pandas series containing actual counts for each leading digit
    def get_actual_counts(self):

        col_to_sort = '7_2009'

        df = self.data

        list_of_firsts = []
        for num in df[col_to_sort].values:
            # convert num to str to get first digit, return as int
            first_num = int(str(num)[0])
            # add digits to list of all firsts
            list_of_firsts.append(first_num)

        # convert list to pandas series
        sr = pd.Series(list_of_firsts)
        # Print the series
        print(sr)
        # Print the value counts for each digit in the series
        print(sr.value_counts())
        sr_counts = sr.value_counts()[:9]
        # data = sr_counts.to_frame()

        data = sr.value_counts()[:9]

        return data


    # Returns array of expected counts based on Benford's law 
    def get_expected_counts(self):

        col_to_sort = '7_2009'

        df = self.data

        benford_percentages = [.301, .176, .125, .097, .079, .067, .058, .051, .046]
        print('BEFORE: ', benford_percentages)
        benford_results = [(i * df.size).round() for i in benford_percentages]
        print('AFTER: ', benford_results)

        return benford_results


# Create bar graph comparing results 
# benford = get_expected_counts()
# actual = get_actual_counts().to_numpy()

# plotdata = pd.DataFrame({

#     "Benford": benford,

#     "Actual": actual})

# plotdata.plot(
#     kind="bar",
#     figsize=(15, 8),
#     title = "Benford's Law vs. Actual Counts",
#     xlabel = "Leading Digit",
#     ylabel = "Total Count"
#     )


# plt.plot(data=plotdata)
# plt.savefig('app/static/images/new_plot.png')
# # plt.show()


# benford = get_expected_counts()
# actual = get_actual_counts().to_numpy()

# digits = (1,2,3,4,5,6,7,8,9)
# plotdata = {
#     "Benford": benford,
#     "Actual": actual
# }

# x = np.arange(len(benford))  # the label locations
# width = 0.3  # the width of the bars
# multiplier = 0

# fig, ax = plt.subplots(figsize=(15, 8))

# for attribute, measurement in plotdata.items():
#     offset = width * multiplier
#     rects = ax.bar(x + offset, measurement, width, label=attribute)
#     ax.bar_label(rects, padding=3)
#     multiplier += 1

# ax.set_xlabel("Leading Digit")
# ax.set_ylabel("Total Count")
# ax.set_title("Benford's Law vs. Actual Counts")
# ax.set_xticks(x + 0.15, digits)
# ax.legend(loc='upper right', ncols=3)

# fig.savefig('app/static/images/new_plot.png', dpi=200)

# plt.show()
