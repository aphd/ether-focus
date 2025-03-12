import matplotlib.pyplot as plt
import seaborn as sns
from utils.date import convert_to_datetime, calculate_time_difference
from utils.data_processing import read_csv

def plot_violin(data, column, ylabel, subplot_position, color, bw=0.2, width=0.8):
    """Generate a violin plot for a specified column."""
    plt.subplot(1, 2, subplot_position)  # Change to 1x2 layout to make space
    sns.violinplot(data=data, y=column, inner=None, bw_method=bw, width=width, color=color)
    sns.boxplot(data=data, y=column, width=0.15, color='white', fliersize=0, linewidth=2)  # Smaller width for boxplot
    sns.stripplot(data=data, y=column, color='black', size=3, alpha=0.6, jitter=True)  # Enable jitter for better spread
    plt.ylabel(ylabel)

def main():
    """Main function to execute the full process."""
    file_path = "../server/csv/waiting-time-txs.csv"
    df = read_csv(file_path)
    df = convert_to_datetime(df)
    df = calculate_time_difference(df)

    plt.figure(figsize=(15, 6))  # Adjust figure size to accommodate 2 plots

    plot_violin(df, 'confirmed_received', "confirmed - received (in seconds)", 1, color='blue')
    plot_violin(df, 'gas_tip_cap', "Gas tip cap (GWei)", 2, color='green')  # New plot for gas_tip_cap

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()