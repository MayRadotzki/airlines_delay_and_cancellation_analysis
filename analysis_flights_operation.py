import pandas as pd
import numpy as np
import Days_Names
import matplotlib.pyplot as plt

#Q1
data_flights = pd.read_csv('flights.csv')
data_airports = pd.read_csv('airports.csv')
data_airlines = pd.read_csv('airlines.csv')

#1
print("Rows:", data_flights.shape[0])

#2
print(data_flights[0:0])

#3
print("Rows:", data_airports.shape[0])
print(data_airports[0:0])

#4
print("Rows:", data_airlines.shape[0])
print(data_airlines[0:0])

# 5
# this question is in the pdf file attached


# Q2
#1
delayed_in_2015 = data_flights[data_flights['DEPARTURE_DELAY'] > 0]
count_delayed_in_2015 = delayed_in_2015['DEPARTURE_DELAY'].count()
print('Delayed in 2015:', count_delayed_in_2015)

#2
days_groups = delayed_in_2015.groupby(['DAY_OF_WEEK']).count().reset_index()
max_delay = days_groups['DEPARTURE_DELAY'].max()
num_of_day = int(days_groups[days_groups.DEPARTURE_DELAY == max_delay].DAY_OF_WEEK)
day_of_week = Days_Names.day_name(num_of_day)
print('Day of week with max delayed:', day_of_week)

# 3
#3a
max_distance = data_flights["DISTANCE"].max()
print('Distance:', max_distance)

#3b
flights_with_max_distance = data_flights[data_flights.DISTANCE == max_distance]
ORIGIN_AIRPORT = flights_with_max_distance.ORIGIN_AIRPORT.unique()
DESTINATION_AIRPORT = flights_with_max_distance.DESTINATION_AIRPORT.unique()
FULL_NAME_ORIGIN = list(data_airports[data_airports.IATA_CODE.isin(ORIGIN_AIRPORT)].AIRPORT)
FULL_NAME_DESTINATION = list(data_airports[data_airports.IATA_CODE.isin(DESTINATION_AIRPORT)].AIRPORT)
print('Airports ​full ​name (origin) :',FULL_NAME_ORIGIN)
# I print the next row in case that the flight doesn't return to the same destination. in this project it unnecessary.
print('Airports ​full ​name (destination):',FULL_NAME_DESTINATION)

#3c
num_day_of_week = list(flights_with_max_distance.DAY_OF_WEEK.unique())
for i in num_day_of_week:
    day_week = Days_Names.day_name(i)
    print('Day of the week:',day_week)

#4
IATA_CODE_OF_JET = list(data_airlines[data_airlines['AIRLINE'] == 'JetBlue Airways'].IATA_CODE)
JET_TAILS_NUMBERS = delayed_in_2015[delayed_in_2015['AIRLINE'] == IATA_CODE_OF_JET[0]].TAIL_NUMBER
print('Tails numbers:\n',JET_TAILS_NUMBERS)


#Q3
#1
cancelled_flights = data_flights[data_flights['CANCELLED'] == 1]
count_cancelled_flights = cancelled_flights['CANCELLED'].count()
# print('Cancelled in 2015:',count_cancelled_flights)

#2
cancelled_reasons = cancelled_flights.groupby(['CANCELLATION_REASON'],sort=False).count().reset_index()
print(cancelled_reasons)
max_for_reason = cancelled_reasons['Unnamed: 0'].max()
common_reason = list(cancelled_reasons[cancelled_reasons.CANCELLED == max_for_reason].CANCELLATION_REASON)
print("The most common reason for cancellation is: ",common_reason[0])

reason_counts = cancelled_flights['CANCELLATION_REASON'].value_counts()
reason_plot= reason_counts.plot('bar')
plt.show()
#we can see that reason B is the most common,10630 flights are canceled due to this reason.
#A is the next common reason with 3230 cancelled flights, then c with 2962 and then D with just 2 cancellations.


#3
percentage_of_canceled= (count_cancelled_flights / data_flights['FLIGHT_NUMBER'].count())*100
print(percentage_of_canceled)

#4
max_distance_in_cancelled = cancelled_flights["DISTANCE"].max()
min_distance_in_cancelled = cancelled_flights["DISTANCE"].min()

cancelled_flights_with_min_distance = cancelled_flights[cancelled_flights.DISTANCE == min_distance_in_cancelled]
origin_airport = cancelled_flights_with_min_distance.ORIGIN_AIRPORT.unique()
dest_airport = cancelled_flights_with_min_distance.DESTINATION_AIRPORT.unique()
airport_full_name_origin = list(data_airports[data_airports.IATA_CODE.isin(origin_airport)].AIRPORT)
airport_full_name_dest = list(data_airports[data_airports.IATA_CODE.isin(dest_airport)].AIRPORT)
print('Shortest path: from {} to {}'.format(airport_full_name_origin[0], airport_full_name_dest[0]))

cancelled_flights_with_max_distance = cancelled_flights[cancelled_flights.DISTANCE == max_distance_in_cancelled]
origin_airport = cancelled_flights_with_max_distance.ORIGIN_AIRPORT.unique()
dest_airport = cancelled_flights_with_max_distance.DESTINATION_AIRPORT.unique()
airport_full_name_origin = list(data_airports[data_airports.IATA_CODE.isin(origin_airport)].AIRPORT)
airport_full_name_dest = list(data_airports[data_airports.IATA_CODE.isin(dest_airport)].AIRPORT)
print('Longest path: from {} to {}'.format(airport_full_name_origin[0], airport_full_name_dest[0]))


#Q4
#1
days =['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
x1 = days
y1 = list(days_groups['DEPARTURE_DELAY'])
plt.xlabel('Days week')
plt.ylabel('Number of delayed flights')
plt.title('Delayed flights in 2015')
plt.bar(x1,y1)
plt.show()

#2
labels ='Cancelled', 'Non-Cancelled'
sizes = [percentage_of_canceled, 100-percentage_of_canceled]
explode = (0, 0.1)
colors = ['gold', 'lightskyblue']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels,colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
ax1.set_title('Percentage of canceled flights in 2015\n')
plt.show()

#3
x2= ['Delayed','Cancelled']
y2= [count_delayed_in_2015,count_cancelled_flights]
plt.xlabel('Number of Flights')
plt.ylabel('s')
plt.barh(x2,y2)
plt.title('Delayed vs cancelled flights in 2015')
plt.show()








