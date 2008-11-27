from datetime import datetime


class Pedido :
    allInst=[]

    def __init__( self,id, cliente, productos, formaDePago, fechaIngreso):
        self.id=id
        self.cliente=cliente
        self.productos=productos
        self.fechaIngreso=fechaIngreso
        self.__class__.allInst.append(self)
	


    @classmethod
    def allInstances(cls):
        return cls.allInst
	
	
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
	

    def __hash__(self):
        self.id.__hash__()

	
    def __cmp__(self,o):
        if(isinstance(o,self.__class__)):
            return self.id - o.id
        else:
            raise TypeError("error en cmp")  

    
    def __eq__(self,o):
        if(isinstance(o,self.__class__)):
            return self.id == o.id
        else:
            raise TypeError("error en eq")

class PedidoLocal(Pedido):

	def __init__(id, cliente,productos,formaDePago, fechaIngreso):
		super(PedidoLocal, self).__init__(self, id, cliente, productos, formaDePago, fechaIngreso)

class ClienteNulo(Exception):
    def __str__(self):
        return "excepcion de cliente nulo"

class PedidoRemoto (Pedido): 

	def __init__(id, cliente,productos,formaDePago,fechaIngreso):
		if(cliente == None):
			raise ClienteNulo
		super(PedidoRemoto, self).__init__( id, cliente, productos, formaDePago, fechaIngreso)
	

class PedidoMesa(PedidoLocal) :


    def __init__(self,id, cliente, productos,formaDePago,fechaIngreso,mesa):
	    super(PedidoMesa,self).__init__(id, cliente, productos, formaDePago, fechaIngreso)
	    self.mesa=mesa
	
	
    
    def getMesa(self):
         return self.mesa
	


    def setFormaDePago(formaDePago):
       self.formaDePago=formaDePago


class PedidoMostrador(PedidoLocal) :

	def __init__(self,id, cliente,productos,formaDePago,fechaIngreso):

		super(PedidoMostrador,self).__init__(id, cliente, productos, formaDePago, fechaIngreso)
	

class PedidoTelefono(PedidoRemoto) :

	def __init__(self,id, cliente,productos,formaDePago,fechaIngreso):

		super(PedidoTelefono,self).__init__(id, cliente, productos, formaDePago, fechaIngreso)

class AsignadorDeHorno:

    def __init__(self,p, e,pizza, empanada ):
          self.hornoP=p
          self.hornoE=e
          self.pizza=pizza
          self.empanada=empanada
          
    def asignarHorno(self,pedido):
        raise NotImplementedError
    

    
class AsignadorDeHornoStandard (AsignadorDeHorno):

        def  asignarHorno( self,pedido):
            empanadas=Fals
            pizzas = False
            ls = pedido.getProductos()
            h = None
            for pr in ls:
                pizzas = pizzas or pr.getTipo().equals(self.pizza)
                empanadas = empanadas or pr.getTipo().equals(self.empanada)
        
            if (pizzas and empanadas):
            	h=notificarHorno()
        
            elif (pizzas):
            	h=self.hornoP
        
            elif(empanadas):
                h=self.hornoE
        
            pedido.setHorno(h)
	

        def notificarHorno(self):
        	return None #TODO: hacer que se pida el horno por pantalla
	

class Horno:


	def getFraccionadorDeHorno(self):
		return self.fraccionadorDeHorno
	

	def __init__(self,cantModulos, fraccionadorDeHorno):
		self.cantModulos=cantModulos
		self.fraccionadorDeHorno=fraccionadorDeHorno



	def getCantModulos(self):
		return self.cantModulos
	

class FraccionadorDeHorno:


	def __init__(self,prodsXModulo):
		self.prodsXModulo=prodsXModulo

	def getProductosPorModulo(self,tipoProducto ):
		return prodsXModulo[tipoProducto]
	
class CalculadorDePrecios:

    def __init__(self):
            pass

    def calcularPrecio(self,pedido):
            raise NotImplementedError
    

class CalculadorDePreciosStandard (CalculadorDePrecios):

	def __init__(self):
	    pass

	def calcularPrecio(self,pedido):
		ls = pedido.getProductos()
		precio=0.0
		for pr in ls:
			precio+=pr.getPrecio()
		
		return precio


class EstimadorDeTiempos: 

    def __init__(self):
          pass
    

    def estimarTiempo(self,pedido):
         raise NotImplementedError

class Estado:
    Ingresado="ingresado"
    Preparado="Preparado"
    EnPreparacion="EnPreparacion" 
    

class EstimadorStandard (EstimadorDeTiempos):


	def __init__( self,pizza, empanada):
		self.pizza=pizza
		self.empanada=empanada

	def estimarTiempo( self,pedido):
		tiempoPreparacion=0.0
		tiempoCoccionPizzas=0.0
		tiempoCoccionEmpanadas=0.0
		h=pedido.getHorno()
		ls = Pedido.allInstances()
		for p in ls:
			tiempoPreparacion+=self.estimarTiempoDePreparacion(p)
			tiempoCoccionPizzas+=self.estimarTiempoDeCoccionPizzas(p, h)
			tiempoCoccionEmpanadas+=self.estimarTiempoDeCoccionEmpanadas(p, h)
		
		tiempoPreparacion+=estimarTiempoDePreparacionActual(pedido)
		tiempoCoccionPizzas+=estimarTiempoDeCoccionPizzasActual(pedido,h)
		tiempoCoccionEmpanadas+=estimarTiempoDeCoccionEmpanadasActual(pedido,h)
		modulos = h.getCantModulos()
		frac = h.getFraccionadorDeHorno()
		cantEmpanadas = frac.getProductosPorModulo(self.empanada)
		cantPizzas = frac.getProductosPorModulo(self.pizza)
		res = tiempoPreparacion+(tiempoCoccionPizzas/(cantPizzas*modulos))+(tiempoCoccionEmpanadas/(cantEmpanadas*modulos))
		return res

	

	def estimarTiempoDeCoccionEmpanadasActual(self,pedido,h) :
		ls = pedido.getProductos()
		res= 0.0
		for pr in ls:
			if(pr.getTipo().equals(self.pizza)):
				res+=pr.getTiempoCoccion()
			
		
		return res
	

	def estimarTiempoDeCoccionPizzasActual(self,pedido,h) :
		ls = pedido.getProductos()
		res= 0.0
		for pr in ls:
			if(pr.getTipo().equals(self.empanada)):
				res+=pr.getTiempoCoccion()
		
		return res
	

	def estimarTiempoDePreparacionActual(self,pedido) :
		ls = pedido.getProductos()
		res= 0.0
		for pr in ls:
			res+=pr.getTiempoPreparacion()
		return res
	

	def estimarTiempoDeCoccionEmpanadas(self,pedido,  horno):
		res=0.0
		if(pedido.getHorno() != horno):
			return res
		
		elif(pedido.getEstado()!= Estado.EnPreparacion and \
              pedido.getEstado() != Estado.Ingresado and \
              pedido.getEstado() != Estado.Preparado):
			return res
		
		else:
			return self.estimarTiempoDeCoccionEmpanadasActual(pedido,horno)
		
    
	def estimarTiempoDeCoccionPizzas(self,pedido,horno):
		res=0.0
		if(pedido.getHorno() != horno):
			return res
		elif(pedido.getEstado()!= Estado.EnPreparacion and\
                pedido.getEstado() != Estado.Ingresado and\
                pedido.getEstado() != Estado.Preparado):
			return res
		else:
			return self.estimarTiempoDeCoccionPizzasActual(pedido,horno)
		
	

	
	def estimarTiempoDePreparacion(self,  pedido):
		res=0.0
		if(pedido.getEstado()!= Estado.Ingresado):
			return res
		
		else:
			return self.estimarTiempoDePreparacionActual(pedido)
		

class Producto :

    allInst = []

    def __init__(self,nombre,precio, tiempoCoccion,tiempoPreparacion,tipoProducto, insumos):
                self.nombre =nombre
                self.insumos=insumos
                self.precio=precio
                self.tiempoCoccion=tiempoCoccion
                self.tiempoPreparacion=tiempoPreparacion
                self.tipoProducto=tipoProducto
                self.__class__.allInst.append(self)

	

	
    @classmethod
    def allInstances(cls):
        return cls.allInst
    
    def getNombre(self) :
        return self.nombre
	

    def getInsumos(self):
        return self.insumos
	

    def getPrecio(self):
        return self.precio
	
    def getPreparable(self):
        return self.tipoProducto.getPreparable()
	

    def getTiempoCoccion(self):
        return self.tiempoCoccion
	

    def getTiempoPreparacion(self):
        return self.tiempoPreparacion
	

    def getTipo(self):
	    return self.tipoProducto


class TipoProducto:

    def __init__(self,nombre, coc,prep):
        self.nombre=nombre
        self.cocinable=coc
        self.preparable=prep

    def getNombre(self) :
        return self.nombre
	

    def getCocinable(self):
        return self.cocinable
    
    def getPreparable(self):
        return self.preparable

    def __hash__(self):
        self.nombre.__hash__()


    def __cmp__(self,o):
        if(isinstance(o,self.__class__)):
            return self.nombre.__cmp__(o.nombre)
        else:
            raise TypeError("error en cmp de TipoProducto")  

    
    def __eq__(self,o):
        if(isinstance(o,self.__class__)):
            return self.nombre == o.nombre
        else:
            raise TypeError("error en eq de TipoProducto")
	
class Insumo :

    allInst = []
    
    def __init__(self,cant,cantCritica, nombre):
        self.cant=cant
        self.cantCritica=cantCritica
        self.nombre=nombre
        self.__class__.allInst.append(self)

    
    @classmethod
    def allInstances(cls):
        return cls.allInst
    
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
	
class GeneradorDePedidos :


    def __init__(self, calculadorDePrecios,estimadorDeTiempos,controladorDeStock,asignadorDeHorno):
        self.asignadorDeHorno=asignadorDeHorno
        self.calculadorDePrecios=calculadorDePrecios
        self.controladorDeStock=controladorDeStock
        self.estimadorDeTiempos=estimadorDeTiempos



    def generarId(self):
        raise NotImplementedError

    def generarPedido(self,cliente,productos,formaDePago,origen,mesa):
        raise NotImplementedError

class OrigenDesconocido(Exception):
    def __init__(self,origen):
        self.origen=origen
    def __str__(self):
	    return "excepcion de origen desconocido"+str(self.origen)

class GeneradorDePedidosStandard (GeneradorDePedidos) :
    def __init__(self,calculadorDePrecios,estimadorDeTiempos,controladorDeStock,asignadorDeHorno):
        super(GeneradorDePedidosStandard,self).__init__(calculadorDePrecios, estimadorDeTiempos,controladorDeStock, asignadorDeHorno)
        self.ultimoIdAsignado=0



    def getDateTime(self) :
        return datetime.now()

    def generarId(self):
        res=self.ultimoIdAsignado
        self.ultimoIdAsignado+=1
        return res


    def generarPedido(self, c,productos,formaDePago,origen,mesa):
        if(controladorDeStock.verificarEIngresar(productos)):
            d=self.getDateTime()
            ID = self.generarId()
            if(origen == "mostrador"):
                p= PedidoMostrador(ID,c,productos,formaDePago,d)
            
            elif(origen == "mesa"):
                p= PedidoMesa(ID,c,productos,formaDePago,d,mesa)
            elif(origen == "telefono"):
                if(c==null):
                    raise ClienteNulo
                p= PedidoTelefono(ID,c,productos,formaDePago,d)
            else:
                raise OrigenDesconocido(origen)
            
            self.asignadorDeHorno.asignarHorno(p)
            p.setTiempoEstimado(self.estimadorDeTiempos.estimarTiempo(p))
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
        return Calle


    def setCalle(self, calle) :
        self.Calle = calle


    def getDepartamento(self) :
        return self.Departamento


    def setDepartamento(self,departamento) :
        self.Departamento = departamento


    def getLocalidad(self) :
        return Localidad


    def setLocalidad(self, localidad) :
        self.Localidad = localidad


    def getNumero(self) :
        return self.Numero


    def setNumero(self, numero) :
        self.Numero = numero


class Cliente :

     allInst = []
     def Cliente(apel,celular,id, nombre,passWeb,telefono,web, dir):
        self.apellido=apel
        self.celular=celular
        self.id=id
        self.nombre=nombre
        self.passWeb=passWeb
        self.telefono=telefono
        self.usrweb=web
        self.dir=dir
        self.__class__.allInst.append(self)

	

	
     @classmethod
     def allInstances(cls):
        return cls.allInst


     def getApellido(self) :
	     return self.apellido


     def getNombre(self) :
	     return self.nombre


     def getId(self) :
	     return self.id


     def getPassWeb(self) :
	     return self.passWeb


     def getCelular(self) :
	     return self.celular


     def getDir(self) :
	     return self.dir


     def getTelefono(self) :
	     return self.telefono


     def getUsrweb(self) :
	     return self.usrweb

class ControladorDeStock : #antes era interface


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

class ProductoInsatisfacible(Exception):
    def __init__(self,pr):
        self.producto=pr
    def __str__(self):
	           return "excepcion de producto instatisfacible"+str(self.producto)


class ControladorDeStockStandard(ControladorDeStock) :

    def __init__(self):
            self.criticos = []

    def getCriticos(self) :
        return self.criticos


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
                reestablecerStockInsumos(yaDeCrementados)
                return False
            
        
        return True
	
    # arma una lista con los insumos que estaban en algun producto de los que se ingresaron y que estan
    #ahora en stock critico

    def obtenerCriticos(self, productos) :
		   self.criticos=[]
		   for pr in productos:
			   ls = pr.getInsumos()
			   for ins in ls:
				
				   if(ins.getCant() <= ins.getCantCritica()):
					   criticos.append(ins)
				
			
		


    def reestablecerStock(self, productos) :
	    for pr in productos:
		    reestablecerStockInsumos(pr.getInsumos())
		

	

    def reestablecerStockInsumos(self,insumos) :
	    for ins in insumos:
		    ins.setCant(ins.getCant()+1)
		
	
    def verificarEIngresar(self, productos) :
                posible=True
                yaDecrementados = []
                for pr in productos:
                        posible=self.ingresar(pr)
                        if(not posible):
                                reestablecerStock(yaDecrementados)
                                raise ProductoInsatisfacible(pr)
                        
                        else:
                                yaDecrementados.append(pr)
    
                obtenerCriticos(productos)
                if(self.criticos.size!=0):
                     raise NotImplementedError("aca hay que hacer un notify de prod insat")
                                #TODO:hacer la parte de los notify
                        
                
                return true
