from datetime import datetime

dates = [
    "2023-01-01",
    "2022-12-31",
    "2024-02-15",
    "2023-06-10"
]

# Convert strings to datetime objects
dates = [datetime.strptime(date, "%Y-%m-%d") for date in dates]

# Sort the dates (creates a new sorted list)
sorted_dates = sorted(dates)
print(sorted_dates)

# Sort the original list in place
dates.sort()
print(dates)