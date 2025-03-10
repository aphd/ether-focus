# Define the Python script
PYTHON_SCRIPT=eth_block_data_analysis.py

# Define the CSV file path for the data
CSV_PATH=../server/csv/main.eth.csv

# Default target
all: help

# Display available options
help:
	@echo "Usage:"
	@echo "  make plot_gas_price_distribution"
	@echo "  make plot_peer_vs_unconfirmed"
	@echo "  make plot_correlation_heat_map"
	@echo "  make plot_fee_violin"
	@echo ""
	@echo "Optional parameters:"
	@echo "  --start_time (e.g., 2024-12-01)"
	@echo "  --stop_time (e.g., 2025-06-13)"

# Plot Gas Price Distribution
plot_gas_price_distribution:
	python $(PYTHON_SCRIPT) plot_gas_price_distribution

# Plot Peer Count vs Unconfirmed Count
plot_peer_vs_unconfirmed:
	python $(PYTHON_SCRIPT) plot_peer_vs_unconfirmed --start_time 2024-12-01 --stop_time 2025-06-13

# Plot Correlation Heatmap
plot_correlation_heat_map:
	python $(PYTHON_SCRIPT) plot_correlation_heat_map

# Plot Fee Violin (with optional start_time and stop_time)
plot_fee_violin:
	python $(PYTHON_SCRIPT) plot_fee_violin

# Plot Fee Violin with custom time range
plot_fee_violin_custom_time:
	python $(PYTHON_SCRIPT) plot_fee_violin --start_time 2024-12-01 --stop_time 2025-06-13

# Clean target (optional, can be used for cleaning up temporary files, logs, etc.)
clean:
	@echo "Cleaning up temporary files (if any)."
	# Add any commands to clean temporary files here if needed.
