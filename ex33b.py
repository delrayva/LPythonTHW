def TheLoop(Max, Step):
    i = 0
    numbers = []

    while i < Max:
        numbers.append(i)
        i += Step
        print "Numbers now: ", numbers
        print "Control: ", i
    print "The numbers: ", numbers
LoopTo = int(raw_input("Loop Until: "))
LoopStep = int(raw_input("Unit Step: "))
TheLoop(LoopTo, LoopStep)

