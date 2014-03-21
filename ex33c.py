def TheLoop(Max, Step):

    numbers = []
    for i in range(0, Max, Step):
        numbers.append(i)
        print "Numbers now: ", numbers
        print "Control: ", i
    print "The numbers: ", numbers


LoopTo = int(raw_input("Loop Until: "))
LoopStep = int(raw_input("Unit Step: "))
TheLoop(LoopTo, LoopStep)

