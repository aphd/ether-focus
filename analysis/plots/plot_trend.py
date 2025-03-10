import matplotlib.pyplot as plt

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