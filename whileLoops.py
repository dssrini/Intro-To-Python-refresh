c = 0
while c < 5:
    print(c)
    c += 1
# Break
c = 0 
while c < 5:
    print(c)
    if c == 3:
        break
    c += 1
# Continue
c = 0 
while c < 5:
    c += 1
    if c == 3:
        continue
    print c

#Pass
a = 0 
while a < 5:
    a += 1
    if a == 3:
        pass
    print a