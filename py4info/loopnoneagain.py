smallest = None
for numbers in [10, 5, 100, 3, 1000, 1]:
    if smallest is None:
        smallest = numbers
    elif numbers < smallest:
        smallest = numbers
    print numbers, smallest
print 'Final', smallest
