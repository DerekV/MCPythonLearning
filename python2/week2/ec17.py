from sys import argv ; from os.path import exists ; script, from_file, to_file = argv ; from_data = open(from_file).read() ; to_data = open(to_file, 'w').write(from_data) ; to_data.close()
