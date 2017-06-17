# Question 1 - increment function
def increment(n):
    """
    Returns n plus 1
    """
    ans = n + 1
    return ans

# Question 2 - multiply function

def mul(a, b):
    """
    Returns product of a and b
    """
    return a * b



# Question 3 - min function
def min(a,b):
    """
    Returns min of a and b
    """
    if a > b:
        return b
    elif b > a:
        return a
    else:
        return none



# Question 4 - linear function
def eval_linfunc(A,b,x):
    """
    Return value of equation Ax+b
    """
    return A * x + b



# Question 5 - squares
def squares(n):
    """
    Print first n squares starting from 1
    squares(3):
        1
        4
        9
    """
    for i in range(1, n):
        ans = i ** 2
        i += 1
    return ans



# Question 6 - odd_sum
def odd_sum(n):
    """
    Returns the sum of the first n odd integers
    odd_sum(3) = 1 + 3 + 5
    """
    for i in range(1, n, 2):
        return i



# Question 7 - is prime
def is_prime(n):
    """
    Returns true if n is prime else false
    """
    if n == 1 or n == 0:
        return false
    for i in range(2, 0.5 * n):
        if n % i == 0:
            return false
        else:
            return true








def isPrime(n):
    """
    Returns True if prime else False
    """
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for x in range(3, int(n ** 0.5), 2):
        if n % x == 0:
            return False
    return True
