# Put your function here
def factorial(n):
    if n > 1 :
        n = n * factorial(n-1)
    elif n < 0 :
        n = "error"

    return n

# testing
num = 5
print(factorial(num))
