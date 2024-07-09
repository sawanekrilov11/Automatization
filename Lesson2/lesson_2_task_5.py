def month_to_season(number_of_month):
    if number_of_month in [12,1,2]:
        return "Winter"
    elif number_of_month in [3,4,5]:
        return "Spring"
    elif number_of_month in [6,7,8]:
        return "Summer"
    elif number_of_month in [9,10,11]:
        return "Autumn"
    else:
        return "Некорректный номер месяца"

print(month_to_season(6))
    