def complicated (a, b):
    return (a+b, a, b)


Total, First, Second  = complicated (3,2)

print "%r\n" *3 % (Total, First, Second),
