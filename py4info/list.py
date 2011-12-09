#write a prgram which reads lists of numbers until "done" is entered. Once "done" is entered, print out the total, count, and average of the numbers. If the user enters anythign other than an umber, print an error mesage and skip to the next number.



# Error message for not putting in a message. Below won't work because it stops... hard to put in list.
count = 0
total = 0
while True:
    UI = raw_input('Enter a number OR hit enter to finish: ')
    if UI == 'done': break
    if len(UI) < 1: break
    UI_flt = float(UI)
    print 'Your number was', UI_flt
    count = count + 1
    total = total + UI_flt
    
print 'You entered this many numbers =', count
print 'The sum of the numbers =', total
print 'The average is =', total/count
        
#for user_list in [UI]:
#    print 'Your list was was', user_list

# user input message

    #
# except

# Need to put user inputs in a list.



#if user enters done then print out the total, count and average

# total program here:
# total = 0
#   for list in [user input]:
#   total = list + total
# print 'The total is', total

# count program here:
# count = 0
# for list in [user input]:
#   count = list + 1
# print 'The count of numbers is', count

# average program here:
# average = total / count
# print 'The average of the numbers is', average


# print 

