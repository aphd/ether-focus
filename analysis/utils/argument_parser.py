# utils/argument_parser.py
import argparse

def parse_arguments():
    """Parse the command-line arguments."""
    parser = argparse.ArgumentParser(description="Plot Ethereum block data.")
    parser.add_argument('plot_type', type=str, help="The plot function to call.")
    parser.add_argument('--start_time', type=str, help="Start time for time-based plots.")
    parser.add_argument('--stop_time', type=str, help="Stop time for time-based plots.")
    return parser.parse_args()
