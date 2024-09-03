days_in_year = 365
days_in_week = 7

days = int(input("Days you have been driving: "))

years = days // days_in_year
remaining_days_after_years = days % days_in_year

weeks = remaining_days_after_years // days_in_week
remaining_days_after_weeks = remaining_days_after_years % days_in_week

print(f"You have been driving for:")
print(f"Years: {years}")
print(f"Years: {weeks}")
print(f"Years: {remaining_days_after_weeks}")
