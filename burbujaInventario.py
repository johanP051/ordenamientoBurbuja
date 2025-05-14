#Desarrollar un algoritmo para un sistema de gestion de tienda en línea donde el mi_inventario de productos se almacena en un diccionario. Cada diccionario representa un producto con: nombre, precio y stock. El objetivo es ordenar los prodcutos por precio de menor a mayor usando el algoritmo de ordenamiento de burbuja para mostrar el catálogo organizado a los clientes.

#Se debe comparar j con j + 1, donde j + 1 > j;  quiere decir que se debe garantizar que j + 1 no sobre pase la logitud de la lista (n), por ende j + 1 = n
# j + 1 = n ;
# Despejando j:   j = n -1
# Ejemplo: [5, 3, 8, 1, 2] --> i=0: [3, 5, 8, 1, 2] --> i=1: [3, 5, 8, 1, 2] --> i=2: [3, 5, 1, 8, 2] --> i=3: [3, 5, 1, 8, 2];  el número mayor siempre que da al final, entonces a j se le puede también restar i al final para ignorar ese número mayor.  j = n - 1 - i

import os
import csv

def burbuja(lista, indices):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-1-i):
            if lista[indices[j+1]] < lista[indices[j]]:
                indices[j+1], indices[j] = indices[j], indices[j+1]

def crear_archivo_csv(contenido):
    while True:
        try:
            nombre_archivo = input("Inserte el nombre del archivo para crearlo, (no digite la extension): ")
        except Exception as e:
            print(e)
        
        if nombre_archivo.endswith(".csv"):
            pass
        else:
            print("Recuerda que la extensión del archivo debe ser .csv, la voy a cambiar :)")
            nombre_archivo = nombre_archivo + ".csv"
    os.system(f"touch {nombre_archivo}.{extension}")
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)

def main():
    inventario = {}
    valores_nombre = []
    valores_precio = []
    valores_cantidad = []

    contador = 0
    while True:
        try:
            nombre = input("\nInserte el nombre de la herramienta: ")
            precio = float(input("Inserte el precio del producto: "))
            cantidad = float(input("Inserte la cantidad en stock: "))
        except ValueError:
            print("\nVerifique que el nombre sea un string y las cantidades sean números")
            continue
        except Exception as e:
            print(f"\nOcurrió un error: {e.__class__.__name__} - {e}")
            break

        inventario["nombre_" + str(contador)] = nombre
        inventario["precio_" + str(contador)] = precio
        inventario["cantidad_" + str(contador)] = cantidad
        contador += 1

        valores_nombre.append(nombre)
        valores_precio.append(precio)
        valores_cantidad.append(cantidad)

        continuar = input("\n¿Desea agregar otro producto? (s/n): ").lower()
        if continuar != "s":
            break
        
    print(f"\nInventario inicial: {inventario}")

    opciones = {1: "Nombre", 2: "Precio", 3: "Cantidad"}
    print(f"\nTiene las siguientes opciones para el criterio de ordenamiento: {opciones}")
    opcion = int(input(f"\nSeleccione el criterio de ordenamiento: "))

    valores = [valores_nombre, valores_precio, valores_cantidad]
    ordenable = valores[opcion - 1]
    indices = list(range(len(ordenable)))

    burbuja(ordenable, indices)
    
    # lista = ["manzana", "pera"]
    # print(list(enumerate(lista)))

    inventario_ordenado = {}
    for posicion_inventario, indice_ordenado in enumerate(indices):
        inventario_ordenado[f"nombre_{posicion_inventario}"] = valores_nombre[indice_ordenado]
        inventario_ordenado[f"precio_{posicion_inventario}"] = valores_precio[indice_ordenado]
        inventario_ordenado[f"cantidad_{posicion_inventario}"] = valores_cantidad[indice_ordenado]

    print(f"\n\nInventario Ordenado:\n")
    items = list(inventario_ordenado.items())
    lista_de_diccionario = []
    contador = 0
    fila_diccionario = []
    for i in items:
        if i[0].endswith(str(contador)):
            fila_diccionario.append(i)

        else:
            contador += 1
            lista_de_diccionario.append(dict(fila_diccionario))
            fila_diccionario = []
            fila_diccionario.append(i)

    print(lista_de_diccionario)
    # crear_archivo(inventario_ordenado)

if __name__ == "__main__":
    main()