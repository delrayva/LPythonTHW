from sys import argv

script, filename = argv

txt = open(filename)
start = txt.tell()

print "Here's your file %r:" % filename
print txt.read()

txt.seek(start)
line = txt.readline()
line = txt.readline()
print "The second line is:"
print line
txt.close()

