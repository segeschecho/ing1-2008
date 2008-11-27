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

dicc = {'Insumos':Insumo.allInstances(),'Productos':Producto.allInstances(),'TiposProducto':{'pizza':pizza,'empanada':empanada,'coca':coca,'birra':birra}}
pickle.dump(dicc, open('datos.txt', 'wb'))


