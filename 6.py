# x is the straight man, with a number inside.
x = "There are %d types of people." % 10
# defines a joke string
binary = "binary"
# defines a don't string
do_not = "don't"
# constructs string y with other strings.
y = "Those who know %s and those who %s." % (binary, do_not)

# prints line x
print x
# prints line y
print y

# prints line x inside another string.
print "I said: %r." % x
# prints line y inside another string
print "I also said: '%s'." %y

# evaluates the joke
hilarious = False
# defines a string that includes a formatting character
joke_evaluation = "Isn't that joke so funny?! %r"

# prints the joke evaluation
print joke_evaluation % hilarious

# defines string w
w = "This is the left side of ..."
# defines string e
e = "a string with a right side."

# prints a string that is the concatenation of w and e
print w + e

