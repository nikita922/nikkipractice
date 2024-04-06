months = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

month_name = input("Enter a month: ")
days = months.get(month_name, "Invalid month")

if days != "Invalid month":
    print(month_name, "has", days, "days")
else:
    print("Invalid month.")
