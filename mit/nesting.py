# make a program that compares three different numbers to see which is greatest

first_number = raw_input('Enter the first number ')
second_number = raw_input('Enter the second number ')
third_number = raw_input('Enter the third number ')

first_number_int = int(first_number)
second_number_int = int(second_number)
third_number_int = int(third_number)

if first_number_int > second_number_int and first_number_int > third_number_int:
    print 'The greatest number is ', first_number_int
    if second_number_int > third_number_int:
        print 'The second greatest number is %r and the least is %r' % (second_number_int, third_number_int)


