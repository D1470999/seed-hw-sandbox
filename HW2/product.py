

for i in range(1, 101):
    for x in range(2, i - 1):
        if i % x == 0:
            print ("Not prime")
        else:
            print ("prime")
    if i > 100:
        break
