def gold_room():
    print "This room is full of gold.  How much do you take?"

    next = input("> ")
    how_much = int(next)
    if how_much <= 50:
        print "Nice, you're not greedy, you win!"
    if how_much > 50:
        print "Not nice, you greedy" 
    else:
        print "Man, learn to type a number."

        
gold_room()
