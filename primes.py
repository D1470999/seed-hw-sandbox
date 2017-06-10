# Prime Assignment

# Use either while or for loops

def isPrime(n):
    """
    Returns True if prime else False
    """
    prime = True
    # TODO: Implement isPrime
    return prime


for i in range(1, 101):
    for x in range(2, i - 1):
        if i % x == 0:
            print ("Not prime")
        else:
            print ("prime")


"""

Example of break:
i = 0
while True:
    print(i)
    i += 1
    if i > 1000:
        break

High Level Idea
37 is prime?
0 or 1 not prime
is 35 div by 2? yes - False
                no - not sure
    div by 3? yes - False
              no - not sure
    div by 4? no - not sure
    ...
    div by 36? no - prime!

Use % (mod) to check for divisibility
"""
for i in range(100):
    print("{}: {}".format(i,isPrime(i)))
