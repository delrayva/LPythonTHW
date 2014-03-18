def TheLoop(Max):
    i = 0
    numbers = []

    while i < Max:
        numbers.append(i)
        i += 1
        print "Numbers now: ", numbers
        print "Control: ", i
    print "The numbers: ", numbers

TheLoop(int(raw_input("> ")))

