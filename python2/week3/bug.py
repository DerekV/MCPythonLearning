
age = eval((input)("enter your age :"))

if age < 20:
    print ("Too young.")
elif age > 20:
    print ("Too old.")
elif age == 20:
    print ("giddy giddy.")
else:
    assert False, ("This shouldn't run.")
