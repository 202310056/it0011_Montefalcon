date = input('Enter the date (mm/dd/yyyy): ')

month, day, year = date.split('/')

months = {
    '01': 'January', '02': 'February', '03': 'March', '04': 'April',
    '05': 'May', '06': 'June', '07': 'July', '08': 'August',
    '09': 'September', '10': 'October', '11': 'November', '12': 'December'
}

if month in months:
    month_name = months[month]
else:
    month_name = "Invalid month"

print(f"Date Output: {month_name} {int(day)}, {year}")