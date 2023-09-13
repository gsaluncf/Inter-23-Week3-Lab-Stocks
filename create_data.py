import pandas as pd
import numpy as np

# Generate sample data
np.random.seed(0)  # Set a seed for reproducibility
date_range = pd.date_range(start='2022-01-01', end='2023-05-31', freq='B')  # Business days
num_days = len(date_range)
closing_prices = np.random.normal(100, 5, num_days)  # Mean price 100, Std. Deviation 5
volume = np.random.randint(100000, 500000, num_days)  # Random volume values

# Create a DataFrame
data = pd.DataFrame({
    'Date': date_range,
    'Close': closing_prices,
    'Volume': volume
})

# Save the DataFrame to a CSV file
data.to_csv('stock_data.csv', index=False)

print("Sample stock data has been created and saved to 'stock_data.csv'.")
