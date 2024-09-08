'''
This function takes an integer n and returns the nth term of the Fibonacci sequence.
'''

mem = {0: 0, 1: 1} # Keeps track of values that have already been calculated (memoization).

def fib(n):
    # Base case.
    if n in mem:
        return mem[n]
    
    mem[n] = fib(n - 1) + fib(n - 2)
    return mem[n]

# Change the input values here.
input1 = 7

result = fib(input1)
print(result)