large = 0
print 'Before', large

for number in [1,10,3]:
    if number > large:
        large = number
    print large, number
    
print 'After', large

