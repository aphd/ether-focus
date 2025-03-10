import matplotlib.pyplot as plt
import seaborn as sns
from utils import get_time_range

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