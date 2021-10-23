import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let\'s explore some US bikeshare data!")
    # TO DO: get user input for city (chicago, new york , washington). HINT: Use a while loop to handle invalid inputs
    city=input("Please enter your city among these 3 cities (chicago, new york city, washington): ")     
    while city.lower() not in ('chicago','new york city','washington'):
        city=input("Invalid Entry Detected! Enter city among these 3 cities (chicago, new york city, washington): ")
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month=input("Please enter the month you would like to search from these months(all, january, february, ... , june) and all to see all : ")
    while month.lower() not in ('all','january','february','march','april','may','june'):
        month=input(" Invalid Month Detected! Please enter month from these months(all, january, february, ... , june) and all to see all : ")
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("please enter the day of the week you would like to search from these days(all, monday, tuesday, ... sunday) and all to see all : ")
    while day.lower() not in ('all','monday','tuesday','wednesday','thursday','friday','saturday','sunday'):
        day=input(" Invalid Day Entry Detected!please enter the day of the week from these days(all, monday, tuesday, ... sunday) and all to see all : ")
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
    # load the file int dataframe names df
    df=pd.read_csv(CITY_DATA[city])
    
    # Extract the start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Extract the month out of the start time
    df['month']=df['Start Time'].dt.month
    
    # Extract the day out of the start time
    df['day_of_week']=df['Start Time'].dt.weekday_name
    
    # filter by month
    if month.lower() != 'all':
        #checking  with the month index to return the month filter
        months=['january', 'february', 'march', 'april', 'may', 'june']
        month=months.index(month) + 1
        
        # filter by month to create a new dataframe
        df=df[df['month']==month]
        
    # filter by day
    if day.lower() != 'all':
        # filter by day of the week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df['month'].mode()[0]
    print('The most common month is :', common_month)
        
    # TO DO: display the most common day of week
    common_day=df['day_of_week'].mode()[0]
    print('The most common day of week is :', common_day)


    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    common_hour=df['hour'].mode()[0]
    print('The most common start hour is :', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    number=df['Start Station'].value_counts().max()
    print("The most used start station is :{} \nand was used {} times\n".format(df['Start Station'].mode()[0].upper(),number))

    # TO DO: display most commonly used end station
    number2=df['End Station'].value_counts().max()
    print("The most used end station is :{} \nand was used {} times\n".format(df['End Station'].mode()[0].upper(),number2))
    
    
    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination= df.groupby(['Start Station','End Station']).size().nlargest(1)
    print('The most frequent combination of start station and end station trip is :\n{}\n'.format(frequent_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time is : {}'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('The mean travel time is : {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('counts of user types are :\n{}'.format(df['User Type'].value_counts()))
    print('\n')
    if city.lower() !='washington':
    # TO DO: Display counts of gender
        print('counts of gender are:\n{}'.format(df['Gender'].value_counts()))
        print('\n')
    # TO DO: Display earliest, most recent, and most common year of birth
        print('The earliest year of birth is :{}'.format(df['Birth Year'].min()))
        print('The most recent year of birth is :{}'.format(df['Birth Year'].max()))
        print('The most common year of birth is :{}'.format(df['Birth Year'].mode()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    count=0
    while True:
        response=input("would you like to view some raw data ? Enter 'yes' or 'no'")
        if response.lower()=='yes':
            print(df[count:count+5])
            count +=5
        else:
            break


def main() -> object:
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
