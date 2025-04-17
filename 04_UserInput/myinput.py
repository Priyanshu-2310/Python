import sys as s

def priinput(prompt = ''):
    print(prompt, end = '')
    return s.stdin.readline().rstrip()


b = priinput("enter your number = ")
print(b)
print(type(b))