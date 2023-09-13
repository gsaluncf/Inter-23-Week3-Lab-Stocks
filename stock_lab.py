import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# Load the stock market data into a DataFrame
def load_data(file_path):
    # Load the data from the CSV file and return it as a DataFrame. We will use Pandas for this

    return pd.read_csv(file_path)


# Calculate and display basic statistics
def basic_statistics(data):
    print("Basic Statistics:")
    print("Mean:", data['Close'].mean())
    #TODO: The standard deviation is a measure of how spread out the data is. It is the square root of the variance.
    #Panda's DataFrame has a built-in function for calculating the standard deviation. Use it to calculate the standard deviation of the closing prices and print it.
    std = 0  # <-- Replace this with the standard deviation of the closing prices
    print("Standard Deviation:", std)
    #TODO: Panada's DataFrame also has a built-in function for calculating the median. Use it to calculate the median of the closing prices and print it.
    median = 0  # <-- Replace this with the standard deviation of the closing prices
    print("Median:", median)


# Create a line chart to visualize the stock price trend over time
def visualize_trend(data):
    plt.figure(figsize=(10, 5)) # <-- This sets the size of the figure
    plt.plot(data['Date'], data['Close'], label='Closing Price') # <-- This plots the closing price
    #plt.   # <-- TODO: Sets the label for the x-axis to date
    #plt. <-- TODO: Sets the label for the y-axis to Price
    plt.title('Stock Price Trend Over Time')
    plt.xticks(rotation=45) # <-- This rotates the x-axis labels by 45 degrees
    plt.legend()        # <-- This displays the legend
    #plt.         # TODO: Displays the figure

# Identify and display the date with the highest and lowest closing prices
def extreme_values(data):
    max_date = data.loc[data['Close'].idxmax()]['Date'] # <-- This gets the date of the highest closing price
    max_price = 0  # <-- Todo:  get the highest closing price
    min_date = "12-12-00" # <-- Todo: This gets the date of the lowest closing price
    min_price = data['Close'].min() # <-- Todo: get the lowest closing price

    print("Date with Highest Closing Price:", max_date, "Price:", max_price)
    print("Date with Lowest Closing Price:", min_date, "Price:", min_price)

# Calculate and display the average trading volume over a specified time period
def average_volume(data, start_date, end_date):
    filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)] # <-- This filters the data to only include the dates between start_date and end_date
    avg_volume = filtered_data['Volume'].mean() # <-- This calculates the average volume
    print(f"Average Trading Volume between") # <-- Todo prints the average volume and formats it to 2 decimal places as well as printing the start and end dates

# Find and display the top N days with the highest trading volume
def top_volume_days(data, n):
    top_days = data.nlargest(n, 'Volume')
    print(f"Top {n} Days with the Highest Trading Volume:")
    print(top_days[['Date', 'Volume']])

# Calculate and display the daily percentage change in stock prices
def daily_percentage_change(data):
    data['Daily Percentage Change'] = data['Close'].pct_change() * 100
    print("Daily Percentage Change:")
    print(data[['Date', 'Daily Percentage Change']])

# ... (previous functions for basic analysis)

# Monte Carlo Simulation for Predicting Future Stock Prices
# This is specificly hard. Give it a shot!
def monte_carlo_simulation(data, num_simulations, num_days):
    returns = data['Close'].pct_change() # Returns are the percentage change in price from one day to the next. Basiclly how much you made or lost in a day as a percentage
    mean_return = returns.mean() # The mean return is the average return over the time period. This is the expected return because its the average of the returns
    std_dev = returns.std() # The standard deviation is a measure of how spread out the data is. So, how much or how often and wildly the returns vary from the mean return
    initial_price = data['Close'].iloc[-1] # The initial price is the last closing price in the data set. This is the price we will start with for the simulation

    simulation_df = pd.DataFrame() # This creates an empty DataFrame that we will use to store the simulated prices

    for i in range(num_simulations):
        #TODO: Use numpy's random.normal function to generate a list of daily returns. The list should have:
        # The mean return
        # standard deviation
        # and the number of days
        #daily_returns = np # <-- Replace this with the correct function call
        #once done, comment out the following line
        daily_returns = np.arange(1, 101)
        #did you comment the above out once you figured out how to calc
        price_series = [initial_price]

        for j in range(num_days): # This loops through the number of days we want to simulate
            price_series.append(price_series[-1] * (1 + daily_returns[j])) # This calculates the price for the next day and appends it to the price_series list

        simulation_df[f"Simulation {i+1}"] = price_series   # This adds the simulated prices to the DataFrame

    plt.figure(figsize=(10, 5)) # <-- This sets the size of the figure
    for i in range(num_simulations): # This loops through the number of simulations
        plt.plot(simulation_df.index, simulation_df[f"Simulation {i+1}"], lw=1, alpha=0.7) # This plots the simulated prices

    #plt. # <-- Todo  sets the label for the x-axis to date
    #plt# <-- Todo  sets the label for the y-axis to Price
    plt.title(f'Monte Carlo Simulation for {num_simulations} Simulations')
    # plt # <-- Todo  display the figure

def main():
    # Load data from a CSV file
    data = load_data('stock_data.csv')

    # Analysis 1: Basic Statistics
    basic_statistics(data)

    # Analysis 2: Visualize Stock Price Trend
    visualize_trend(data)

    # Analysis 3: Identify Extreme Values
    extreme_values(data)

    # Analysis 4: Average Trading Volume
    average_volume(data, '2023-01-01', '2023-12-31')

    # Analysis 5: Top N Days with Highest Trading Volume
    top_volume_days(data, 5)

    # Analysis 6: Daily Percentage Change
    daily_percentage_change(data)

    # Monte Carlo Simulation
    num_simulations = 5
    num_days = 30
    # monte_carlo_simulation(data, num_simulations, num_days)

if __name__ == "__main__":
    main()
