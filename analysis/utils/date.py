import pandas as pd

def convert_to_datetime(df):
    """Convert specified columns to datetime format, truncating to ignore milliseconds."""
    for col in ['received', 'confirmed']:
        # Truncate the string to the first 19 characters (ignoring milliseconds)
        df[col] = df[col].str[:19]
        # Convert to datetime
        df[col] = pd.to_datetime(df[col], format='%Y-%m-%dT%H:%M:%S', errors='coerce')
    return df

def calculate_time_difference(df):
    """Calculate time differences in seconds."""
    df['confirmed_received'] = (df['confirmed'] - df['received']).dt.total_seconds()
    return df

def read_csv(file_path):
    """Read CSV file into a DataFrame."""
    return pd.read_csv(file_path)