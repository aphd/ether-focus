# utils/data_processing.py
import pandas as pd

def load_data(filepath):
    """Load the Ethereum block data from the CSV file."""
    try:
        df = pd.read_csv(filepath, on_bad_lines='skip')
        df['time'] = pd.to_datetime(df['time'])
        
        # Localize time only if it is naive
        if df['time'].dt.tz is None:
            df['time'] = df['time'].dt.tz_localize('UTC')
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

def format_time_for_utc(datetime_str):
    """Convert a datetime string to UTC format."""
    dt = pd.to_datetime(datetime_str)
    return dt.strftime('%Y-%m-%dT%H:%M:%S.') + '{:06d}'.format(dt.microsecond) + 'Z'

def get_time_range(df, start_time=None, stop_time=None):
    """Return the time range with UTC conversion."""
    if df.empty:
        raise ValueError("DataFrame is empty. Please check the data file.")

    start_time = format_time_for_utc(start_time) if start_time else df['time'].min()
    stop_time = format_time_for_utc(stop_time) if stop_time else df['time'].max()
    return pd.to_datetime(start_time), pd.to_datetime(stop_time)
