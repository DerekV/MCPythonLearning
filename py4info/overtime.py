hours = raw_input("enter the number of hours you worked this week: " )
hours_float = float(hours)

rate = raw_input("enter the rate your payed: " )
rate_float = float(rate)

print rate_float, hours_float

if hours <= 40 :
    pay = hours_float * rate_float
if pay > 40 :
    pay = rate_float * 40 + (rate_float * 1.5 * hours_float - 40)
    
print pay
