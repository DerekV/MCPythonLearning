# given a interger thats a perfect square want to find square root of it.
i = 1

while True:
    # Had to find a way to stop the infinte loop back to the message 'enter a number' without the user hitting something. 
    
    if i != 1: break
    x = raw_input('Enter a number: ')
    
    #len(variable) means if the type entered by the user is less then 1 digit (i.e they enter nothing then break.
    if len(x) < 1: break
    x_int = int(x)
    #This bit finds the perfect square of a number in reverse and keeps running until it gets it then breaks out of the loop back to the start of the first while True part.
    while x_int != i * i:
        if x_int >= i * i:
            i = i + 1
        else: 
            print "Sorry this number doesn't have a perfect square"
            quit()
print 'The square root of your number is', i #github edit


