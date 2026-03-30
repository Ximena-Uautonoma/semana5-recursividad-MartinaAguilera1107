"""
Ejercicio 1: Dado un número entero positivo N, retornar una lista con los números desde 1 hasta N.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""

def contar_ciclo(n):
    resultado = []
    i = 1
    while i <= n:
        resultado.append(i)
        i += 1
    return resultado
print(contar_ciclo(5))


def contar_recursivo(n):
    if n == 0:
        return []
    else:
        return [n] + contar_recursivo(n-1)
print(contar_recursivo(5))

