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

def plot_violin(data, column, ylabel,  subplot_position, color, bw=0.2, width=0.8):
    """Generate a violin plot for a specified column."""
    plt.subplot(1, 3, subplot_position)  # Change to 1x3 layout
    sns.violinplot(data=data, y=column, inner=None, bw_method=bw, width=width, color=color)  # Use bw_method
    sns.boxplot(data=data, y=column, width=0.2, color='white', fliersize=5, linewidth=2)
    sns.stripplot(data=data, y=column, color='black', size=5, alpha=0.6)
    plt.ylabel(ylabel)

def main():
    """Main function to execute the full process."""
    file_path = "../server/csv/waiting-time-txs.csv"
    df = read_csv(file_path)
    df = convert_to_datetime(df)
    df = calculate_time_difference(df)

    plt.figure(figsize=(15, 6))  # Adjust figure size to accommodate 3 plots

    plot_violin(df, 'confirmed_received', "confirmed - received (in seconds)", 1, color='blue')
    plot_violin(df, 'confirmed_received_origin', "confirmed - received_origin (in seconds)", 2, color='orange')
    plot_violin(df, 'gas_tip_cap', "Gas tip cap (GWei)", 3, color='green')  # New plot for gas_tip_cap

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()