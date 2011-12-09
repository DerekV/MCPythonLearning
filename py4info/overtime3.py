inp = raw_input("Enter Hours: ")
try:
    hours = float(inp)
except:
    print "please enter a number"
    quit()
    
inp = raw_input("Enter Rate: ")
try:
    rate = float(inp)
except:
    print "please enter a number"
    quit()
    

if hours <= 40 :
    pay = rate * hours
if hours > 40 :
    pay = rate * 40 + (rate * 1.5 * (hours - 40))
        
print pay



