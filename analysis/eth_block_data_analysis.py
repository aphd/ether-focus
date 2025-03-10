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

def plot_peer_vs_unconfirmed(df, start_time, stop_time):
    """Plot peer count vs unconfirmed count with two y-axes based on time."""
    
    # Convert the time field to datetime in UTC
    df['time'] = pd.to_datetime(df['time']).dt.tz_convert('UTC')
    
    # Convert start_time and stop_time to datetime in UTC
    start_time = pd.to_datetime(start_time).tz_localize('UTC')
    stop_time = pd.to_datetime(stop_time).tz_localize('UTC')

    # Filter the DataFrame based on the provided time range
    df_filtered = df[(df['time'] >= start_time) & (df['time'] <= stop_time)]

    fig, ax1 = plt.subplots(figsize=(10, 6))

    # First plot for peer count
    ax1.plot(df_filtered['time'], df_filtered['peer_count'], color='purple', alpha=0.5, label='Peer Count', marker='o')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Peer Count', color='purple')
    ax1.tick_params(axis='y', labelcolor='purple')
    ax1.grid(True)

    # Create a second y-axis for unconfirmed count
    ax2 = ax1.twinx()
    ax2.plot(df_filtered['time'], df_filtered['unconfirmed_count'], color='orange', alpha=0.5, label='Unconfirmed Count', marker='o')
    ax2.set_ylabel('Unconfirmed Count', color='orange')
    ax2.tick_params(axis='y', labelcolor='orange')

    # Set title and layout
    plt.title('Peer Count vs Unconfirmed Count Over Time')
    fig.tight_layout()
    plt.show()

def plot_correlation_heat_map(df):
    """Plot correlation heatmap of gas price columns."""
    gas_columns = ['base_fee', 'high_priority_fee', 'high_gas_price', 'peer_count', 'unconfirmed_count']
    corr = df[gas_columns].corr()
    plt.figure(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Gas Price Correlation Heatmap')
    plt.tight_layout()
    plt.show()

def plot_fee_violin(df):
    # List of keys to display in the violin plot
    # columns_to_plot = ['high_gas_price', 'medium_gas_price', 'low_gas_price', 'high_priority_fee', 'medium_priority_fee', 'low_priority_fee', 'base_fee']
    columns_to_plot = ['high_priority_fee', 'medium_priority_fee', 'low_priority_fee']
    
    # Filter the DataFrame to include only the columns of interest
    df_filtered = df[columns_to_plot]
    
    # Set the size of the figure
    plt.figure(figsize=(12, 8))
    
    # Create the violin plots for the filtered data
    sns.violinplot(data=df_filtered)
    
    plt.title('Violin Plots for Gas Prices and Priority Fees')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    
    plt.tight_layout()
    plt.show()



def main():
    """Main function to load data and generate plots."""
    filepath = "../server/csv/main.eth.csv"
    df = load_data(filepath)
    
    # plot_gas_price_distribution(df)
    # plot_peer_vs_unconfirmed(df, '2024-12-01', '2025-06-13')
    # plot_correlation_heat_map(df)
    plot_fee_violin(df)

if __name__ == '__main__':
    main()
