from sys import argv

script, from_file, to_file = argv
dest = open(to_file, 'w'); dest.write(open(from_file).read()); dest.close
