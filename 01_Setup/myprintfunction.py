import sys as s

def priyanshuprint(*arg, sep=' ', end='\n'):
    output = ' '
    for i in arg:
        output = output + str(i)
        output = output + sep
    
    s.stdout.write(output)


priyanshuprint("hello hi")
     