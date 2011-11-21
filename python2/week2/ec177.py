from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = input.read(input = open(from_file))

output = open(to_file, 'w')
output.write(indata)

output.close()
input.close()


