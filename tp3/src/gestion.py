from creacion import *

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



    def ingresarPedido(self, c,productos,formaDePago, origen,mesa):

         if(len(productos)==0):
             raise ProductosVacios         
         p = self.generadorDePedidos.generarPedido(c, productos, formaDePago, origen,mesa)
         if(p != None):
            self.controladorDePreIngreso.ingresar(p)
         else:
             raise PedidoNulo
         



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


    def agregarPedidoListo(self, p):
            self.listos.append(p)
            p.setEstado(Estado.Listo)
            self.notificar()
            print "notificar pedido listo"
    
    def getListos(self):
            return self.listos        


class ControladorDePreIngreso :

    def __init__(self,coordinadorDePedidos,controladorDeIngreso):
        self.controladorDeIngreso=controladorDeIngreso
        self.coordinadorDePedidos=coordinadorDePedidos



    def determinarCocinable(self, p):
        productos = p.getProductos()
        res= False
        for pr in productos:
            tp=pr.getTipo()
            res=res or tp.getCocinable()
            if res:
                break
        
        return res



    def determinarPreparable(self, p):
        productos = p.getProductos()
        res= False
        for pr in productos:
            tp=pr.getTipo()
            res=res or tp.getPreparable()
            if res:
                break
        
        return res


 
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


    def ingresar(self, p):
      res=self.coordinadorDeCocina.prepararPedido(p)
      print res
      if(not res):
          p.setEstado(Estado.Ingresado)
          self.encolarPedido(p)
          self.notificar()
          print "Aca hay que hacer un notify de ingreso"
          #TODO: hacer la parte del observer
      



    def listarPedidos(self):
        return self.listaIngreso


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
          
        print "ped:" + str(ped)
        return ped



    def tieneTipo(self, p, tp):
        ls = p.getProductos()
        res=False
        for pr in ls:
            res=pr.getTipo()==tp
            if(res):
                break
        
        return res


