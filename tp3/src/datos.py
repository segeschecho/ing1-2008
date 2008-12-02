from inicializador import *

import pickle

#Insumo(cantidad,cantidadCritica,nombre)

bollo = Insumo(30,10,"Bollo de Pizza")
tapa = Insumo(50,20,"Tapa de Empanada")
insumo1 = Insumo(10,3,"Kit Muzzarella")
insumo2 = Insumo(25,25,"Kit Empanada de Carne")
insumo3 = Insumo(13,13,"Kit Napolitana")
insumo4 = Insumo(100,10,"Kit Empanada de Pollo")
insumo5 = Insumo(10,11,"Kit Roquefort")
insumo6 = Insumo(12,12,"Botella de Quilmes")
insumo7 = Insumo(45,23,"Botella de Coca-Cola")
insumo8 = Insumo(0,12,"Botella de Iguana")
insumo9 = Insumo(22,23,"Botella de Pepsi")
insumo10 = Insumo(0,1,"Kit Calabresa")
insumo11 = Insumo(14,20,"Kit Empanada de humita")
insumo12 = Insumo(0,12,"Kit Empanada de atun")

#TipoProducto(Nombre,cocinable,preparabl)
pizza= TipoProducto("Pizza",True,True)
empanada= TipoProducto("Empanada",True,True)
coca=  TipoProducto("Gaseosa",False,False)
cerveza= TipoProducto("Cerveza",False,False)

#Producto(nombre,precio,tiempoCoccion,tiempoPreparacion,TipoProducto,insumos)

#bebidas
Bebida1 = Producto("Coca-Cola",5,0.0,0.0,coca,[insumo7]) #no critico
Bebida2 = Producto("Quilmes",7,0.0,0.0,cerveza,[insumo6]) #al limite de critico
Bebida3 = Producto("Pepsi Cola",5,0.0,0.0,coca,[insumo9]) # critico
Bebida2 = Producto("Iguana",7,0.0,0.0,cerveza,[insumo8]) # agotada

#pizzas
Pizza1 = Producto("Muzzarella",25,5.0,10.2,pizza,[bollo,insumo1]) #no critico
Pizza2 = Producto("Napolitana",30,5.4,12.3,pizza,[bollo,insumo3]) #al limite de critico
Pizza3 = Producto("Roquefort",40,7,15.0,pizza,[bollo,insumo5]) # critico
Pizza4 = Producto("Calabresa",40,7.1,15.0,pizza,[bollo,insumo10])#Agotada

#empanadas
Empanada1 = Producto("Pollo",3,10,11.0,empanada,[tapa,insumo4]) #No critico
Empanada2 = Producto("Carne",3,11,12.0,empanada,[tapa,insumo2]) #al limite de critico
Empanada3 = Producto("Humita",3,10,11.0,empanada,[tapa,insumo11]) #critico
Empanada4 = Producto("Atun",3,11,12.0,empanada,[tapa,insumo12]) #Agotada


dir1 = Direccion("Trinidad", "N/A", "tortuguitas", 123)
dir2 = Direccion("Los alamos", "N/A", "Wilde", 1465)
dir3 = Direccion("San Martin", "2do Piso", "Capital Federal", 3988)
dir4 = Direccion("Montaneses", "1er Piso", "Capital Federal", 345)
dir5 = Direccion("Oliden", "N/A", "Vicente Lopez", 3433)
dir6 = Direccion("Los Paraisos", "N/A", "Bursaco", 20)

cli1 = Cliente("Sainz Trapaga", 1555664488, 1, "Gonzalo", "hayQPaja", 48566633, "gomox", dir1)
cli2 = Cliente("Martinez", 1521356684, 2, "Federico", "estudiando", 46532233, "fedefly", dir2)
cli3 = Cliente("Gonzalez", 1523314655, 3, "Emiliano", "bartolo", 45632132, "emilio", dir3)
cli4 = Cliente("Gonzalez", 1532169788, 4, "Sergio", "lechuga", 45125398, "checho", dir4)
cli5 = Cliente("Rinaldi", 1564659777, 5, "Nicolas", "esteee", 46633221, "elcorrector", dir5)
cli6 = Cliente("D'arrigo", 1564521133, 6, "Sergio", "niato", 46632136, "jefetp", dir6)

dicc = {'Insumos':Insumo.allInstances(),'Productos':Producto.allInstances(),'TiposProducto':{'pizza':pizza,'empanada':empanada,'coca':coca,'birra':cerveza}, 'Clientes':[cli1,cli2,cli3,cli4,cli5,cli6]}
#guradamos el diccionario con los datos necesarios para cargar a la pizzeria

pickle.dump(dicc, open('datos.pyp', 'wb'))

pizzeria = Pizzeria(open('datos.pyp','rb'))
pizzeria.getCoordP().ingresarPedido(cli1,[Empanada1],"efectivo", "telefono",None)

pickle.dump(pizzeria,open('pizzeriaTesting','wb'))
