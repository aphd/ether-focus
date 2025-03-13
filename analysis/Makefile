# Define the Python script
PYTHON_SCRIPT=eth_block_data_analysis.plot.py

# Define the CSV file path for the data
CSV_PATH=../server/csv/main.eth.csv

# Default target
all: help

# Display available options
help:
	@echo "Usage:"
	@echo "  make plot_histogram"
	@echo "  make plot_fee_violin"
	@echo "  make plot_line_with_twin_axes"
	@echo "  make plot_fee_violin_custom_time"
	@echo "  make plot_correlation_heat_map"
	@echo ""
	@echo "Optional parameters:"
	@echo "  --start_time (e.g., 2024-12-01)"
	@echo "  --stop_time (e.g., 2025-06-13)"

# Plot Gas Price Distribution
plot_histogram:
	python $(PYTHON_SCRIPT) plot_histogram

# Plot Fee Violin (with optional start_time and stop_time)
plot_fee_violin:
	python $(PYTHON_SCRIPT) plot_fee_violin

# Plot Peer Count vs Unconfirmed Count
plot_line_with_twin_axes:
	python $(PYTHON_SCRIPT) plot_line_with_twin_axes --start_time 2024-12-01 --stop_time 2025-06-13

# Plot Correlation Heatmap
plot_correlation_heat_map:
	python $(PYTHON_SCRIPT) plot_correlation_heat_map

# Plot Fee Violin with custom time range
plot_fee_violin_custom_time:
	python $(PYTHON_SCRIPT) plot_fee_violin --start_time 2024-12-01 --stop_time 2025-06-13

plot_waiting_time_fees_correlation:
	python waiting_time_fees_correlation.plot.py "../server/csv/waiting-time-txs.csv"

plot_waiting_time_fees_correlation_histo:
	python waiting_time_fees_correlation.plot.py "../server/csv/waiting-time-txs-by-block.csv"

plot_waiting_time_and_fee_distribution:
	python waiting_time_and_fee_distribution.plot.py "../server/csv/waiting-time-txs.csv"

plot_waiting_time_and_fee_distribution_histo:
	python waiting_time_and_fee_distribution.plot.py "../server/csv/waiting-time-txs-by-block.csv"

# Clean target (optional, can be used for cleaning up temporary files, logs, etc.)
clean:
	@echo "Cleaning up temporary files (if any)."
	# Add any commands to clean temporary files here if needed.
