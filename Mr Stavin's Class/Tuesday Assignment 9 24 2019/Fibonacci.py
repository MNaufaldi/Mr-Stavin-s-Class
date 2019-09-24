#Fibonacci sequence
# 0 1 1 2 3 5 8
def fibonacci(number):
    if number > 1:
        return fibonacci(number-1) + fibonacci(number-2)
    else:
        return number
print(fibonacci(8))