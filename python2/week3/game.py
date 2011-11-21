#Writting a game

#Lets start off slow





def door_choices():
    print "You enter a room, there are two doors labled one and two"
    print "Choose one to open"
    
    door_choose = raw_input(">")
    
    if door_choose == "one":
        print "You choose door one"
    elif door_choose == "two":
        print "You choose door two. You Fail! Try again."
    else:
        print "WHY YOU NO FOLLOW INSTRUCTIONS"
        
door_choices()
