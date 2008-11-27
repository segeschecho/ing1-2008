from Inicializador import *
import pickle

bollo = Insumo(30,10,"Bollo")
tapa = Insumo(50,20,"Tapa")
insumo1 = Insumo(10,3,"Muzzarela")
insumo2 = Insumo(20,5,"kit carne")
insumo3 = Insumo(13,3,"Napolitana")
insumo4 = Insumo(20,10,"kit Pollo")
insumo5 = Insumo(10,1,"Roquefort")
insumo6 = Insumo(23,12,"Botella de Quilmes")
insumo7 = Insumo(45,23,"Botella de Coca")
pizza= TipoProducto("pizza",True,True)
empanada= TipoProducto("empanada",True,True)
coca=  TipoProducto("coca",False,False)
birra= TipoProducto("cerveza",False,False)
Producto1 = Producto("Coca cola",5,0.0,0.0,coca,[insumo7])
Producto2 = Producto("Quilmes",7,0.0,0.0,birra,[insumo6])
Producto3 = Producto("Pizza Muzzarella",25,5.0,10.2,pizza,[bollo,insumo1])
Producto4 = Producto("Pizza Napolitana",30,5.4,12.3,pizza,[bollo,insumo3])
Producto5 = Producto("Pizza Roquefort",40,7,15.0,pizza,[bollo,insumo5])
Producto6 = Producto("Empanada pollo",3,10,11.0,empanada,[tapa,insumo4])
Producto7 = Producto("Empanada carne",3,11,12.0,empanada,[tapa,insumo2])
dir1 = Direccion("Trinidad", "N/A", "tortuguitas", 123)
dir2 = Direccion("Los alamos", "N/A", "wilde", 1465)
dir3 = Direccion("San Martin", "2do Piso", "Capital Federal", 3988)
dir4 = Direccion("Montaneses", "1er Piso", "Capital Federal", 345)
dir5 = Direccion("Oliden", "N/A", "Vicente Lopez", 3433)
dir6 = Direccion("Los Paraisos", "N/A", "Bursaco", 20)

cli1 = Cliente("Botella", 1555664488, 1, "Pepe", "hola1234", 48566633, "pepito", dir1)
cli2 = Cliente("Martinez", 1521356684, 2, "Federico", "estudiando", 46532233, "fedefly", dir2)
cli3 = Cliente("Gonzalez", 1523314655, 3, "Emiliano", "bartolo", 45632132, "emilio", dir3)
cli4 = Cliente("Gonzalez", 1532169788, 4, "Sergio", "nada324", 45125398, "checho", dir4)
cli5 = Cliente("Rinaldi", 1564659777, 5, "Nicolas", "esteee", 46633221, "elcorrector", dir5)
cli6 = Cliente("D'arrigo", 1564521133, 6, "Sergio", "holaaa", 46632136, "jefetp", dir6)


dicc = {'Insumos':Insumo.allInstances(),'Productos':Producto.allInstances(),'TiposProducto':{'pizza':pizza,'empanada':empanada,'coca':coca,'birra':birra}, 'Clientes':[cli1,cli2,cli3,cli4,cli5,cli6]}
pickle.dump(dicc, open('datos.txt', 'wb'))


