productos = {
    '8475HD': ['hp', 15.6, '8gb', 'dd', '1t', 'intel core i5', 'nvidia gtx1050'],
    '2175HD': ['lenovo', 14, '4gb', 'ssd', '512gb', 'intel core i5', 'nvidia gtx1050'],
    'JjfFHD': ['asus', 14, '16gb', 'ssd', '256gb', 'intel core i7', 'nvidia rtx2080ti'],
    'fgdxFHD': ['hp', 15.6, '8gb', 'dd', '1t', 'intel core i3', 'integrada'],
    'GF75HD': ['asus', 15.6, '8gb', 'dd', '1t', 'intel core i7', 'nvidia gtx1050'],
    '123FHD': ['lenovo', 14, '6gb', 'dd', '1t', 'amd ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8gb', 'dd', '1t', 'amd ryzen 7', 'nvidia gtx1050'],
    'UWU131HD': ['dell', 15.6, '8gb', 'dd', '1t', 'amd ryzen 3', 'nvidia gtx1050'],
    'FS1230HD': ['acer', 15.6, '4gb', 'ssd', '256gb', 'intel core i3', 'integrada']
}

stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1],
    'FS1230HD': [249990, 0]
}

def stock_marca(marca):
    total = 0
    for modelo in productos:
        if productos[modelo][0].lower() == marca.lower():
            total += stock[modelo][1]
    print("el stock es:", total)

def busqueda_precio(pmin, pmax):
    lista = []
    for modelo in stock:
        precio = stock[modelo][0]
        cantidad = stock[modelo][1]
        if precio >= pmin and precio <= pmax and cantidad > 0:
            marca = productos[modelo][0]
            lista.append(marca + "--" + modelo)
    if lista:
        lista.sort()
        print("los notebooks entre los precios consultados son:", lista)
    else:
        print("no hay notebooks en ese rango de precios.")

def actualizar_precio(modelo, precio_nuevo):
    if modelo in stock:
        stock[modelo][0] = precio_nuevo
        return True
    else:
        return False

opcion = ""
while opcion != "4":
    print("\n*** menu principal ***")
    print("1. stock marca.")
    print("2. busqueda por precio.")
    print("3. actualizar precio.")
    print("4. salir.")
    opcion = input("ingrese una opcion: ")

    if opcion == "1":
        marca = input("ingrese la marca a consultar: ")
        stock_marca(marca)

    elif opcion == "2":
        while True:
            try:
                minimo = int(input("ingrese el precio minimo: "))
                maximo = int(input("ingrese el precio maximo: "))
                break
            except:
                print("debe ingresar valores enteros")
        busqueda_precio(minimo, maximo)

    elif opcion == "3":
        seguir = "s"
        while seguir == "s":
            modelo = input("ingrese el modelo a actualizar: ")
            try:
                nuevo = int(input("ingrese el precio nuevo: "))
            except:
                print("debe ingresar un valor entero para el precio.")
                continue
            ok = actualizar_precio(modelo, nuevo)
            if ok:
                print("precio actualizado!!")
            else:
                print("el modelo no existe!!")
            seguir = input("desea actualizar otro precio (s/n)?: ").lower()

    elif opcion == "4":
        print("programa terminado.")

    else:
        print("debe seleccionar una opcion valida")



