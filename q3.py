'''
This function takes an integer n and returns the nth term of the Fibonacci sequence.
'''

# Used to keep track of values that have already been calculated (memoization).
mem = {0: 0, 1: 1}

def fib(n):
    # Base case.
    # Also used for memoization by checking if value has already been calculated.
    if n in mem:
        return mem[n]

    # Recursively calculate fibonacci sequence.
    mem[n] = fib(n - 1) + fib(n - 2)
    return mem[n]

# Change the input values here.
input1 = 7

result = fib(input1)
print(result)