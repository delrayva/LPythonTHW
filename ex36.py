#! /usr/bin/env python

contents = ['Hydrogen', 'Helium', 'Neon', 'Argon', 'Xenon', 'Radon', 'Lead']
corridor = ['up', 'left', 'forward', 'back', 'right', 'down']

inventory = []
room = 0
verbose = True

while (not 'Xenon' in inventory) or (not 'Hydrogen' in inventory):
    print "You are in room %d" % room
    print "There are %s balloons in here" % contents[room]
    if verbose:
        print "You can go 'up', 'down', 'left', 'right', forward', or 'back'"
        print "You can also 'list' and 'take'"
        print "Say 'simple' to simplify these messages, or 'help' for help"
    
    action = raw_input("> ")
    
    if action == "simple":
        verbose = False
        print "Say 'verbose' to restore messages."
        
    elif action == "verbose":
        verbose = True
        print "Ok."
        
    elif action == "list":
        print inventory
        
    elif action == "help":
        print "You want to have both a Hydrogen and a Xenon balloon"
        
    elif action == "take":
        inventory.append(contents[room])
        print "You have taken a %s balloon" % contents [room]

    elif action in corridor:
        room = (room + 1 + corridor.index(action)) % len(contents)
        
    elif "pop" in action:
        print "Don't pop a balloon!"
        if(len(inventory)>0):
            inventory.pop()
        else:
            print "You don't even have a balloon, anyway."
        
    else:
        print "I don't know what that means. Don't pop a balloon."
        print "Say 'verbose' to restore messages."
    print '\n'
    
print "That's what we needed!", inventory
