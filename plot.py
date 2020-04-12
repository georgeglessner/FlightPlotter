import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import csv
import os

directory = "data"


def plotData():
    x_axis = []
    y_axis = []

    # loop files and add to x and y axis arrays
    for file in os.listdir(directory):
        if file.endswith(".csv"):
            d = os.path.splitext(file)[0]
            date = dt.datetime.strptime(d, "%Y-%m-%d").date()
            x_axis.append(date)
            with open("{}/{}".format(directory, file)) as f:
                y_axis.append(sum(1 for line in f))

    my_plotter(x_axis, y_axis)


def my_plotter(xaxis, yaxis):
    # Create bar chart with data
    plt.bar(xaxis, yaxis)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_minor_locator(mdates.DayLocator())
    plt.title("Flights")
    plt.xlabel("Date")
    plt.ylabel("# of Uniqure Flights")
    plt.savefig("FlightPlot.png")


if __name__ == "__main__":
    plotData()
