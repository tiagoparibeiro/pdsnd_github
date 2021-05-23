import time
import pandas as pd
import numpy as np

city_data = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

days_of_week = ['sunday', 'monday', 'tuesday', 'wendsday','thursday', 'friday', 'saturday']


##################   1) GET FILTER FUNCTION   #################################
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = 0
    while city not in city_data.keys():
        try:
            city_choice = int(input("Insert the number corresponding the city we are going to analyse \n1 - Chicago\n2 - New York City\n3 - Washington\nAnswer: "))
            #Converting answer number to city name
            if city_choice == 1:
                city = 'chicago'
            elif city_choice == 2:
                city = 'new york city'
            elif city_choice == 3:
                city = 'washington'
        except ValueError:
                print("\nHum... this type of data is not valid. Please, insert a number between 1 and 3")


    # get user input for month (all, january, february, ... , june)
    month = ''
    while (month not in months) and (month != 'all'):
        month = input("Insert the month we are going to analyse (all, january, february, ... , june): ").lower()


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_choice = ''
    while (day_choice not in days_of_week) and (day_choice != "all"):
        day_choice = input("Insert the day of week we are going to analyse (all, monday, tuesday, ..., sunday): ").lower()

    # converting day of the week from string to int
    if day_choice == 'sunday':
        day = 0
    elif day_choice == 'monday':
        day = 1
    elif day_choice == 'tuesday':
        day = 2
    elif day_choice == 'wendsday':
        day = 3
    elif day_choice == 'thursday':
        day = 4
    elif day_choice == 'friday':
        day = 5
    elif day_choice == 'saturday':
        day = 6
    elif day_choice == 'all':
        day = day_choice


    print('-'*40)
    return city, month, day



###############   2) LOAD DATA FUNCTION   ####################################
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
    print("\n")
    print("Loading Data...")

    # load data file into a dataframe
    df = pd.read_csv('{}'.format(city_data[city]))

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] =df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['Hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) +1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df



############### 3) TIME STATS FUNCTION ######################################
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month_mode = df['month'].mode()
    month_frequancy = df['month'].value_counts()
    month_name = ''

    #converting month int to string
    if month_mode[0] == 1:
        month_name = 'January'
    elif month_mode[0] == 2:
        month_name = 'Februar'
    elif month_mode[0] == 3:
        month_name = 'March'
    elif month_mode[0] == 4:
        month_name = 'April'
    elif month_mode[0] == 5:
        month_name = 'May'
    elif month_mode[0] == 6:
        month_name = 'June'
    elif month_mode[0] == 7:
        month_name = 'July'
    elif month_mode[0] == 8:
        month_name = 'August'
    elif month_mode[0] == 9:
        month_name = 'September'
    elif month_mode[0] == 10:
        month_name = 'October'
    elif month_mode[0] == 11:
        month_name = 'November'
    elif month_mode[0] == 12:
        month_name = 'December'



    print("Most common month for bike travels was {}".format(month_name))
    ## debug ##
    #print("\n")
    #print("Getting Month Frequency to check result...")
    #print(month_frequancy)
    #print("\n")

    # display the most common day of week
    day_of_week_mode = df['day_of_week'].mode()
    day_of_week_frequency = df['day_of_week'].value_counts()

    print("Most common day of the week for bike travels was {} (sunday = 0, saturday = 6)".format(day_of_week_mode[0]))
    ## debug ##
    #print("\n")
    #print("Getting Day of Week Frequency to check result...")
    #print(day_of_week_frequency)


    # display the most common start hour
    hour_mode = df['Hour'].mode()
    hour_frequency = df['Hour'].value_counts()

    print("Most common hour to start a bike travel was {}".format(hour_mode[0]))
    ## debug ##
    #print("\n")
    #print("Getting Hour Frequency to check result...")
    #print(hour_frequency)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print("\n")



############### 4) STATSION STATS FUNCTION #####################################
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station_mode = df['Start Station'].mode()
    start_station_frequency = df['Start Station'].value_counts()

    print("Most common start station was {}".format(start_station_mode[0]))
    ## debug ##
    #print("\n")
    #print("Getting Start Station Frequency to check result...")
    #print(start_station_frequency)

    # display most commonly used end station
    end_station_mode = df['End Station'].mode()
    end_station_frequency = df['End Station'].value_counts()

    print("Most common end station was {}".format(end_station_mode[0]))
    ## debug ##
    #print("\n")
    #print("Getting End Station Frequency to check result...")
    #print(end_station_frequency)

    # display most frequent combination of start station and end station trip
    stations_combination_1 = df.groupby(['Start Station','End Station']).size().idxmax()
    stations_combinations = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False)

    print("Most common route was from {} to {}".format(stations_combination_1[0],stations_combination_1[1]))
    ## debug ##
    #print("\n")
    #print("Getting Station Combination Frenquency to check result...")
    #print(stations_combinations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print("\n")



############### 5) TRIP DURANTION STATS FUNCTION ###############################
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_duration_sum = round((df['Trip Duration'].sum()/60),2)

    print('Total bike travel duration sum was {} minutes'.format(travel_duration_sum))


    # display mean travel time
    travel_duration_mean = round((df['Trip Duration'].mean()/60),2)

    print('Total travel duration mean was {} minutes'.format(travel_duration_mean))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print("\n")



############### 6) USER STATS FUNCTION ###############################
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_counts = df['User Type'].value_counts()

    print('\nGetting User Types...\n')
    print(user_type_counts)

    # Display counts of gender
    try:
        user_gender_counts = df['Gender'].value_counts(dropna=False)

    #some data sets do not have gender column, this excepation handles the problem
    except KeyError:
        print("\nWarning! Gender is not present in this Data Set!")

    else:
        print('\n\nGetting User Genders...\n')
        print(user_gender_counts)

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_year = round(df['Birth Year'].min())
        recent_year = round(df['Birth Year'].max())
        commons_years = round(df['Birth Year'].mode())
        common_year = int(round(commons_years[0],0))
        year_frequency = round(df['Birth Year'].value_counts())

    #some data sets do not have year birth column, this excepation handles the problem
    except KeyError:
        print("\nWarning! Birth Year is not present in this Data Set!")

    else:
        print('\n\nGetting Birth Years...\n')
        print('Earliest Birth Year    {}'.format(earliest_year))
        print('Recent Birth Year      {}'.format(recent_year))
        print('Most Common Birth Year {}'.format(round(common_year)))

    ## debug ##
    #print("\n")
    #print("Getting Year Birth Frenquency to check result...")
    #print(year_frequency)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print("\n")



####################### 7) PRESENT RAW DATA FUNCTION ###############################
def raw_data(df):
    '''
        Displays the data frame's raw data five rows at a time. At the end, the function asks if the user wants to see the next 5 rows.
    '''

    # Asking if the user wants to see 5 rows of raw data
    data_presentation = ''
    while data_presentation not in ("yes","no"):
        try:
            data_presentation = input("\nWould you like to see 5 rows of raw data? (yes/no)\nAnswer:  ").lower()
        except ValueError:
            print("\nHum... this type of data is not valid. Please, insert yes or no")

        if data_presentation == 'no':
            break
        elif data_presentation ==  'yes':
            print('-'*40)
            # defining the first (i) and last (f) row variables that will allow itarating 5 rows at a time and printing it.
            i = 0
            f = 5
            print(df[i:f])
            print('-'*40)
            print("\n")

            # Asking if the user wants to see the next 5 rows.
            while True:
                answer = ''
                i = f
                f = i + 5 # NOTE: Would be better to define a variable 'n' by asking the user how many rows they would like to see instead of using the number 5.

                while answer not in ("yes","no"):
                    answer = input("\nWould you like to see the next 5 rows? (yes/no)\nAnswer: ").lower()

                if answer == "no":
                    break
                elif answer == "yes":
                    print(df[i:f])
                    print('-'*40)
                    print("\n")
                    continue

            continue

    print('-'*40)


####################### 8) MAIN FUNCTION ###############################
def main():
    while True:
        #Getting Filters and Loading the data file
        city, month, day = get_filters()
        df = load_data(city, month, day)

        #Presenting statistics
        try:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
        #if the user select a combination of city, month and day of week that does not have any data, an IndexError will occur, this exception solve this problem
        except IndexError:
            print("There is no data to be presented!")

        #Offering the possibility of looking at the raw data five rows at a time
        raw_data(df)

        #Asking if the user wants to restart the program
        restart = ''
        while restart not in ('yes','no'):
            restart = input('\nWould you like to restart? Enter yes or no.\n').lower()

        if restart == 'no':
            break
        elif restart == 'yes':
            print('-'*40)
            print("\n")
            continue


if __name__ == "__main__":
	main()
