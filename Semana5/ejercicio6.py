"""
Ejercicio 6:
Una tienda registra sus ventas diarias en una lista de números. Cada número representa el monto de ventas de un día.
Se solicita calcular el total de ventas acumuladas.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""

def total_ventas_ciclo(ventas):
    total = 0
    for i in ventas:
        total += i
    return total
ventas = [200, 3000, 400, 5]
print(total_ventas_ciclo(ventas))


def total_ventas_recursivo(ventas):
   if not ventas:
    return 0
   else:
    return ventas[0] +  total_ventas_recursivo(ventas[1:])
    
ventas = [100, 200, 150, 50]
print(total_ventas_recursivo(ventas)) 
