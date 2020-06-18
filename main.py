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
    print("Type C for Chicago, N for New York or W for Washington")
    while True :

        city_name = input("Please Enter The City Name You Want To Analyze: ").lower() 


        if city_name != "n" and city_name != "c" and city_name!= "w" : 

            print ("Wrong Input! Type C for Chicago, N for New York or W for Washington ")
            continue  
        
        if city_name == "c" : 
            city = CITY_DATA["chicago"] 
            break
        elif city_name == "n" : 
            city = CITY_DATA["new york city"]
            break
        elif city_name == "w" : 
            city = CITY_DATA["washington"]
            break 

    # TO DO: get user input for month (all, january, february, ... , june)
    print("Type 1 to 12 to choose months where January is 1 and December is 12 or Type ALL to display for all months ")
    while True : 

        month_name = input("Which month do you want to see the data for : ").lower()

        if month_name !="1" and month_name!="2" and month_name!="3" and month_name!="4" and month_name!="5" and month_name!="6" and month_name!="7" and month_name!="8" and month_name!="9" and month_name!="10" and month_name!="11" and month_name!="12"  and month_name != "all": 
            print ("Wrong Input! Type 1 to 12 to choose months where January is 1 and December is 12 or Type ALL to display for all months")
            continue

        months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

        if month_name == "all" : 

            print ("No Filters Will Be Applied")
            month = "all"
            break

        else : 

            month = months[int(month_name)-1]
            break 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print ("Type 1 to 7 to choose days where Monday is 1 and Sunday is 7 or Type ALL to display for all days")
    while True : 
        
        day_name = input("Which day do you want the data for : ").lower()

        if day_name !="1" and day_name!="2" and day_name!="3" and day_name!="4" and day_name!="5" and day_name!="6" and day_name!="7" and day_name!="all": 

            print ("Wrong Input! Type 1 to 7 to choose days where Sunday is 1 and Saturday is 7 or Type ALL to display for all days ")
            continue

        days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

        if day_name!= "all" :
            day = days[int(day_name)-1]
            break

        elif day_name == "all" : 
            print("No Filters Will Be Applied")
            day = "all"
            break

    print('-'*40)    
    return (city,month,day)


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
    df = pd.read_csv(city)

    if month == "all" and day == "all" : 
        return df

    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_the_week"] = df["Start Time"].dt.weekday
    
    if month!='all' :

        months = ["January","February","March","April","May",
        "June","July","August","September","October","November","December"]
        month= months.index(month) + 1 

        new_df = df[df["month"]==month]
    else : 
        new_df = df

    if day!="all" : 
        days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        day = days.index(day)+1
        new_df = new_df[df["day_of_the_week"]==day]


    return new_df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Displaying the most popular month if you have chosen 'ALL' option for months : ")
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_the_week"] = df["Start Time"].dt.weekday

    if len(df["month"].unique()) < 2 : 
        print ("*"*40)
        print("Since you have filtered using one month,this does not apply")
        print ("*"*40)
    else : 
        popular_month = df["month"].mode()[0]
        months = ["January","February","March","April","May",
        "June","July","August","September","October","November","December"]
        popular_month= months[popular_month-1]
        print ("The most popular month is : ",popular_month)
     


    # TO DO: display the most common day of week
    print("Displaying the most popular day of the week if you have chosen 'ALL' option for day  : ")   
    if len(df["day_of_the_week"].unique()) < 2 : 
        print ("*"*40)
        print("Since you have filtered using one week,this does not apply")
        print ("*"*40)

    else : 
        popular_day= df["day_of_the_week"].mode()[0]
        day= ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        popular_day= day[popular_day]
        print ("The most popular day of the week is :",popular_day)

    # TO DO: display the most common start hour
    
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used Start Station is :" ,df["Start Station"].mode()[0])

    # TO DO: display most commonly used end station
    print ("The most commonly used End Station is :",df["End Station"].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df["combination_of_start_and_end_stations"] = df["Start Station"] + " " + df["End Station"]
    print ("The most frquent combination of start station and end station:",df["combination_of_start_and_end_stations"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time_travel= np.sum(df["Trip Duration"])
    print("The total travel time is :" , total_time_travel)

    # TO DO: display mean travel time
    mean_travel_time = np.mean(df["Trip Duration"])
    print("The mean travel time is:" , mean_travel_time) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of Subscribers : " , df["User Type"].value_counts()[0])
    print("Counts of Customers : " , df["User Type"].value_counts()[1])
    # TO DO: Display counts of gender
    if "Gender" in df.columns :

        print ("Counts of Men :", df["Gender"].value_counts()[0])
        print ("Counts of Woman :", df["Gender"].value_counts()[1])
    else : 
        print ("No information about Gender is found in this dataset")

    if "Birth Year" in df.columns: 

        print("Most common year of birth : " , df["Birth Year"].mode()[0])
        print("Earliest year of birth :" , df["Birth Year"].min())
        print("Most Recent year of birth:" , df["Birth Year"].max())
      # TO DO: Display earliest, most recent, and most common year of birth
    else : 

        print("No information about Birth Year is found in this dataset")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def do_you_want_to_see_raw_data():
    
    while True : 
        print("Are you interested into looking at raw data ?") 
        answer = input("Please type Y for Yes and N for No : ").lower()

        if answer!="y" and answer!="n" :

            print("Wrong Input! Please type Y for Yes and N for No") 
            continue
        if answer == "n" : 
            break

        if answer == "y" :

            while True :

                print("Type C for Chicago, N for New York or W for Washington")

                city_name = input("Please Enter The City Name You Want To Analyze: ").lower() 


                if city_name != "n" and city_name != "c" and city_name!= "w" : 

                    print ("Wrong Input! Type C for Chicago, N for New York or W for Washington ")
                    continue  
        
                if city_name == "c" : 
                    
                    city = CITY_DATA["chicago"]
                    
                    read = pd.read_csv(city)
                    
                    for i in range(0,len(read),1) :

                        print(read.loc[i])
                        
                        if i%5 == 0 and i!=0 : 
                            
                            print("Do you want more ?")
                    

                            while True :
                                your_input = input("Please type Y for Yes or N for No : ").lower()
                                
                                if your_input!="y" and your_input!="n" : 
                                    print ("Wrong Input! Type Y for Yes, N for No :")
                                    continue  
                                
                                if your_input == 'y' : 
                                   break
                                elif your_input =='n' :
                                    break 
                            if your_input == 'y' : 
                                continue 
                            elif your_input =='n' :
                                break

                if city_name == "n" : 
                    
                    city = CITY_DATA["new york city"]
         
                    read = pd.read_csv(city)
                    
                    for i in range(0,len(read),1) :

                        print(read.loc[i])
                        
                        if i%5 == 0 and i!=0 : 
                            
                            print("Do you want more ?")
                    

                            while True :
                                your_input = input("Please type Y for Yes or N for No : ").lower()
                                
                                if your_input!="y" and your_input!="n" : 
                                    print ("Wrong Input! Type Y for Yes, N for No :")
                                    continue  
                                
                                if your_input == 'y' : 
                                   break
                                elif your_input =='n' :
                                    break 
                            if your_input == 'y' : 
                                continue 
                            elif your_input =='n' :
                                break
 
                if city_name == "w" : 
                    
                    city = CITY_DATA["washington"]
         
                    read = pd.read_csv(city)
                    
                    for i in range(0,len(read),1) :

                        print(read.loc[i])
                        
                        if i%5 == 0 and i!=0 : 
                            
                            print("Do you want more ?")
                    

                            while True :
                                your_input = input("Please type Y for Yes or N for No : ").lower()
                                
                                if your_input!="y" and your_input!="n" : 
                                    print ("Wrong Input! Type Y for Yes, N for No :")
                                    continue  
                                
                                if your_input == 'y' : 
                                   break
                                elif your_input =='n' :
                                    break 
                            if your_input == 'y' : 
                                continue 
                            elif your_input =='n' :
                                break



                break  
def main():
    while True:
        see_data = do_you_want_to_see_raw_data()
        
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter Y for Yes or N for No :').lower()
        if restart!='y' and restart!='n' : 
            print ("Wrong Input! Type Y for Yes, N for No :")
            continue
        if restart.lower() != 'y':
             break
        
if __name__ == "__main__":
	main()
