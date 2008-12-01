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
for each in range(6):
    productosNuevoPedido.append(empanadaCarne)

# dos cocas
productosNuevoPedido.append(cocaCola)
productosNuevoPedido.append(cocaCola)

# el stock para las empanadas de carne es de: 20 kit de carne (critico 25), 50 tapas (critico 20)
# ingreso un pedido con empanadas asi el preparador queda ocupado
coordPed.ingresarPedido(pepe, productosNuevoPedido, "efectivo", "telefono", None)
# ingreso el pedido que estamos testeando
coordPed.ingresarPedido(None, productosNuevoPedido, "efectivo", "mostrador", None)
