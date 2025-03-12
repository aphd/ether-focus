import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def read_csv(file_path):
    """Read CSV file into a DataFrame."""
    return pd.read_csv(file_path)

def convert_to_datetime(df):
    """Convert specified columns to datetime format."""
    for col in ['received', 'received_origin', 'confirmed']:
        df[col] = pd.to_datetime(df[col])
    return df

def calculate_time_difference(df):
    """Calculate time differences in seconds."""
    df['confirmed_received'] = (df['confirmed'] - df['received']).dt.total_seconds()
    df['confirmed_received_origin'] = (df['confirmed'] - df['received_origin']).dt.total_seconds()
    return df

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
    sns.scatterplot(data=data, x='gas_fee_cap', y='confirmed_received', color='green', alpha=0.6)
    plt.title('Confirmed Received vs Gas Fee Cap')
    plt.xlabel('Gas Fee Cap (GWei)')
    plt.ylabel('Confirmed - Received (seconds)')

    plt.tight_layout()
    plt.show()

def main():
    """Main function to execute the full process."""
    file_path = "../server/csv/waiting-time-txs.csv"
    df = read_csv(file_path)
    df = convert_to_datetime(df)
    df = calculate_time_difference(df)

    plot_scatter(df)

if __name__ == "__main__":
    main()