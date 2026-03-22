import pandas as pd

df = pd.read_csv("fcc-forum-pageviews.csv")

# Convert date column
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Remove top & bottom 2.5%
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

import matplotlib.pyplot as plt

def draw_line_plot():
    fig, ax = plt.subplots(figsize=(12,6))
    
    ax.plot(df.index, df['value'], color='red')
    
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    df_bar = df.copy()
    
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.strftime('%B')
    
    df_group = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    fig = df_group.plot(kind='bar', figsize=(10,8)).figure
    
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")
    
    fig.savefig('bar_plot.png')
    return fig