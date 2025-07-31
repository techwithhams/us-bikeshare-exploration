import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('Please enter which city would you like to choose chicago, new york city or washington?\n').lower()
        if city not in CITY_DATA:
            print('Sorry, Not a Vaild City. Please Try Again.')
        
        else:
            break
        
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please enter which month would you like to choose all, january, february, ... june.\n').lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        if month not in months:
            print('Sorry, Not a Valid Month. Please Try Again.')
            
        else:
            break
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please enter which day would you like to choose all, monday, tuesday, ... sunday.\n').lower()
        days = ['monday', 'tuesday', 'wednesday', 'thursday','friday','saturday', 'sunday', 'all']
        if day not in days:
            print('Sorry, Not a Valid Day. Please Try Again.')
            
        else:
            break
    


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """    
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
        
        
    if day != 'all':
        
        df = df[df['day_of_week'] == day.title()]
    
    
    return df
  
            

  


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('The Most Common Month: ', popular_month)


    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The Most Common Day: ' , popular_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The Most Common Hour: ', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('\nThe Most Common Used Start Station: ', common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('\nThe Most Common Used End Station: ', common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    common_start_end_station = df.groupby(['Start Station', 'End Station']).count().idxmax()
    print('\nThe Most Common Frequent Combination of Start and End Station: ', common_start_end_station)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nThe Total Travel Time: ', total_travel_time, 'seconds or ', total_travel_time/60, 'minutes or ', total_travel_time/3600, 'hours or ', total_travel_time/86400, 'days')


    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('\nThe Mean of Travel Time: ', average_travel_time, 'seconds or', average_travel_time/60, 'minutes or ', average_travel_time/3600, 'hours or ', average_travel_time/86400, 'days') 


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nUser Types: ', user_types)
    


    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('\n Counts of Gender: ', df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
  
    if 'Birth Year' in df:
        earliest_birth_year = int(df['Birth Year'].min())
        print('\nThe Earliest Year of Birth: ', earliest_birth_year)
        most_recent_birth_year = int(df['Birth Year'].max())
        print('\nThe Most Recent Year of Birth: ', most_recent_birth_year)
        common_birth_year = int(df['Birth Year'].mode()[0])
        print('\nThe Most Common Year of Birth: ', common_birth_year)
        
    else:
        print('there is no data for this city')
                          
              

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
    
def display_raw_data(df):
    """Ask User if he/she wants to display the raw data and print 5 rows at each time."""
    
    raw_data = input('\nWould you like to see the first 5 rows of data?\n').lower()
    if raw_data == 'yes':
        count = 0 
        while True:
            print(df.iloc[count:count+5])
            count += 5
            next_data = input('\nWould you like to see the next 5 rows of data?\n').lower()
            if next_data != 'yes':
                break
    
   
    
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
