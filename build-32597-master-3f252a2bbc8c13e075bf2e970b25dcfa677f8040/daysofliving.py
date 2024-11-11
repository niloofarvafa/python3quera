from datetime import datetime

def day_calculator():
    date_str = input("Enter a date (YYYY-MM-DD): ")
    print(f"Input date: {date_str}")  # Debugging print
    date = datetime.strptime(date_str, '%Y-%m-%d')
    sajjad_bdate = datetime.strptime("1999-01-14", '%Y-%m-%d')
    diff_date = (date - sajjad_bdate).days
    print(f"Difference in days: {diff_date}")  # Debugging print
    if diff_date < 0:
        return "Not yet born"
    else:
        return diff_date

if __name__ == "__main__":
    result = day_calculator()
    print(result)