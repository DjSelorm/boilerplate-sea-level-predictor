import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('https://github.com/DjSelorm/boilerplate-sea-level-predictor/blob/main/epa-sea-level.csv')
    df.head()

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    #Adding labels for the x and y axes and a title will make the plot more informative.
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level (inches)')
    plt.title('Sea Level Rise Over Time')
    plt.grid(True)
    plt.show()

    # Create first line of best fit
    x_data = df['Year']
    y_data = df['CSIRO Adjusted Sea Level']
    
    # 3. Apply the linregress function
    slope, intercept, r_value, p_value, std_err = linregress(x_data, y_data)
    
    # 5. Create a new array of years for prediction up to 2050
    # The original 'Year' column might not include all years as integers, so ensure we get a range from min year to 2050
    years_extended = np.arange(x_data.min(), 2051, 1)
    
    # 6. Calculate the predicted sea level values for this new array of years
    predicted_sea_level = intercept + slope * years_extended
    
    # Plotting the scatter plot (from the previous step)
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # 7. Plot the regression line
    plt.plot(years_extended, predicted_sea_level, color='red', label='Regression Line (1880-2050)')
    
    plt.xlabel('Year')
    plt.ylabel(' Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.grid(True)
    plt.legend()
    plt.show()

    # Create second line of best fit
    plt.figure(figsize=(12, 7))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')
    plt.plot(years_extended, predicted_sea_level, color='red', label='Regression Line (1880-2050)')
    
    # 1. Filter data for years 2000 onwards
    df_2000_onwards = df[df['Year'] >= 2000]
    
    # 2. Extract x_data and y_data for the new subset
    x_data_2000 = df_2000_onwards['Year']
    y_data_2000 = df_2000_onwards['CSIRO Adjusted Sea Level']
    
    # 3. Apply the linregress function to the filtered data
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(x_data_2000, y_data_2000)
    
    # 4. Create a new array of years for prediction (from 2000 up to 2050)
    years_extended_2000 = np.arange(x_data_2000.min(), 2051, 1)
    
    # 5. Calculate the predicted sea level values for this new array of years
    predicted_sea_level_2000 = intercept_2000 + slope_2000 * years_extended_2000
    
   
    
    # 6. Plot this new regression line
    # Add labels and title
    plt.plot(years_extended_2000, predicted_sea_level_2000, color='green', label='Regression Line (2000-2050)')
    
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level (inches)')
    plt.title('Sea Level Rise Over Time with Two Regression Lines')
    plt.grid(True)
    plt.legend()
    plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
