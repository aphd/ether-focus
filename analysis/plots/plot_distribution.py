import matplotlib.pyplot as plt
import seaborn as sns
from utils import get_time_range

def plot_fee_violin(df, start_time=None, stop_time=None):
    """Display violin plots for different datasets on the same canvas."""
    start_time, stop_time = get_time_range(df, start_time, stop_time)
    df_filtered = df[(df['time'] >= start_time) & (df['time'] <= stop_time)]
    sns.violinplot(data=df_filtered[['high_priority_fee', 'medium_priority_fee', 'low_priority_fee']])
    plt.title('Violin Plots for Gas Prices and Priority Fees')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.tight_layout()
    plt.show()
    
def plot_histogram(df, columns, colors, labels, title):
    """Plot histograms for specified columns."""
    plt.figure(figsize=(10, 6))
    for col, color, label in zip(columns, colors, labels):
        plt.hist(df[col], bins=50, alpha=0.7, label=label, color=color)
    plt.xlabel('Gas Price')
    plt.ylabel('Frequency')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()