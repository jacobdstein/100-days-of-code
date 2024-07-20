def is_leap_year(the_year: int) -> bool:
    return the_year % 4 == 0 and (the_year % 100 != 0 or the_year % 400 == 0)


month_days = {
    "January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31,
    "August": 30, "September": 31, "October": 30, "November": 31, "December": 30
}

month = input("Enter a month: ")
year: int = int(input("Enter a year: "))

days = month_days[month]
if month == "February" and is_leap_year(year):
    days += 1

print(f"There are {days} days in {month}, {year}.")
