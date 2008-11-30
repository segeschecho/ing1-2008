from creacion import *

class Aviso :

    def __init__(self,despachadorDePreparacionStandard):
         self.destinatario = despachadorDePreparacionStandard

    def avisar(self):
        raise notImplementedError

    def getDestinatario(self) :
        return self.destinatario
   


    def setDestinatario(self,despachadorDePreparacionStandard) :
        self.destinatario = despachadorDePreparacionStandard

class AvisoEmpanadero(Aviso) :

      def avisar(self) :
          self.destinatario.empanadasTerminadas()

class AvisoPizzero(Aviso) :
      
      def avisar(self) :
          self.destinatario.pizzasTerminadas()

class CoordinadorDeCocina :

    def __init__(self,controladorDeIngreso, coordinadorDePedidos,
                 despachadorDePreparacion,despachadorDeCoccion):
        self.controladorDeIngreso=controladorDeIngreso
        self.coordinadorDePedidos=coordinadorDePedidos
        self.despachadorDePreparacion=despachadorDePreparacion
        self.despachadorDeCoccion = despachadorDeCoccion


    def cocinar(self, p):
              p.setEstado(Estado.Preparado)
              self.despachadorDeCoccion.cocinar(p)
              #no hace nada porque no hay que implementar la parte de la coccion


    def conseguirPedido(self,tp):
        return self.controladorDeIngreso.proximoPedido(tp)


    
    def pedidoListo(self, p):
        raise NotImplementedError


    def prepararPedido(self, p):
        return self.despachadorDePreparacion.prepararPedido(p)




    def setControladorDeIngreso(self, controladorDeIngreso) :
        self.controladorDeIngreso = controladorDeIngreso




    def setCoordinadorDePedidos(self, coordinadorDePedidos) :
        self.coordinadorDePedidos = coordinadorDePedidos



    def setDespachadorDePreparacion(self, despachadorDePreparacion) :
        self.despachadorDePreparacion = despachadorDePreparacion
    
    def setDespachadorDeCoccion(self, despachadorDeCoccion) :
        self.despachadorDeCoccion = despachadorDeCoccion
    

class DespachadorDePreparacion(object) :
     def __init__(self, prepPizzero,prepEmPanadero,coordinador):
        self.prepEmpanadero=prepEmPanadero
        self.prepPizzero=prepPizzero
        self.coordinador=coordinador
        


     def prepararPedido(self, p):
         raise notImplementedError


class DespachadorDePreparacionStandard(DespachadorDePreparacion) :

    def __init__(self,prepPizzero, prepEmPanadero,coordinador, pizza, empanada):
        
        super(DespachadorDePreparacionStandard,self).__init__(prepPizzero,prepEmPanadero,coordinador)
        
        self.pizza=pizza
        self.empanada=empanada
        self.partesAPreparar={}
        self.colaEmp=[]
        self.colaPiz=[]
        self.pedidoPizzeroActual=None
        self.pedidoEmpanaderoActual=None




    def asignableEmpanadero(self,p):
        res=self.esEmpanadero(p) and not self.prepEmpanadero.getOcupado()
        if(res):
            if(self.esPizzero(p)):
                self.partesAPreparar[p]=2
                if(not self.prepPizzero.getOcupado()):
                    self.pedidoPizzeroActual=p
                    self.prepPizzero.preparar(self.getSubpedidoPizzero(p))
                    
                else:
                    self.colaPiz.append(p)
                

            
            else:
                self.partesAPreparar[p]= 1
            
            self.pedidoEmpanaderoActual=p
            p.setEstado(Estado.EnPreparacion)
            self.prepEmpanadero.preparar(self.getSubpedidoEmpanadero(p))
        
        return res


    
    def asignablePizzero(self, p):
        
        res=self.esPizzero(p) and not self.prepPizzero.getOcupado()
        if(res):
            if(self.esEmpanadero(p)):
                self.partesAPreparar[p]= 2
                self.colaEmp.append(p)
            
            else:
                self.partesAPreparar[p] =1
            
            self.pedidoPizzeroActual=p
            self.prepPizzero.preparar(self.getSubpedidoPizzero(p))
            p.setEstado(Estado.EnPreparacion)
        
        return res



    def empanadasTerminadas(self):
        p = self.pedidoEmpanaderoActual
        partes = self.partesAPreparar[p]
        partes=partes-1
        self.partesAPreparar[p] = partes
        if(partes == 0):
            self.coordinador.cocinar(p)
            del self.partesAPreparar[p]
            self.pedidoEmpanaderoActual=None
        
        if(not len(self.colaEmp)==0):
            p=self.colaEmp.pop(0)
            #colaEmp.remove(0)
        
        else:
            p=self.coordinador.conseguirPedido(self.empanada)
        
        if(p!= None):
            self.pedidoEmpanaderoActual = p
            p.setEstado(Estado.EnPreparacion)
            self.partesAPreparar[p]=1
 
            if self.esPizzero(p):
               self.partesAPreparar[p]=2
               self.colaPiz.append(p)
            self.prepEmpanadero.preparar(self.getSubpedidoEmpanadero(p))

    def esEmpanadero(self, p):
        ls = p.getProductos()
        for pr in ls:
            if(pr.getTipo() == self.empanada):
                return True
        return False


    
    def esPizzero(self, p):
        ls = p.getProductos()
        for pr in ls:
            if(pr.getTipo() == self.pizza):
                return True
        return False


    def getSubpedidoEmpanadero(self, p):
        ls = p.getProductos()
        res = []
        for pr in ls:
            if(pr.getTipo()==self.empanada):
                res.append(pr)
            
        
        return res


    def getSubpedidoPizzero(self, p):
        ls = p.getProductos()
        res = []
        for pr in ls:
            if(pr.getTipo()==self.pizza):
                res.append(pr)
            
        
        return res


    def pizzasTerminadas(self):
        p = self.pedidoPizzeroActual
        partes =self.partesAPreparar[p]
        partes=partes-1
        self.partesAPreparar[p] = partes
        if(partes == 0):
            self.coordinador.cocinar(p)
            del self.partesAPreparar[p]
            self.pedidoPizzeroActual=None
        print "me llamaron aca?"
        if(len(self.colaPiz)!=0):
            p=self.colaPiz.pop(0)
        
        else:
            p=self.coordinador.conseguirPedido(self.pizza)
        
        if(p!= None):
            self.pedidoPizzeroActual = p
            p.setEstado(Estado.EnPreparacion)
            self.partesAPreparar[p]=1
            if self.esEmpanadero(p):
               self.colaEmp.append(p)
               self.partesAPreparar[p]=2
            self.prepPizzero.preparar(self.getSubpedidoPizzero(p))



    def prepararPedido(self, p):
        if(self.asignableEmpanadero(p)):
            return True
        
        else:
            return self.asignablePizzero(p)
        
class Preparador(Notificador) :

     def __init__(self,aviso):
         self.aviso=aviso
         self.ocupado=False
         super(Preparador,self).__init__()

     def getOcupado(self):
         raise NotImplementedError

    
     def preparar(self, productos):
         raise NotImplementedError
         
     def terminar(self):
         raise NotImplementedError

class PreparadorEspecializado(Preparador) :

    def __init__(self, aviso) :
        super(PreparadorEspecializado,self).__init__(aviso)
        productosAPreparar = []


    
    def getOcupado(self) :
        return self.ocupado
    
    def getPreparar(self):
      return self.productosAPreparar

    def preparar(self, productos) :
        self.ocupado=True
        self.productosAPreparar=productos
        self.notificar()
        #print "notificar que hay que preparar"
        #TODO: la parte del notify

    def terminar(self) :
        self.ocupado=False
        self.productosAPreparar = []
        self.notificar()
        self.aviso.avisar() 

class DespachadorDeCoccion(Notificador):
    def __init__(self):
       super(DespachadorDeCoccion,self).__init__()
    def cocinar(self,pedido):
        raise NotImplementedError

class DespachadorDeCoccionNormal(DespachadorDeCoccion):
    def __init__(self,hornoP,hornoE):
       super(DespachadorDeCoccionNormal,self).__init__()
       self.colaEmp = []
       self.colaPizz=[]
       self.hornoP = hornoP
       self.hornoE = hornoE
   
    def cocinar(self,p):
       if p.getHorno() == self.hornoP: 
           self.colaPizz.append(p)
       elif p.getHorno() == self.hornoE:
           self.colaEmp.append(p)
       else:
           raise TypeError("horno indefinido: "+str(p.getHorno())+"\n el despachador tiene estos hornos:\n horno pizzero: "+\
                           str(self.hornoP) + "\n horno empanadero:" + str(self.hornoE))
       self.notificar()

    def getColaPizz(self):
        return self.colaPizz
 
    def getColaEmp(self):
        return self.colaEmp
       
