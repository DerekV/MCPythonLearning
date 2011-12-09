# The program will take input from user and based on if input is even or odd print out 'even' or 'odd'.
try:
    user_input = raw_input('Enter a Interger: ')
    user_input_int = int(user_input)
    
    if user_input_int % 2.0 != 0.0:
        print 'That interger was odd'
    else:
        print 'That interger was even'
except:
    print 'Enter a Interger next time'
    print 'Terrible job'
    quit()
    
print 'great job'
