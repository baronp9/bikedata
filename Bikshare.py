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
        city = input("Please enter the city name you want to explore. Available choices: chicago, new york city, washington. ").lower()
        if city in CITY_DATA: 
            break
        else:
            print("That city is not in the registry. Please try again.")

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    while True:
        month = input("Please enter the month you would like to view. ('all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'):").lower()
        if month in months:
            break
        else:
            print("Invalid input, try again.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input("Please enter the day of the week you would like to view. ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):").lower()
        if day in days:
            break
        else:
            print("Invalid input, try again.")

    print('-'*40)
    return city, month, day

def display_data(df):
   
    start_loc = 0
    end_loc = 5
    while True: 
        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
        if view_data == 'yes': 
            print(df.iloc[start_loc:end_loc])
            start_loc += 5
            end_loc += 5
            view_display = input("Would you like to continue?: ").lower()
            if view_display == 'yes':
                continue
            else: 
                break
        else:
                break

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
    df['day'] = df['Start Time'].dt.dayofweek
    df['Hour'] = df['Start Time'].dt.hour 
    
    if month != 'all': 
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1
        df = df[df['month']== month]

    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day)
        df = df[df['day'] == day]

    return df 
    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('the most common month is:', common_month) 

    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]
    print('the most common day is:', common_day) 

    # TO DO: display the most common start hour
    common_start_hour = df['Hour'].mode()[0]
    print('the most common start hour is:', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    c_start_station = df['Start Station'].mode()[0]
    print('The most common start station is:',c_start_station)

    # TO DO: display most commonly used end station
    c_end_station = df['End Station'].mode()[0]
    print('The most common end station is:',c_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combo = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('The most frequent combination of start and end station trips is:', combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('The total amount of time traveled was:', total_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('The average amount of time traveled was:', mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Total count of users:', user_types)
    

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
            gender_count = df['Gender'].value_counts()
            print('Total count of users based on gender', gender_count)
    else:
            print("Data unavaliable")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
        print('The oldest user was born in:', earliest)
        print('The youngest user was born in:', most_recent)
        print('The most common birth year is:', most_common)
    else:
        print("Birth year is unavaliable for this dataset")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        

if __name__ == "__main__":
	main()
