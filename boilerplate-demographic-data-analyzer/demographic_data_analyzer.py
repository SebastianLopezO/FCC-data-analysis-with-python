import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    file = "adult.data.csv"
    df = pd.read_csv(file)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men =  df[df["sex"] == "Male"]["age"].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df["education"].value_counts(normalize=True)["Bachelors"]*100).round(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    higher_edu_list = ['Bachelors', 'Masters', 'Doctorate']
    is_advanced_education = df['education'].isin(higher_edu_list)
    is_high_salary = df['salary'] == '>50K'

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = (is_advanced_education.mean() * 100).round(1)
    lower_education = 100 - higher_education

    # percentage with salary >50K
    higher_education_rich = round(df[is_advanced_education & is_high_salary].shape[0] / df[is_advanced_education].shape[0]*100,1)
    lower_education_rich = round(df[~is_advanced_education & is_high_salary].shape[0] / df[~is_advanced_education].shape[0]*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df.min()["hours-per-week"]

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df["hours-per-week"]==min_work_hours]["salary"].value_counts()[">50K"]

    rich_percentage = (df[df["hours-per-week"]==min_work_hours]["salary"].value_counts(normalize=True)[">50K"]*100).round(1)

    # What country has the highest percentage of people that earn >50K?
    country_highest_percentage = (df[df["salary"] == ">50K"].groupby("native-country").size() / df.groupby("native-country").size() * 100).round(1)

    highest_earning_country = country_highest_percentage.idxmax()
    highest_earning_country_percentage = country_highest_percentage.max()

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]["occupation"].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
