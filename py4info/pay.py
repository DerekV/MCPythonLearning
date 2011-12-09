# A program that prompts the user for hours and rate per hour to computer gross pay

user_hours = raw_input('Enter the hours you work: ')
user_hours_int = float(user_hours)

user_rate = raw_input('Now enter the number of hours worked: ')
user_rate_int = float(user_rate)

pay = user_hours_int * user_rate_int

print ('Your pay total is %r') % pay
