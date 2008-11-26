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
            print "no son del mismo tipo comop para hacer un cmp "
            raise  

    
    def __eq__(self,o):
        if(isinstance(o,self.__class__)):
            return self.id == o.id
        else:
            print "no son del mismo tipo como para hacer un eq"
            raise 


class PedidoLocal(Pedido):

	def PedidoLocal(id, cliente,productos,formaDePago, fechaIngreso):
		super(PedidoLocal, self).__init__(self, id, cliente, productos, formaDePago, fechaIngreso)

class PedidoRemoto (Pedido): 

	def PedidoRemoto(id, cliente,productos,formaDePago,fechaIngreso):
		super(PedidoRemoto, self).__init__( id, cliente, productos, formaDePago, fechaIngreso)
	



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
        	return null #TODO: hacer que se pida el horno por pantalla
	

class Horno:


	def getFraccionadorDeHorno(self):
		return self.fraccionadorDeHorno
	

	def __init__(self,cantModulos, fraccionadorDeHorno):
		self.cantModulos=cantModulos
		self.fraccionadorDeHorno=fraccionadorDeHorno



	def getCantModulos(self):
		return self.cantModulos
	

class FraccionadorDeHorno:


	def FraccionadorDeHorno(self,prodsXModulo):
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
		
		elif(pedido.getEstado()!= Estado.EnPreparacion and pedido.getEstado() != Estado.Ingresado and pedido.getEstado() != Estado.Preparado):
			return res
		
		else:
			return self.estimarTiempoDeCoccionEmpanadasActual(pedido,horno)
		
	
	def estimarTiempoDeCoccionPizzas(self,pedido,horno):
		res=0.0
		if(pedido.getHorno() != horno):
			return res
		
		elif(pedido.getEstado()!= Estado.EnPreparacion and pedido.getEstado() != Estado.Ingresado and pedido.getEstado() != Estado.Preparado):
			return res
		
		else:
			return self.estimarTiempoDeCoccionPizzasActual(pedido,horno)
		
	

	
	def estimarTiempoDePreparacion(self,  pedido):
		res=0.0
		if(pedido.getEstado()!= Estado.Ingresado):
			return res
		
		else:
			return self.estimarTiempoDePreparacionActual(pedido)
		

print "uhhh"


