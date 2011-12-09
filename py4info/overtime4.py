def computepay():
    rate = raw_input("Enter your pay: ")
    rate_int = int(rate)

    hours = raw_input("Enter the number of hours worked: ")
    hours_int = int(hours)
    
    if hours < 40:
        rate = hours_int * rate_int
    print "Your pay for the week is %r" % rate
        
computepay()
        
    
