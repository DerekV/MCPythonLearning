found = False
for i in [10, 9, 8, 7, 6, 5]:
    if i != 8:
        continue
    if i == 8:
        break
        found = True
    print found, i
print 'Yes, you You have a appointment at that time'
