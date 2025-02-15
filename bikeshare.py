import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new York': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!\n')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input(
            "Would you like to see data for Chicago, New York or Washington?\n").lower()
        if city in ('chicago', 'new york', 'washington'):
            break
        else:
            print(
                "Please can you write only one city to see data for Chicago, New York or Washington?")
            continue

    # get user input for month (all, january, february, ... , june)

    while True:
        month = input("\nWould you like to see data for specific month( january, february, march, april, may, june )... you can type all to see the data for all these months\n").lower()
        if month in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            break
        else:
            print("Please can you write only one month or all")
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("\nWould you like to see data for specific day( monday, tuesday, wednesday, thursday, friday, saturday, sunday )... you can type all to see the data for all these days\n").lower()
        if day in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            break
        else:
            print("Please can you write only one day or all")
            continue

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    common_month = df['month'].mode()[0]
    print('The most common month is: ', common_month)

    # display the most common day of week

    common_day = df['day_of_week'].mode()[0]
    print('The most common day is: ', common_day)

    # display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print('The most common start hour is: ', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    common_start_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is: ', common_start_station, '\n')

    # display most commonly used end station

    common_end_station = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station is: ', common_end_station, '\n')

    # display most frequent combination of start station and end station trip

    frequent_combination_station = df[[
        'Start Station', 'End Station']].mode().loc[0]
    print('The most commonly used combination of start station and end station trip {}, {}'
          .format(frequent_combination_station[0], frequent_combination_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    print('Total travel time is... ', sum(df['Trip Duration']))

    # display mean travel time

    print('Mean travel time is... ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_types = df['User Type'].value_counts()
    print('The counts of user types are: ', user_types, '\n')

    # Display counts of gender

    try:
        gender_counts = df['Gender'].value_counts()
        print('The counts of gender are: ', gender_counts, '\n')
    except KeyError:
        print('The counts of gender are: there is no data\n')

    # Display earliest, most recent, and most common year of birth

    try:
        print('The earliest year is: ', df['Birth Year'].min(), '\n')
    except KeyError:
        print('The earliest year is: there is no data\n')

    try:
        print('The most recent year is: ', df['Birth Year'].max(), '\n')
    except KeyError:
        print('The most recent year is: there is no data\n')

    try:
        print('The most common year is: ',
              df['Birth Year'].value_counts().idxmax(), '\n')
    except KeyError:
        print('The most common year is: there is no data\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):

    view_data = input(
        '\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while (view_data == 'yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()


def project_name():
    print("bikeshare")


def print_info():
    print("proggraming for data science nanodegree\n")
    print("Udacity")


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
