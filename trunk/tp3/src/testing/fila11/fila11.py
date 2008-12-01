from inicializador import *

fi = open("datos.pyp", 'rb')        
sis = Pizzeria(f=fi)

clientes = sis.clientes
coordPed = sis.getCoordP()
productos = sis.productos

# clientes
pepe = clientes[0]

cocaCola = productos[0]
empanadaCarne = productos[6]

productosNuevoPedido = []
# una docena de empanadas de carne
for each in range(12):
    productosNuevoPedido.append(empanadaCarne)

# dos cocas
productosNuevoPedido.append(cocaCola)
productosNuevoPedido.append(cocaCola)

coordPed.ingresarPedido(pepe, productosNuevoPedido, "efectivo", "mostrador", 1)
