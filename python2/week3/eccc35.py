from sys import exit

def gold_room():
    print "Your in the gold room, how much money do you take?"
    next = raw_input(">")
    how_much = int(next)
    #if "0" in next or "1" in next:
    if how_much <= 50 in how_much:
        print "Nice"
    if >= 50 in how_much:
        print "You're a greedy bastard!."
    else:
        print "WHY U NO TYPE NUMBER"
        exit(1)
        

gold_room()
