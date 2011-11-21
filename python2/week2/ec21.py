def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return (a + b)
    
number1 = input("enter a number:")
number2 = input("enter another number:")
print "%d" % number1
print "%d" % number2

answer = add(number1, number2)
print ("The answer is: %d") % answer

print "Try another set of numbers"

another_number1 = input ("enter another number:")
another_number2 = input ("enter one more number:")

another_answer = add(another_number1, another_number2)
print ("This answer is: %d") % another_answer


#add(x + 5)

    
       
#(x, y) = raw_input("enter two numbers to add together:")
#addition = add(x, y)
#print ("Your numbers added together equal: %d") % addition
