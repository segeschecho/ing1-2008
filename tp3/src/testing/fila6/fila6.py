from inicializador import *
import pickle

fi = open("datos.pyp", 'rb')        
sis = Pizzeria(f=fi)
#print Producto.allInstances()
    
#ahora agrego pedidos y eso para darle un estado a la pizeria
clientes = sis.clientes
coordPed = sis.getCoordP()
productos = sis.productos

#pizzero
pizzero = sis.getPreparadorPizzero()

#clientes
cli0 = clientes[0] #pepe
cli1 = clientes[1] #fede
cli2 = clientes[2] #emi
cli3 = clientes[3] #sergio
cli4 = clientes[4] #nicolas

#productos 2, 3 y 4 son pizzas(emuzarella tiene stock 3 y critico 3, napolitana tiene 2 y stock crit 3, ambos insumos en estado critico)
pizza1 = productos[2]
pizza2 = productos[3]
pizza3 = productos[4]

#ingreso un par de pedidos que tengan pizzas, asi el preparador queda ocupado
#queda 1 insumo para muzzarella
coordPed.ingresarPedido(cli0, [pizza1, pizza2], None, "mesa", 1)
#lhay 0 insumos para pizzas napolitanas
coordPed.ingresarPedido(cli1, [pizza2], None, "mesa", 2)
coordPed.ingresarPedido(cli2, [pizza3, pizza3, pizza3], None, "mesa", 3)
#con esto hay 2 insumos con estado critico

dicc = {'Pizerria':[sis]}
pickle.dump(dicc, open('fila6.pyp', 'wb'))