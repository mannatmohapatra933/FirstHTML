import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")

    # Scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Line 1 (all data)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = range(1880, 2051)
    y_pred = res.slope * x_pred + res.intercept
    plt.plot(x_pred, y_pred, 'r')

    # Line 2 (from 2000)
    df_recent = df[df['Year'] >= 2000]
    res2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred2 = range(2000, 2051)
    y_pred2 = res2.slope * x_pred2 + res2.intercept
    plt.plot(x_pred2, y_pred2, 'g')

    # Labels
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    plt.savefig('sea_level_plot.png')
    return plt.gca()