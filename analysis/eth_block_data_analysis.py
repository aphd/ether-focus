import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_data, get_time_range, parse_arguments

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

def plot_line_with_twin_axes(df, x, y1, y2, y1_label, y2_label, title):
    """Plot line graphs with two y-axes."""
    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax1.plot(df[x], df[y1], color='purple', alpha=0.5, label=y1_label, marker='o')
    ax1.set_ylabel(y1_label, color='purple')
    ax1.tick_params(axis='y', labelcolor='purple')
    
    ax2 = ax1.twinx()
    ax2.plot(df[x], df[y2], color='orange', alpha=0.5, label=y2_label, marker='o')
    ax2.set_ylabel(y2_label, color='orange')
    
    plt.title(title)
    fig.tight_layout()
    plt.show()

def plot_correlation_heat_map(df , start_time=None, stop_time=None):
    """Plot correlation heatmap of gas price columns."""
    gas_columns = ['base_fee', 'high_priority_fee', 'high_gas_price', 'peer_count', 'unconfirmed_count']
    start_time, stop_time = get_time_range(df, start_time, stop_time)
    df_filtered = df[(df['time'] >= start_time) & (df['time'] <= stop_time)]
    corr = df_filtered[gas_columns].corr()
    plt.figure(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Gas Price Correlation Heatmap')
    plt.tight_layout()
    plt.show()

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

def plot_selected_function(df, plot_type, start_time, stop_time):
    """Call the selected plot function based on the `plot_type` parameter."""
    plot_functions = {
        'plot_gas_price_distribution': lambda: plot_histogram(df, 
            ['high_gas_price', 'medium_gas_price', 'low_gas_price'], 
            ['r', 'g', 'b'], ['High', 'Medium', 'Low'], 'Distribution of Gas Prices'),
        'plot_peer_vs_unconfirmed': lambda: plot_line_with_twin_axes(df[(df['time'] >= start_time) & (df['time'] <= stop_time)],
            'time', 'peer_count', 'unconfirmed_count', 'Peer Count', 'Unconfirmed Count', 
            'Peer Count vs Unconfirmed Count Over Time'),
        'plot_correlation_heat_map': lambda: plot_correlation_heat_map(df, start_time, stop_time),
        'plot_fee_violin': lambda: plot_fee_violin(df, start_time, stop_time)
    }
    plot_functions.get(plot_type, lambda: print(f"Error: Plot type '{plot_type}' not found."))()

def main():
    args = parse_arguments()
    
    # Load the data
    filepath = "../server/csv/main.eth.csv"
    df = load_data(filepath)
    
    # Check if DataFrame is empty
    if df.empty:
        print("No data available for plotting.")
        return
    
    # Get the start and stop time
    start_time, stop_time = get_time_range(df, args.start_time, args.stop_time)
    
    # Call the plot function based on the CLI arguments
    plot_selected_function(df, args.plot_type, start_time, stop_time)

if __name__ == '__main__':
    main()