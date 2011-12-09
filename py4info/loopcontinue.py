for i in [1, 10, 100, 50, 25, 100000, 50300]:
    if i < 10:
        continue
    if i < 90:
        print 'these numbers are wusses: ', i
    if i > 1000:
        break
print 'This number is KINGGG!: ', i
