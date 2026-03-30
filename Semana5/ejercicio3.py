"""
Ejercicio 3:
Dado un número entero positivo N, calcular su factorial.

Debe implementar una versión iterativa y una recursiva.
"""
def factorial_ciclo(n):
    lista = []
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
        lista.append(resultado)
    return lista
print(factorial_ciclo(5))


def factorial_recursivo(n):
    lista = []
    resultado = 1
    if n == 1:
        return 1
    else:
        for i in range(1, n + 1):
            resultado *= i
            lista.append(resultado)
        return lista
print(factorial_recursivo(5))
