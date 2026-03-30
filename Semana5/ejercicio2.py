"""
Ejercicio 2:
Dado un número entero positivo N, retornar la suma de los primeros N números.

Debe implementar:
- suma_ciclo(n)
- suma_recursiva(n)
"""

def suma_ciclo(n):
    lista = []
    while n > 0:
        lista.append(n)
        n -= 1
    return sum(lista)
print(suma_ciclo(10))


def suma_recursiva(n):
    if n == 0:
        return 0
    else:
        return n + suma_recursiva(n-1)
print(suma_recursiva(10))
