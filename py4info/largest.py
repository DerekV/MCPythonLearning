largest = -1
print 'Before', largest
for value in [3,41,12,9,74,15]:
    if value > largest:
        largest = value
    print largest, value
    
print 'After', largest
