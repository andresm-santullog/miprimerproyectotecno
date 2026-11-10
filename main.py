# # quiero saber de una lista del 0 al 100, cual es par e impar
# lista = list(range(1001))
# even = []
# odd = []
# for numero in lista:
#     if numero % 2 == 0:
#         even.append(numero)
#     else:
#         odd.append(numero)

#para hacer una funcion que me devuelva los pares e impares, puedo hacer lo siguiente:
def pares_impares(lista):
    even = []
    odd = []
    for numero in lista:
        if numero % 2 == 0:
            even.append(numero)
        else:
            odd.append(numero)
    return even, odd

# ...correr esto devuelve la lista entera
# print("Números pares:", pares_impares(list(range(1001)))[0])
# print("Números impares:", pares_impares(list(range(1001)))[1])

if __name__ == "__main__":
    n = 1000
    pares, impares = pares_impares(list(range(n + 1)))
    print("Números pares:", pares[:5], "...")  # primeros 5 números pares
    print("Números impares:", impares[:5], "...")  # primeros 5 números impares
    print("Total de números pares:", len(pares))
    print("Total de números impares:", len(impares))
