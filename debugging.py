## LECTURE CODE and some notes

def f(n):
    assert n >= 0
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer
 ##FACTORIAL RECURSIVE
def fact(n):
    assert n >=0
    if n<=1:
        return n
    else
    return n *fact(n-1)

def g(n):
    x = 0
    for i in range(n):
        for j in range(n):
            x += 1
    return x

def h(x):
    assert type(x) == int and x >= 0
    answer = 0
