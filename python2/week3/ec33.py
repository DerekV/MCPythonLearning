
numbers = []

def number_loop(i,x,y):
    while i < x and y < x:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        y = i + 2
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
        print "Extra fun is %d" % y
        
number_loop(1,10,3)


