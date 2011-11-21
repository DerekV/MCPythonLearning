a = raw_input('Enter an integer: ')
try:
	a=int(a)
except:
	print 'Please enter a valid integer'
	exit(1)
print 'You entered:', a
