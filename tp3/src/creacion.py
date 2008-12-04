#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

from datetime import datetime
from sets import Set


#Excepciones varias
class ErrorDeIngreso(Exception):
    pass

class ClienteNulo(ErrorDeIngreso):
    pass

class PedidoDeMesaSinMesa(ErrorDeIngreso):
    pass

class OrigenDesconocido(Exception):
    def __init__(self,origen):
        self.origen=origen
    def __str__(self):
	    return "excepcion de origen desconocido"+str(self.origen)

class PedidoDeMostradorConMesa(ErrorDeIngreso):
    pass


class PedidoDeTelefonoConMesa(ErrorDeIngreso):
    pass


class TipoDePagoInvalido(ErrorDeIngreso):
    pass


class ProductoInsatisfacible(ErrorDeIngreso):
   pass

#Notificador: responsable de hacer callbacks 
class Notificador(object):
    def __init__(self):
        self.observers=[]
    
    def clearObservers(self):
        self.observers=[]

    def suscribir(self,callback):
        """
        @param callback: metodo que se ejecuta al hacer
         notify
        @type callback: metodo
        @return: void

        Asocia un nuevo callback al notificador
        """
        self.observers.append(callback)
    
    def desuscribir(self,callback): 
        self.observers.remove(callback)
    
    def notificar(self):
        for each in self.observers:
            each()
   
#Clase base de pedidos
class Pedido(object) :
    allInst=[]    
   
    #Permite obtener un pedido dado su id
    @classmethod
    def getPorId(cls,id):
        for each in cls.allInst:
            if each.id == id:
                return each
        raise ValueError("ID inválido!") 

    #Devuelve la lista con todas las instancias de Pedido
    @classmethod
    def allInstances(cls):
        return cls.allInst

    #Reseta allInst
    @classmethod
    def setAllInstances(cls,allInst):
         cls.allInst = allInst
    
    #Reinicia la lista de todas las instancias (Se usa para poder hacer un load desde archivo)
    @classmethod
    def reinit(cls):
        cls.allInst=[]

    def __init__( self,id, cliente, productos, formaDePago, fechaIngreso):
        
        if id in [x.getId() for x in self.__class__.allInst]:
            raise ValueError("Ya hay un pedido con ese ID!")
        
        self.id = id
        self.cliente = cliente
        self.productos = productos
        self.formaDePago = formaDePago
        self.fechaIngreso = fechaIngreso
        self.__class__.allInst.append(self)
        self.estado = None
        self.precio = None
        self.horno = None
        self.tiempoEstimado = None

    #Getters y setters varios	
    def getCliente(self):
        return self.cliente
	
    def getFechaIngreso(self):
        return self.fechaIngreso

    def getEstado(self) :
        return self.estado

    def setEstado(self, estadoP) :
        self.estado = estadoP

    def getFechaIngreso(self) :
        return self.fechaIngreso

    def setFechaIngreso(self, fechaIngreso) :
        self.fechaIngreso = fechaIngreso

    def getFormaDePago(self):
        return self.formaDePago

    def setFormaDePago(self, formaDePago) :
        self.formaDePago = formaDePago

    def getHorno(self) :
        return self.horno

    def setHorno(self, horno) :
        self.horno = horno

    def getId(self) :
        return self.id

    def getProductos(self) :
        return self.productos

    def setProductos(self, productos) :
         self.productos = productos

    def setTiempoEstimado(self, tiempoEstimado) :
         self.tiempoEstimado = tiempoEstimado
	
    def getTiempoEstimado(self) :
         return self.tiempoEstimado

    def getPrecio(self) :
         return self.precio
	
    def setPrecio(self, precio) :
         self.precio = precio
	
 
    #Metodo que se invoca al unpicklear un pedido, nos permite ir asignando
    #a la lista de todas las instancias
    def __setstate__(self,dict):
        for k in dict.keys():
            setattr(self, k,dict[k])
        self.__class__.allInst.append(self)

    #Funciones necesarias para poder usar un diccionario de pedidos
    def __hash__(self):
        return self.id.__hash__()
    
    def __eq__(self,o):
        if o == None:
            return False

        if isinstance(o,self.__class__):
            return self.id == o.id
        else:
            raise TypeError("No se puede comparar con %s!" % o.__class__)

    def __neq__(self,o):
        return not self.__eq__(o)


    #Funcion que dice el destion, es decir si es delivery, mesa, o mostrador
    #Pedido no la implementa, es responsabilidad de las subclases
    def getDestino(self):
        raise NotImplementedError



#Otros sabores de pedido
class PedidoLocal(Pedido):
       
	def __init__(self,id, cliente,productos,formaDePago, fechaIngreso):
		super(PedidoLocal, self).__init__(id, cliente, productos, formaDePago, fechaIngreso)



class PedidoRemoto (Pedido): 
        def getDestino(self):
            return "Delivery"

	def __init__(self,id, cliente,productos,formaDePago,fechaIngreso):
		if(cliente == None):
			raise ClienteNulo("Los pedidos remotos deben tener un cliente asignado")
                
		super(PedidoRemoto, self).__init__( id, cliente, productos, formaDePago, fechaIngreso)



class PedidoMesa(PedidoLocal):

    def __init__(self,id, cliente, productos,formaDePago,fechaIngreso,mesa):
        if mesa is None:
            raise PedidoDeMesaSinMesa("Los pedidos de mesa deben tener una mesa asignade")
	    
        super(PedidoMesa,self).__init__(id, cliente, productos, formaDePago, fechaIngreso)
        self.mesa = mesa
	

    def getDestino(self):
        return "Mesa"
    
    def getMesa(self):
        return self.mesa




class PedidoMostrador(PedidoLocal) :

	def __init__(self,id, cliente,productos,formaDePago,fechaIngreso):
		super(PedidoMostrador,self).__init__(id, cliente, productos, formaDePago, fechaIngreso)

	def getDestino(self):
            return "Mostrador"

class PedidoTelefono(PedidoRemoto) :

	def __init__(self,id, cliente,productos,formaDePago,fechaIngreso):
		super(PedidoTelefono,self).__init__(id, cliente, productos, formaDePago, fechaIngreso)


#Responsable de asignar el horno al pedido, al momento de crearlo
class AsignadorDeHorno:

    def __init__(self,p, e,pizza, empanada ):
        self.hornoP = p
        self.hornoE = e
        self.pizza = pizza
        self.empanada = empanada
        self.oraculoDeHorno = None
          
    def asignarHorno(self,pedido):
        raise NotImplementedError
       
class AsignadorDeHornoStandard (AsignadorDeHorno):

    def asignarHorno(self, pedido):
        h = None
        empanadas = False
        pizzas = False
        ls = pedido.getProductos()
        for pr in ls:
            pizzas = pizzas or pr.getTipo() == self.pizza
            empanadas = empanadas or pr.getTipo() == self.empanada
    
        if pizzas and empanadas:
                #Pedido Mixto, hay que pedir el horno
        	h = self.notificarHorno()
        elif pizzas:
        	h = self.hornoP
        elif empanadas:
            h = self.hornoE
    
        pedido.setHorno(h)

    #Permite que se asigne el callback para pedir el horno	
    def asignarCallback(self,callback):
        self.oraculoDeHorno = callback
    
    def desasignarCallback(self):
        self.oraculoDeHorno = None

    #Ejecuta el callback para pedir el horno 
    def notificarHorno(self):
        return self.oraculoDeHorno()
        
class Horno:

    def __init__(self,cantModulos, fraccionadorDeHorno,descripcion):
        self.cantModulos = cantModulos
        self.fraccionadorDeHorno = fraccionadorDeHorno
        self.descripcion = descripcion

    def getFraccionadorDeHorno(self):
        return self.fraccionadorDeHorno

    def getCantModulos(self):
        return self.cantModulos
	
    def getDescripcion(self):
        return self.descripcion


class FraccionadorDeHorno:

    def __init__(self,prodsXModulo):
        self.prodsXModulo = prodsXModulo

    def getProductosPorModulo(self, tipoProducto):
        return self.prodsXModulo[tipoProducto]

class CalculadorDePrecios:

    def calcularPrecio(self,pedido):
            raise NotImplementedError
    

class CalculadorDePreciosStandard (CalculadorDePrecios):

    def calcularPrecio(self,pedido):
        #Recorremos los productos sumando los precios
        ls = pedido.getProductos()
        precio = 0.0
        for pr in ls:
            precio += pr.getPrecio()
		
        return precio

class EstimadorDeTiempos: 

    def estimarTiempo(self,pedido):
        raise NotImplementedError

#Simulacion de clase enumerada
class Estado:
    Ingresado="Ingresado"
    Preparado="Preparado"
    EnPreparacion="EnPreparacion" 
    Listo="Listo"


class EstimadorStandard (EstimadorDeTiempos):

    def __init__( self,pizza, empanada):
        self.pizza = pizza
        self.empanada = empanada

    def estimarTiempo(self,pedido):
        #Incializamos las variables
        tiempoPreparacion = 0.0
        tiempoCoccionPizzas = 0.0
        tiempoCoccionEmpanadas = 0.0
        h = pedido.getHorno()
        ls = Pedido.allInstances()
        #Calculamos los tiempos para todos los pedidos 
        for p in ls:
            tiempoPreparacion += self.estimarTiempoDePreparacion(p)
            tiempoCoccionPizzas += self.estimarTiempoDeCoccionPizzas(p, h)
            tiempoCoccionEmpanadas += self.estimarTiempoDeCoccionEmpanadas(p, h)
        #El pedido que se esta ingresando queda afuera ya que tiene estado None
        #Por eso sus tiempos los calculamos aparte		
        tiempoPreparacion += self.estimarTiempoDePreparacionActual(pedido)
        tiempoCoccionPizzas += self.estimarTiempoDeCoccionPizzasActual(pedido,h)
        tiempoCoccionEmpanadas += self.estimarTiempoDeCoccionEmpanadasActual(pedido,h)
        
        modulos = h.getCantModulos()
        frac = h.getFraccionadorDeHorno()
        cantEmpanadas = frac.getProductosPorModulo(self.empanada)
        cantPizzas = frac.getProductosPorModulo(self.pizza)
        #Efectuamos el calculo final
        res = tiempoPreparacion + \
              (tiempoCoccionPizzas / (cantPizzas*modulos))+ \
              (tiempoCoccionEmpanadas / (cantEmpanadas*modulos))
        
        return res

    #Estima el tiempo de coccion de las empanadas de un pedido
    def estimarTiempoDeCoccionEmpanadasActual(self,pedido,h) :
        ls = pedido.getProductos()
        res = 0.0
        for pr in ls:
            if pr.getTipo() ==self.empanada:
                res += pr.getTiempoCoccion()
        return res
	
    #Idem para las pizzas
    def estimarTiempoDeCoccionPizzasActual(self,pedido,h) :
        ls = pedido.getProductos()
        res = 0.0
        for pr in ls:
            if pr.getTipo() == self.pizza:
                res += pr.getTiempoCoccion()
        return res
	
    #Estima el tiempo de preparacion de un pedido
    def estimarTiempoDePreparacionActual(self,pedido) :
        ls = pedido.getProductos()
        res = 0.0
        for pr in ls:
            res += pr.getTiempoPreparacion()
        return res
	
    #Calcula el tiempo de coccion de las empanadas que estan en el mismo horno
    #que el pedido nuevo
    def estimarTiempoDeCoccionEmpanadas(self,pedido,  horno):
        res = 0.0
        if(pedido.getHorno() != horno):
            return res
		
        elif(pedido.getEstado() != Estado.EnPreparacion and \
             pedido.getEstado() != Estado.Ingresado and \
             pedido.getEstado() != Estado.Preparado):
            return res
		
        else:
            return self.estimarTiempoDeCoccionEmpanadasActual(pedido,horno)
		
    #Idem para las pizzas
    def estimarTiempoDeCoccionPizzas(self,pedido,horno):
        res = 0.0
        if(pedido.getHorno() != horno):
            return res
        elif(pedido.getEstado() != Estado.EnPreparacion and \
             pedido.getEstado() != Estado.Ingresado and \
             pedido.getEstado() != Estado.Preparado):
            return res
        else:
            return self.estimarTiempoDeCoccionPizzasActual(pedido,horno)
	
    #Calcula el tiempo de preparación de los pedidos que estan adelante
    #del nuevo
    def estimarTiempoDePreparacion(self,  pedido):
        res = 0.0
        if pedido.getEstado() != Estado.Ingresado or pedido.getEstado() != Estado.EnPreparacion:
            return res
        else:
            return self.estimarTiempoDePreparacionActual(pedido)

class Producto :

    allInst = []
    ID = 0
      
    def __init__(self,nombre,precio, tiempoCoccion,tiempoPreparacion,tipoProducto, insumos):
        self.nombre = nombre
        self.insumos = insumos
        self.precio = precio
        self.tiempoCoccion = tiempoCoccion
        self.tiempoPreparacion = tiempoPreparacion
        self.tipoProducto = tipoProducto
        self.__class__.allInst.append(self)
        self.ID = self.__class__.ID
        self.__class__.ID += 1

    #Simil a lo que pasaba con el pedido
    @classmethod
    def reinit(cls):
        cls.allInst=[]
        cls.ID=0
    
    @classmethod
    def setAllInstances(cls,allInst):
         cls.allInst = allInst

    @classmethod
    def getPorId(cls,ID):
        for each in cls.allInst:
            if each.ID == ID:
                return each
        raise ValueError("ID inválido!") 
   
    @classmethod
    def allInstances(cls):
        return cls.allInst
    
    #getters y setters
    def getId(self):
        return self.ID

    def getNombre(self) :
        return self.nombre

    def getInsumos(self):
        return self.insumos

    def getPrecio(self):
        return self.precio
	
    def getPreparable(self):
        return self.tipoProducto.getPreparable()
	
    def getCocinable(self):
        return self.tipoProducto.getCocinable()
    
    def getTiempoCoccion(self):
        return self.tiempoCoccion	

    def getTiempoPreparacion(self):
        return self.tiempoPreparacion

    def getTipo(self):
        return self.tipoProducto
 

    def __setstate__(self,dict):
        for k in dict.keys():
            setattr(self, k,dict[k])
        
        self.__class__.allInst.append(self)  
        self.ID = self.__class__.ID
        self.__class__.ID += 1

   
    def __repr__(self):
        return "<Producto nombre: " + self.nombre + ">"
        
    def __str__(self):
        return self.nombre
 

class TipoProducto:
    #Misma estrategia que para productos y pedidos
    allInst = []
    ID = 0
    @classmethod
    def reinit(cls):
        cls.allInst=[]
        cls.ID=0
    
    @classmethod
    def setAllInstances(cls,allInst):
         cls.allInst = allInst

    def __init__(self,nombre, coc,prep):
        self.nombre = nombre
        self.cocinable = coc
        self.preparable = prep
        self.__class__.allInst.append(self)  
        self.id = self.__class__.ID
        self.__class__.ID += 1


    def __setstate__(self,dict):
        for k in dict.keys():
            setattr(self, k,dict[k])

        self.__class__.allInst.append(self)  
        self.id = self.__class__.ID
        self.__class__.ID += 1

    
    @classmethod
    def getPorId(cls,ID):
        for each in cls.allInst:
            if each.id == ID:
                return each
        raise TypeError("ID invalido!") 
   
    @classmethod
    def allInstances(cls):
        return cls.allInst
    
    def __hash__(self):
        return self.nombre.__hash__()


    def __cmp__(self,o):
        if o == None:
            return False
        if isinstance(o,self.__class__):
            return self.nombre.__cmp__(o.nombre)
        else:
            raise TypeError("error en cmp de TipoProducto")  

    
    def __eq__(self,o):
        if isinstance(o,self.__class__):
            return self.nombre == o.nombre
        else:
            raise TypeError("error en eq de TipoProducto")

    def __neq__(self,o):
        return not self.__eq__(o)

    def __repr__(self):
        return "<TipoProducto: %s, preparable: %s, cocinable: %s>" % (self.nombre,self.preparable,self.cocinable)


    def getNombre(self) :
        return self.nombre
	
    def getId(self):
      return self.id
    
    def getCocinable(self):
        return self.cocinable
    
    def getPreparable(self):
        return self.preparable

class Insumo :
     
    def __setstate__(self,dict):
      self.cant=dict['cant']
      self.cantCritica=dict['cantCritica']
      self.nombre=dict['nombre']
      self.ID = dict['ID']
      self.__class__.allInst.append(self) 
      self.ID = self.__class__.ID
      self.__class__.ID+=1

    @classmethod
    def reinit(cls):
        cls.allInst=[]
        cls.ID=0
 
    @classmethod
    def setAllInstances(cls,allInst):
         cls.allInst = allInst
    
    allInst = []
    ID=0
    def __str__(self):
        return "soy el insumo:" + self.nombre + " y mi cantidad actual es: " + str(self.cant) +" y mi cantidad critica es: " + str(self.cantCritica)
        
    def __init__(self,cant,cantCritica, nombre):
        self.cant=cant
        self.cantCritica=cantCritica
        self.nombre=nombre
        self.__class__.allInst.append(self)
        self.ID = self.__class__.ID
        self.__class__.ID+=1

    def getId(self):
       return self.ID
  
    @classmethod
    def allInstances(cls):
        return cls.allInst
    
    @classmethod
    def getPorId(cls,ID):
        for each in cls.allInst:
		if each.ID == ID:
                      return each
        raise TypeError("ID invalido") 

    def getCant(self) :
        return self.cant
    

    def getCantCritica(self) :
        return self.cantCritica
	

    def setCant(self,cant):
        self.cant = cant
	



    def getNombre(self) :
        return self.nombre
	

    def setNombre(self, nombre) :
        self.nombre = nombre
	

    def setCantCritica(self, cantCritica) :
	    self.cantCritica = cantCritica

	
class GeneradorDePedidos(object) :


    def __init__(self, calculadorDePrecios,estimadorDeTiempos,controladorDeStock,asignadorDeHorno):
        self.asignadorDeHorno=asignadorDeHorno
        self.calculadorDePrecios=calculadorDePrecios
        self.controladorDeStock=controladorDeStock
        self.estimadorDeTiempos=estimadorDeTiempos

    #Metodo para generar ID de pedidos
    def generarId(self):
        raise NotImplementedError

    #Crea un pedido, es un factory method
    def generarPedido(self,cliente,productos,formaDePago,origen,mesa):
        raise NotImplementedError


    
class GeneradorDePedidosStandard (GeneradorDePedidos) :
    
    def __init__(self,calculadorDePrecios,estimadorDeTiempos,controladorDeStock,asignadorDeHorno):
        super(GeneradorDePedidosStandard,self).__init__(calculadorDePrecios, estimadorDeTiempos,controladorDeStock, asignadorDeHorno)
        self.ultimoIdAsignado=0

    #Obtiene la fecha actual para "grabarsela" al pedido
    def getDateTime(self) :
        return datetime.now()
    
    #Estrategia simple de creación de pedido
    def generarId(self):
        res=self.ultimoIdAsignado
        self.ultimoIdAsignado+=1
        return res
                    

    def generarPedido(self, c,productos,formaDePago,origen,mesa):
        #Primero intentamos ingresarlo, reservando los recursos
        if(self.controladorDeStock.verificarEIngresar(productos)):
            d=self.getDateTime()
            #Decidimos a partir del origen a partir del nombre (pobre OCP y Liskov)
            if(origen == "mostrador"):
                #Chequeamos invariantes para construir un pedido de mostrador
                if not formaDePago in ["efectivo","tarjeta"]:
	            self.controladorDeStock.reponerStock(productos)
                    raise TipoDePagoInvalido("Forma de pago Invalida\nSe intento asignar la forma de pago: "+str(formaDePago)+" a un pedido con origen: "+str(origen))
                if mesa != None:
                    self.controladorDeStock.reponerStock(productos)
		    raise PedidoDeMostradorConMesa("Los pedidos de mostrador no tienen que tener una mesa asignada")
                ID = self.generarId()
                p= PedidoMostrador(ID,c,productos,formaDePago,d)
             
            elif(origen == "mesa"):
                #Simil con pedido de mesa
                if formaDePago != None :
		    self.controladorDeStock.reponerStock(productos)
                    raise TipoDePagoInvalido("Forma de pago Invalida\nSe intento asignar la forma de pago: "+str(formaDePago)+" a un pedido con origen: "+str(origen))
                ID = self.generarId()
                p= PedidoMesa(ID,c,productos,formaDePago,d,mesa)
         
            elif(origen == "telefono"):
                #Idem para pedido telefonico
                if formaDePago != "efectivo" :
		    self.controladorDeStock.reponerStock(productos)
                    raise TipoDePagoInvalido("Forma de pago Invalida\nSe intento asignar la forma de pago: "+str(formaDePago)+" a un pedido con origen: "+str(origen))
                if mesa != None:
		    self.controladorDeStock.reponerStock(productos)
                    raise PedidoTelefonicoConMesa("Los pedidos telefonicos no tienen que tener una mesa asignada")
                if(c==None):
		    self.controladorDeStock.reponerStock(productos)
                    raise ClienteNulo("Los pedidos remotos deben tener un cliente asociado")
                ID = self.generarId()
                p= PedidoTelefono(ID,c,productos,formaDePago,d)
            else:
		self.controladorDeStock.reponerStock(productos)
                raise OrigenDesconocido("El origen indicado no es valido")
            #Asignamos el horno
            self.asignadorDeHorno.asignarHorno(p)
            if p.getHorno() != None:
                 #Si tiene un horno, no es de solo bebida, tiene sentido estimar el tiempo 
                 p.setTiempoEstimado(self.estimadorDeTiempos.estimarTiempo(p))
            else:
                p.setTiempoEstimado(0)
            #Finalmente calculamos el precio
            p.setPrecio(self.calculadorDePrecios.calcularPrecio(p))
            return p
        
        return None

class Direccion :

    def __init__(self,calle,departamento,localidad,numero) :
        self.Calle = calle
        self.Departamento = departamento
        self.Localidad = localidad
        self.Numero = numero


    def getCalle(self) :
        return self.Calle


    def setCalle(self, calle) :
        self.Calle = calle


    def getDepartamento(self) :
        return self.Departamento


    def setDepartamento(self,departamento) :
        self.Departamento = departamento


    def getLocalidad(self) :
        return self.Localidad


    def setLocalidad(self, localidad) :
        self.Localidad = localidad


    def getNumero(self) :
        return self.Numero


    def setNumero(self, numero) :
        self.Numero = numero


class Cliente :
     #Metodos para unpicklear
     def __setstate__(self,dict):
        for k in dict.keys():
            setattr(self, k,dict[k])
        self.__class__.allInst.append(self) 
        self.ID = self.__class__.ID
        self.__class__.ID+=1
        
     @classmethod
     def reinit(cls):
        cls.allInst=[]
        cls.ID=0

     @classmethod
     def setAllInstances(cls,allInst):
         cls.allInst = allInst

     ID=0  
     allInst = []
     def __init__(self,apel,celular,id, nombre,passWeb,telefono,web, dir):
        self.apellido=apel
        self.celular=celular
        self.id=id
        self.nombre=nombre
        self.passWeb=passWeb
        self.telefono=telefono
        self.usrweb=web
        self.dir=dir
        self.__class__.allInst.append(self)
        self.ID = self.__class__.ID
        self.__class__.ID+=1

     def getId(self):
         return self.ID
     
  
     def __str__(self):  
         return "el cliente es:" + self.nombre + " " + self.apellido + " con Id: " +\
                 str(self.ID) + " y nombre de usuario WEB: " + self.usrweb

     @classmethod
     def getPorId(cls,ID):
        for each in cls.allInst:
		if each.ID == ID:
                      return each
        raise TypeError("ID invalido") 
	
     @classmethod
     def allInstances(cls):
        return cls.allInst
     
     def getDireccion(self):
        return self.dir


     def getApellido(self) :
	     return self.apellido


     def getNombre(self) :
	     return self.nombre


     def getId(self) :
	     return self.ID


     def getPassWeb(self) :
	     return self.passWeb


     def getCelular(self) :
	     return self.celular


     def getDir(self) :
	     return self.dir


     def getTelefono(self) :
	     return self.telefono


     def getUsrWeb(self) :
	     return self.usrweb

class ControladorDeStock(Notificador) : #antes era interface
    
    def __init__(self):
        super(ControladorDeStock,self).__init__()

    def ingresar(self,producto):
        raise NotImplementedError


    def obtenerCriticos(self, productos):
        raise NotImplementedError


    def reestablecerStock(self, productos):
        raise NotImplementedError

    def reestablecerStockInsumos(self, insumos):
        raise NotImplementedError
    
    def verificarEIngresar(self, productos):
        raise NotImplementedError




class ControladorDeStockStandard(ControladorDeStock) :

    def __init__(self):
            super(ControladorDeStockStandard,self).__init__()
            self.criticos = Set([])

    def getCriticos(self) :
        return self.criticos

    #Decide si un producto se puede ingresar o no
    #Si no puede restauara el stock que modifico (rollback)
    def ingresar(self, producto) :
        ls = producto.getInsumos()
        yaDeCrementados = []
        cant=0
        for ins in ls:
            cant=ins.getCant()
            if(cant > 0):
                ins.setCant(cant-1)
                yaDeCrementados.append(ins)
            else:
                self.reestablecerStockInsumos(yaDeCrementados)
                return False
            
        
        return True
	
    # arma una lista con los insumos que estaban en algun producto de los que se ingresaron y que estan
    #ahora en stock critico
    def obtenerCriticos(self, productos) :
		   self.criticos=Set([])
		   for pr in productos:
			   ls = pr.getInsumos()
			   for ins in ls:
				
				   if(ins.getCant() < ins.getCantCritica()):
					   self.criticos.add(ins)
				
			
		
    #Restablece el stock de los insumo de una lista de productos
    def reestablecerStock(self, productos) :
	    for pr in productos:
		    self.reestablecerStockInsumos(pr.getInsumos())

    #Incrementa el stock de una lista de insumos
    def reestablecerStockInsumos(self,insumos) :
	    for ins in insumos:
		    ins.setCant(ins.getCant()+1)
		
    #Intenta ingresar un pedido, descontando el stock	
    def verificarEIngresar(self, productos) :
        posible = True
        yaDecrementados = []
        #Listamos los insumos que no estaban en estado critico (en verdad es conjunto, no lista)
        stockAnterior = Set([x for x in Insumo.allInstances() if x.getCant() >= x.getCantCritica()])
        for pr in productos:
            posible = self.ingresar(pr)
            if(not posible):
                #Uno de los productos no se pudo satisfacer
                #Restablecemos el stock de los que ya decrementamos, porque el pedido no se va a poder hacer
                self.reestablecerStock(yaDecrementados)
                #Tiramos una excepcion identificando que producto no se pudo ingresar
                raise ProductoInsatisfacible("No se pudo ingresar el producto: " + pr.getNombre() +"(Id: "+str(pr.getId()) + ")")
            else:
                yaDecrementados.append(pr)
              
        self.obtenerCriticos(productos)
        #Intersecamos los conjuntos para que en criticos queden los que pasaron de estado normal a critico
        self.criticos.intersection_update(stockAnterior)
        #Avisamos a los observadores que hubo cambios en el stock
        self.notificar()
                     
                        
                
        return True
	
    def reponerStock(self, productos):
        print "me llame"
        for pr in productos:
            for ins in pr.getInsumos():
                ins.setCant(ins.getCant() + 1)
 
