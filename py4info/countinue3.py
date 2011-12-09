while True:
    line = raw_input('>')
    if line[0] == '#':
        continue
    if line == 'Done':
        break
    print line
print 'Done!!!'
