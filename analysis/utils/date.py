import pandas as pd

def convert_to_datetime(df):
    """Convert specified columns to datetime format."""
    for col in ['received', 'received_origin', 'confirmed']:
        df[col] = pd.to_datetime(df[col], errors='coerce')  # Coerce errors
    return df

def calculate_time_difference(df):
    """Calculate time differences in seconds."""
    df['confirmed_received'] = (df['confirmed'] - df['received']).dt.total_seconds()
    df['confirmed_received_origin'] = (df['confirmed'] - df['received_origin']).dt.total_seconds()
    return df

def read_csv(file_path):
    """Read CSV file into a DataFrame."""
    return pd.read_csv(file_path)