import matplotlib.pyplot as plt
import seaborn as sns
import argparse
from utils.date import convert_to_datetime, calculate_time_difference
from utils.data_processing import read_csv

def plot_scatter(data):
    """Generate scatter plots for confirmed_received against gas_tip_cap and gas_fee_cap."""
    plt.figure(figsize=(12, 6))

    # Subplot for confirmed_received vs gas_tip_cap
    plt.subplot(1, 2, 1)
    sns.scatterplot(data=data, x='gas_tip_cap', y='confirmed_received', color='blue', alpha=0.6)
    plt.title('Confirmed Received vs Gas Tip Cap')
    plt.xlabel('Gas Tip Cap (GWei)')
    plt.ylabel('Confirmed - Received (seconds)')

    # Subplot for confirmed_received vs gas_fee_cap
    plt.subplot(1, 2, 2)
    sns.scatterplot(data=data, x='gas_price', y='confirmed_received', color='green', alpha=0.6)
    plt.title('Confirmed Received vs Gas Price')
    plt.xlabel('Gas Price (GWei)')
    plt.ylabel('Confirmed - Received (seconds)')

    plt.tight_layout()
    plt.show()

def main():
    """Main function to execute the full process."""
    parser = argparse.ArgumentParser(description='Plot gas tips and fees from a CSV file.')
    parser.add_argument('file_path', type=str, help='Path to the CSV file')
    args = parser.parse_args()

    df = read_csv(args.file_path)
    df = convert_to_datetime(df)
    df = calculate_time_difference(df)

    plot_scatter(df)

if __name__ == "__main__":
    main()