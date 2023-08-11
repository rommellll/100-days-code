def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(input_year, input_month):
  """"Take year and month to check how many days in contains"""
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if input_month == 2:
      if is_leap(input_year):
          return 29
  month_index = input_month - 1
  return month_days[month_index]

days_in_month()
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(input_year=year, input_month=month)
print(days)







