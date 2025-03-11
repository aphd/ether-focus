import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def read_csv(file_path):
    """Read CSV file into a DataFrame."""
    return pd.read_csv(file_path)

def convert_to_datetime(df):
    """Convert columns to datetime format."""
    df['received'] = pd.to_datetime(df['received'])
    df['received_origin'] = pd.to_datetime(df['received_origin'])
    df['confirmed'] = pd.to_datetime(df['confirmed'])
    return df

def calculate_time_difference(df):
    """Calculate the time differences in seconds."""
    df['confirmed_received'] = (df['confirmed'] - df['received']).dt.total_seconds()
    df['confirmed_received_origin'] = (df['confirmed'] - df['received_origin']).dt.total_seconds()
    return df

def plot_violin(data, column, title, subplot_position, bw=0.2, width=0.8):
    """Generate a violin plot for a specified column with a box plot inside and individual points."""
    plt.subplot(1, 2, subplot_position)
    
    # Create the violin plot
    sns.violinplot(data=data, y=column, inner=None, bw=bw, width=width)
    
    # Overlay a larger box plot
    sns.boxplot(data=data, y=column, width=0.2, color='white', fliersize=5, linewidth=2)
    
    # Overlay a strip plot for individual points
    sns.stripplot(data=data, y=column, color='black', size=5, alpha=0.6)
    
    plt.title(title)
    plt.ylabel("Time difference (seconds)")

def main():
    """Main function to execute the full process."""
    file_path = "../server/csv/waiting-time-txs.csv"
    df = read_csv(file_path)
    df = convert_to_datetime(df)
    df = calculate_time_difference(df)

    plt.figure(figsize=(12, 6))
    
    plot_violin(df, 'confirmed_received', "Violin plot: confirmed - received (in seconds)", 1, bw=0.5, width=0.8)
    plot_violin(df, 'confirmed_received_origin', "Violin plot: confirmed - received_origin (in seconds)", 2, bw=0.5, width=0.8)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()