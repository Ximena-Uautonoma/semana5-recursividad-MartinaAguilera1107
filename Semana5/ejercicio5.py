def factorial1(numero):
    while numero != 0:
        return numero * factorial1(numero-1)
    return 1
def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero-1)
print(factorial1(4))
print(factorial(4))
