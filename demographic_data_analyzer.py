import pandas as pd


def calculate_demographic_data(print_data=True):
    df = pd.read_csv("adult.data.csv")

    # 1. Count of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1
    )

    # 4. Higher education (Bachelors, Masters, Doctorate)
    higher_edu = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_edu = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # 5. % >50K for higher education
    higher_education_rich = round(
        (higher_edu['salary'] == '>50K').mean() * 100, 1
    )

    # 6. % >50K for lower education
    lower_education_rich = round(
        (lower_edu['salary'] == '>50K').mean() * 100, 1
    )

    # 7. Minimum work hours
    min_work_hours = df['hours-per-week'].min()

    # 8. % rich among those who work minimum hours
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (num_min_workers['salary'] == '>50K').mean() * 100, 1
    )

    # 9. Country with highest % of >50K
    country_salary = df[df['salary'] == '>50K']['native-country'].value_counts()
    total_country = df['native-country'].value_counts()

    country_percentage = (country_salary / total_country * 100).sort_values(ascending=False)

    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = round(country_percentage.max(), 1)

    # 10. Most popular occupation for >50K in India
    top_IN_occupation = (
        df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
        ['occupation']
        .value_counts()
        .idxmax()
    )

    if print_data:
        print("Race Count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors:", percentage_bachelors)
        print("Higher edu rich %:", higher_education_rich)
        print("Lower edu rich %:", lower_education_rich)
        print("Min work hours:", min_work_hours)
        print("Rich % (min workers):", rich_percentage)
        print("Highest earning country:", highest_earning_country)
        print("Highest earning country %:", highest_earning_country_percentage)
        print("Top occupation in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }