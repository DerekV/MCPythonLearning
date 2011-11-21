  
def gold_room():
    print "This room is full of gold.  How much do you take?"
    try:
        next = raw_input("> ")
        load = int(next)
    except:
        print "Please enter a number"
        exit(1)
    print "you entered:", next
    #if next <= 50:
        #print "Nice"
    #elif next >= 50:
        #print "You're a greedy bastard!."
   # else 
        #print "WHY U NO TYPE NUMBER"

gold_room()

