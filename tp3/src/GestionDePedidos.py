class ProductosVacios(Exception):
    
    def __str__(self):
        return "excepcion de lista de productos vacia"

class PedidoNulo(Exception):
    
    def __str__(self):
        return "Excepcion de Pedido nulo"

class CoordinadorDePedidos :

    def __init__(self,generadorDePedidos, controladorDePreIngreso,
        controladorDeListos):
        self.generadorDePedidos=generadorDePedidos
        self.controladorDeListos=controladorDeListos
        self.controladorDePreIngreso=controladorDePreIngreso


    
    def agregarPedidoListo(self, p):
           self.controladorDeListos.agregarPedidoListo(p)



    def ingresarPedido(self, c,productos,formaDePago, origen,mesa):
         if(productos.isEmpty()):
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
        
    
class ControladorDeListos :


    def __init__(self):
           self.listos = []


    def agregarPedidoListo(self, p):
            listos.append(p)
            print "notificar pedido listo"
            #TODO: aca hay q ue avisar que hay un pedido listo nuevo


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
            res=res or tp.getpreparable()
            if res:
                break
        
        return res


 
    def ingresar(p):
        if(self.determinarPreparable(p) or self.determinarCocinable(p)):
              self.controladorDeIngreso.ingresar(p)
        else:
              self.coordinadorDePedidos.agregarPedidoListo(p)
          

class ControladorDeIngreso :

    def __init__(self,coordinadorDeCocina):
        self.coordinadorDeCocina=coordinadorDeCocina
        self.listaIngreso=[] 


    def encolarPedido(self,p):
        raise NotImplementedError

    
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
      if(not res):
          p.setEstado(Estado.Ingresado)
          self.encolarPedido(p)
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
                print ("ACA hay que hacer un notify de prox pedido")
                #TODO: hacer un notify
            if(ped != None):
                break
            

        if(ped != None):
           self.listaIngreso.remove(ped)
        
        return ped



    def tieneTipo(self, p, tp):
        ls = p.getProductos()
        res=False
        for pr in ls:
            res=pr.getTipo().equals(tp)
            if(res):
                break
        
        return res


