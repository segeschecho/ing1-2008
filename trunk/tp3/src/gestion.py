from creacion import *
#Excepciones varias
class ProductosVacios(Exception):    
    def __str__(self):
        return "Lista de productos vacia"

class PedidoNulo(Exception):
    
    def __str__(self):
        return "Pedido nulo"


class CoordinadorDePedidos :

    def __init__(self,generadorDePedidos, controladorDePreIngreso,
        controladorDeListos):
        self.generadorDePedidos=generadorDePedidos
        self.controladorDeListos=controladorDeListos
        self.controladorDePreIngreso=controladorDePreIngreso

   
    
    def agregarPedidoListo(self, p):
           self.controladorDeListos.agregarPedidoListo(p)


    #Recibe una solicitud de ingresar un pedido. Ordena crearlo, y ordena
    #al controlador de pre ingreso que decida que hacer con el pedido
    def ingresarPedido(self, c,productos,formaDePago, origen,mesa):

         if(len(productos)==0):
             raise ProductosVacios         
         p = self.generadorDePedidos.generarPedido(c, productos, formaDePago, origen,mesa)
         if(p != None):
            self.controladorDePreIngreso.ingresar(p)
         else:
             raise PedidoNulo
         

    #getters y setters varios
    def getGeneradorDePedidos(self) :
        return self.generadorDePedidos


    def setGeneradorDePedidos(self, generadorDePedidos) :
        self.generadorDePedidos = generadorDePedidos


    def getControladorDePreIngreso(self) :
        return self.controladorDePreIngreso


    def setControladorDePreIngreso(self,controladorDePreIngreso) :
        self.controladorDePreIngreso = controladorDePreIngreso


    def getControladorDeListos(self) :
        return self.controladorDeListos


    def setControladorDeListos(self, controladorDeListos) :
        self.controladorDeListos = controladorDeListos
        
    
class ControladorDeListos(Notificador):


    def __init__(self):
           self.listos = []
           super(ControladorDeListos,self).__init__()

    #Encola un pedido listo y notifica a sus observadores de eso
    def agregarPedidoListo(self, p):
            self.listos.append(p)
            p.setEstado(Estado.Listo)
            self.notificar()
    
    def getListos(self):
            return self.listos        


class ControladorDePreIngreso :

    def __init__(self,coordinadorDePedidos,controladorDeIngreso):
        self.controladorDeIngreso=controladorDeIngreso
        self.coordinadorDePedidos=coordinadorDePedidos

 
    #Toma un pedido y decide si el mismo tiene alguna parte
    #cocinable
    def determinarCocinable(self, p):
        productos = p.getProductos()
        res= False
        for pr in productos:
            tp=pr.getTipo()
            res=res or tp.getCocinable()
            if res:
                break
        
        return res


    #Analogo pero para preparable
    def determinarPreparable(self, p):
        productos = p.getProductos()
        res= False
        for pr in productos:
            tp=pr.getTipo()
            res=res or tp.getPreparable()
            if res:
                break
        
        return res


    #Decide si un pedido va a listos o va a la cola de ingreso
    def ingresar(self,p):
        if(self.determinarPreparable(p) or self.determinarCocinable(p)):
              self.controladorDeIngreso.ingresar(p)
        else:
              self.coordinadorDePedidos.agregarPedidoListo(p)
          

class ControladorDeIngreso(Notificador) :

    def __init__(self,coordinadorDeCocina):
        self.coordinadorDeCocina=coordinadorDeCocina
        self.listaIngreso=[] 
        super(ControladorDeIngreso,self).__init__()


    def encolarPedido(self,p):
        raise NotImplementedError
    
    def getIngresados(self):
        return self.listaIngreso
    
    def ingresar(self,p):
        raise NotImplementedError

    def listarPedidos(self):
        raise NotImplementedError
    
    
    def proximoPedido(self, tp):
        raise NotImplementedError
        

class ControladorDeIngresoStandard (ControladorDeIngreso) :


    def __init__(self,coordinadorDeCocina):
              super(ControladorDeIngresoStandard,self).__init__(coordinadorDeCocina)


    def encolarPedido(self, p):
        self.listaIngreso.append(p)

    #Intenta ingresar el pedido a la cocina, si no pued
    #lo encola
    def ingresar(self, p):
      res=self.coordinadorDeCocina.prepararPedido(p)
      if(not res):
          p.setEstado(Estado.Ingresado)
          self.encolarPedido(p)
          self.notificar()

      



    def listarPedidos(self):
        return self.listaIngreso

    #Busca en su cola si hay un pedido que contenga algun producto de tipo 
    #tp, si lo encuentra lo devuelve
    def proximoPedido(self, tp):
        ls = self.listaIngreso
        ped=None
        for pedActual in ls:        
            sirve=self.tieneTipo(pedActual, tp)
            if(sirve):
                ped=pedActual
                break
            

        if(ped != None):
           self.listaIngreso.remove(ped)
           self.notificar()
          
        return ped


    #Permite conocer si algun producto del pedido p tiene tipo tp
    def tieneTipo(self, p, tp):
        ls = p.getProductos()
        res=False
        for pr in ls:
            res=pr.getTipo()==tp
            if(res):
                break
        
        return res


