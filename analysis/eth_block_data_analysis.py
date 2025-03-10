import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filepath):
    """Load the Ethereum block data from the CSV file."""
    try:
        df = pd.read_csv(filepath, on_bad_lines='skip')  # Adjust as necessary
        df['time'] = pd.to_datetime(df['time'])
        return df
    except Exception as e:
        print(f"Error loading data: {e}")

def plot_block_height_vs_time(df):
    """Plot block height over time."""
    plt.figure(figsize=(10, 6))
    plt.plot(df['time'], df['height'], label='Block Height', color='b')
    plt.xlabel('Time')
    plt.ylabel('Block Height')
    plt.title('Ethereum Block Height Over Time')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_gas_price_distribution(df):
    """Plot distribution of gas prices."""
    plt.figure(figsize=(10, 6))
    plt.hist(df['high_gas_price'], bins=50, alpha=0.7, label='High Gas Price', color='r')
    plt.hist(df['medium_gas_price'], bins=50, alpha=0.7, label='Medium Gas Price', color='g')
    plt.hist(df['low_gas_price'], bins=50, alpha=0.7, label='Low Gas Price', color='b')
    plt.xlabel('Gas Price')
    plt.ylabel('Frequency')
    plt.title('Distribution of Gas Prices')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_peer_vs_unconfirmed(df):
    """Plot peer count vs unconfirmed count."""
    plt.figure(figsize=(10, 6))
    plt.scatter(df['peer_count'], df['unconfirmed_count'], color='purple', alpha=0.5)
    plt.xlabel('Peer Count')
    plt.ylabel('Unconfirmed Count')
    plt.title('Peer Count vs Unconfirmed Count')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_gas_price_correlation(df):
    """Plot correlation heatmap of gas price columns."""
    gas_columns = ['base_fee', 'high_priority_fee', 'high_gas_price', 'peer_count', 'unconfirmed_count']
    corr = df[gas_columns].corr()
    plt.figure(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Gas Price Correlation Heatmap')
    plt.tight_layout()
    plt.show()

def plot_fee_correlation(df):
    """Plot correlation between base fee and priority fees."""
    plt.figure(figsize=(10, 6))
    plt.scatter(df['base_fee'], df['high_priority_fee'], color='orange', alpha=0.5)
    plt.xlabel('Base Fee')
    plt.ylabel('High Priority Fee')
    plt.title('Base Fee vs High Priority Fee')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    """Main function to load data and generate plots."""
    filepath = "../server/csv/main.eth.csv"
    df = load_data(filepath)
    
    # plot_block_height_vs_time(df)
    # plot_gas_price_distribution(df)
    # plot_peer_vs_unconfirmed(df)
    plot_gas_price_correlation(df)
    # plot_fee_correlation(df)

if __name__ == '__main__':
    main()
