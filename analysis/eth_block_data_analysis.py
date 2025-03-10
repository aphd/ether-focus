
from utils import load_data, get_time_range, parse_arguments
from plots import plot_fee_violin, plot_histogram, plot_line_with_twin_axes, plot_correlation_heat_map

def plot_selected_function(df, plot_type, start_time, stop_time):
    """Call the selected plot function based on the `plot_type` parameter."""
    plot_functions = {
        'plot_histogram': lambda: plot_histogram(df, 
            ['high_gas_price', 'medium_gas_price', 'low_gas_price'], 
            ['r', 'g', 'b'], ['High', 'Medium', 'Low'], 'Distribution of Gas Prices'),
        'plot_line_with_twin_axes': lambda: plot_line_with_twin_axes(df[(df['time'] >= start_time) & (df['time'] <= stop_time)],
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
    # Get the start and stop time
    start_time, stop_time = get_time_range(df, args.start_time, args.stop_time)
    # Call the plot function based on the CLI arguments
    plot_selected_function(df, args.plot_type, start_time, stop_time)

if __name__ == '__main__':
    main()