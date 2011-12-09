def overtime(a,b):
    if b <= 40:
        z = a * b
        return z
    elif b > 40:
        z = a * b + (((b -40) * a) * 0.5)
        return z
    else:
        print "Some error"
    
try:
    x = raw_input("Enter rate pay: ")
    x_flt = float(x)
    y = raw_input("Enter Hours worked: ")
    y_flt = float(y)
except:
    print "Enter a number next time please"
    quit()
        
ans = overtime(x_flt,y_flt)
print "Your pay is %r" % ans
    
            
    
