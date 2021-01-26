def power(base,exp):
    if exp==1 :
        return base 
    return base * power(base,exp-1)

def multiplication(a,b):
    if b == 1:
        return a
    return a + multiplication(a,b-1)

def factorial(n):
    if n == 1:
        return n
    return n*(factorial(n-1))

def natural(n):
    if n == 0:
        return n
    natural(n-1)
    print(n, end= ' ')

def sum_of_digits(x):
    if x == 0:
        return x
    return x%10 + sum_of_digits(x//10)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

#print(multiplication(8,8))
#print(power(2,8))
#print(factorial(5))
#natural(8)
#print(sum_of_digits(654))
#print(fibonacci(9))