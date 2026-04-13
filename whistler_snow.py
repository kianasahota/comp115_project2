from pathlib import Path 
#imports pathlib class from Path module 

import csv               
#imports csv module 

import matplotlib.pyplot as plt 
#imports matplotlib.pyplot module but shortens pyplot to plt 

from datetime import datetime  
#imports datetime class from datetime module 

#importing data from csv file
path = Path('project_2.py/whistler_snow_73.csv') 

#path.read_text() opens the csv file and puts all the text into python as one big string
#splitlines() splits the big string into lines of smaller strings when encounters '\n' (newline character)
lines = path.read_text().splitlines()

#csv.reader() breaks lines whenever it sees a comma so that it creates columns 
reader = csv.reader(lines)

#reads first row containing all the headers and moves csv reader to the next line, 
# so when iterates in for loop, it starts at the second row, so as to not cause error and program crash 
header_row = next(reader)


for index, column_header in enumerate(header_row):
    print(index, column_header)

dates, snow = [], []

for row in reader:
    date_str = f'{row[6]}-{row[7]}'
    current_date = datetime.strptime(date_str, '%m-%d')
    
    try:
        snow_day = float(row[21])
        
    except ValueError:
        print(f"Error parsing data at {current_date}")
        continue

    else:
        dates.append(current_date)
        snow.append(snow_day)

    print(snow)


#plot max temps
plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots(figsize = (10, 6))
ax.plot(dates, snow, color ='red', alpha = 0.5, label = 'Snowfall Dec 1973')
#ax.plot(dates, lows, color = 'blue', alpha = 0.5, label = 'Low Temperatures')
#ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1, label = 'Daily Range')

#fomratting
ax.set_title("Daily High and Low Temperatures on Grouse Mountain 2026", fontsize = 20) #\n
ax.set_xlabel('Date', fontsize = 16)
#fig.autofmt_xdate()
ax.set_ylabel("Snowfall (mm)",fontsize=16)
ax.tick_params(labelsize=12)


ax.legend(loc = 'upper right', bbox_to_anchor = (0.9, 1.0), fontsize = 12, shadow = True ) #ax.legend(0r)

#Create grid in background 
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_axisbelow(True)

import matplotlib.dates as mdates

# This tells the graph: "Show me the month name (%b), and ignore everything else"
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))

fig.autofmt_xdate()






path2 = Path('project_2.py/whistler_snow_23.csv') 

#path.read_text() opens the csv file and puts all the text into python as one big string
#splitlines() splits the big string into lines of smaller strings when encounters '\n' (newline character)
lines2 = path2.read_text().splitlines()

#csv.reader() breaks lines whenever it sees a comma so that it creates columns 
reader2 = csv.reader(lines2)

#reads first row containing all the headers and moves csv reader to the next line, 
# so when iterates in for loop, it starts at the second row, so as to not cause error and program crash 
header_row2 = next(reader2)


for index, column_header in enumerate(header_row2):
    print(index, column_header)

dates2, snow2 = [], []

for row in reader2:
    date_str = f'{row[6]}-{row[7]}'
    current_date2 = datetime.strptime(date_str, '%m-%d')
    
    try:
        snow_day2 = float(row[21])
        
    except ValueError:
        print(f"Error parsing data at {current_date2}")
        continue

    else:
        dates2.append(current_date2)
        snow2.append(snow_day2)

    print(snow2)


#plot max temps
plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots(figsize = (10, 6))
ax.plot(dates, snow, color ='red', alpha = 0.5, label = 'Snowfall 1973 (318.8 cm)')
ax.plot(dates2, snow2, color = 'blue', alpha = 0.5, label = 'Snowfall 2023 (163.1 cm)')

#fomratting
ax.set_title('Comparison of snowfall in Whistler: 1973 vs. 2023', fontsize = 20)
ax.set_xlabel('Date in year (mm-dd)', fontsize = 16)
#fig.autofmt_xdate()
ax.set_ylabel("Snowfall (cm)",fontsize=16)
ax.tick_params(labelsize=12)


ax.legend(loc = 'upper right', bbox_to_anchor = (0.9, 1.0), fontsize = 12, shadow = True ) #ax.legend(0r)

#Create grid in background 
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_axisbelow(True)

# import matplotlib.dates as mdates

# This tells the graph: "Show me the month name (%b), and ignore everything else"
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))

fig.autofmt_xdate()

plt.show()



