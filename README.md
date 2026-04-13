# Grouse Mountain Temperature Analysis 

![Project Screenshot](temp_graph.png)
![Project Screenshot](whistler_snow_cmp.png)

Description 

Our project is a visual analysis of the High and Low Temperatures on Grouse Mountain over different timeframes.
Our first graph displays the general trends of temperatures in the year of 2026. Since Grouse Mountain is located in North Vancouver, we thought it would be interesting to learn more about weather changes and patterns in a local area.
Additonally, we created a second graph comparing snowfall over a 50 year period. For this graph, we used data from Whistler as we could not locate enough historical data for Grouse Mountain. The graph looks at snowfall in Whistler at the Whistler Roundhouse in 1973 and compares it with the snowfall there in 2023. 

Features 
* Shaded Daily-range: Uses 'fill_between' function to shade daily range between highs and lows
* Grid Lines: Makes it easy to identify precise values on graph 
* Legend: Allows user to identify symbols and colours on graph
* Error Handling: Uses 'try-except' block to detect and ignore incorrect data so that the program doesn't crash
* For Loop: to extract every high and low temperature and every date in each row (unless marked as empty string, then accounted for with except block)

Built With 
* Matplotlib - Transforms raw data into graphs 
* CSV module - Used to read and extract data from CSV files
* datetime class from datetime module - Used to extract dates in notation yy-mm-dd
* Path class from pathlib - Used with csv module to read csv file containing data
* Python 3.x

Code Overview
The project is structured around efficient data processing and clear visualization. Key implementations include:

1. Data Extraction with Error Handling The program iterates through rows of CSV data using a try-except block. This ensures that if a temperature value is missing (a common issue in weather datasets), the program logs the error and continues instead of crashing:

Python
dates, highs, lows = [], [], []

for row in reader:
    current_date = datetime.strptime(row[4], '%Y-%m-%d')
    try:
        high = float(row[9])
        low = float(row[11])
    except ValueError:
        print(f"Error parsing data at {current_date}")
        continue
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        
2. Visualizing Temperature Ranges To make the data easy to read at a glance, we use the fill_between function. This creates a shaded "Daily Range" between the high and low temperature lines:

Python
# Plotting the lines and shading the range
ax.plot(dates, highs, color='red', alpha=0.5, label='High Temperatures')
ax.plot(dates, lows, color='blue', alpha=0.5, label='Low Temperatures')
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1, label='Daily Range')

Pre-requisites

Install Matplotlib
'''bash pip install matplotlib'''

How to Run
Clone or download this repository.

Ensure you have the required CSV files (whistler_snow_73.csv, whistler_snow_23.csv, etc.) in the project directory.

Open the project file grouse_mtn_data.py or whistler_snow.py in your Python IDE.

Run the program:

Bash
python grouse_mtn_data.py
A window will open showing the temperature trends and snowfall comparisons. Click the "X" on the window to close it.

License

This project is open-source and free to use for educational purposes.

Credits 
https://climate.weather.gc.ca/climate_data/daily_data_e.html?hlyRange=%7C&dlyRange=1960-01-01%7C1961-12-31&mlyRange=1960-01-01%7C1961-12-01&climate_id=1105656&Prov=BC&urlExtension=_e.html&searchType=stnName&optLimit=yearRange&StartYear=1840&EndYear=2026&selRowPerPage=25&Line=1&searchMethod=contains&Month=12&Day=8&txtStationName=north+vancouver&timeframe=2&Year=1961

Writers 
Lauren Desprez
Kiana Sahota 




