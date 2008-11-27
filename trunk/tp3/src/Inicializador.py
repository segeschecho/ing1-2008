from Cocina import *
from GestionDePedidos import *
from CreacionDePedidos import *
import pickle
class Sistema:
    def __init__(self,init=True,f=None):
        if(init):
            dic=self.cargarDiccionario(f)
            self.cargarInsumos(dic)
            self.cargarProductos(dic)
            self.cargarTipoProducto(dic)
            #self.cargarClientes(dic)
        #self.cargarPedidos()
        #ahora vamos a armar un fraccionador
        t = {}
        t[self.pizza]=1
        t[self.empanada]= 4
        frPizzero =  FraccionadorDeHorno(t)
        frEmpanadero =  FraccionadorDeHorno(t)
        #armamos 2 hornos
        hpizzero =  Horno(10,frPizzero)
        hempanadero =  Horno(10,frEmpanadero)
        # armamos los avisos
        avE =  AvisoEmpanadero(None)
        avP =  AvisoPizzero(None)
        #ahora los preparadores
        self.prepPizzero=  PreparadorEspecializado(avP)
        self.prepEmpanadero=  PreparadorEspecializado(avE)
        #coordinadorDeCocina
        dep=None
        self.coordC =  CoordinadorDeCocina(None,None,None)
        #Despachador
        dep =  DespachadorDePreparacionStandard(self.prepPizzero,self.prepEmpanadero,self.coordC,self.pizza,self.empanada)
        self.coordC.setDespachadorDePreparacion(dep)
        #controladorDeIngreso
        self.contIng =  ControladorDeIngresoStandard(self.coordC)
        self.coordC.setControladorDeIngreso(self.contIng)
        #controladorDelistos
        self.contList =  ControladorDeListos()
        #CoordinadorDePedidos
        self.coordP =  CoordinadorDePedidos(None,None,self.contList)
        self.coordC.setCoordinadorDePedidos(self.coordP)
        #controladorDePreIngreso
        contPreIng =  ControladorDePreIngreso(self.coordP,self.contIng)
        self.coordP.setControladorDePreIngreso(contPreIng)
        #CalculadorDePrecios
        calcP =  CalculadorDePreciosStandard()
        #AsignadorDeHorno
        asigH =  AsignadorDeHornoStandard(hpizzero,hempanadero,self.pizza,self.empanada)
        #EstimadorDeTiempos
        estT =  EstimadorStandard(self.pizza,self.empanada)
        #ControladorDeStock
        contS =  ControladorDeStockStandard()
        #GenedarodDePedidos
        genP =  GeneradorDePedidosStandard(calcP,estT,contS,asigH)
        self.coordP.setGeneradorDePedidos(genP)
   
    def cargarInsumos(self,dic):
        self.insumos =dic["Insumos"]
    
    def cargarProductos(self,dic):
        self.productos=dic["Productos"]
    
    def cargarTipoProducto(self,dic):
        tipoproductos = dic['TiposProducto']
        self.pizza=tipoproductos['pizza']
        self.empanada=tipoproductos['empanada']
        self.coca=tipoproductos['coca']
        self.birra=tipoproductos['birra']
                
    def cargarClientes(self,dic):
        self.Clientes=dic["clientes"]
        
    def cargarDiccionario(self,f):
        dic=pickle.load(f)
        return dic
    
    def getContIng(self):
        return self.contIng
    
    def getContListos(self):
        return self.contListos
    
    def getCoordC(self):
        return self.coordC
        
    def getCoordP(self):
        return self.coordP
    
    def getPreparadorEmpanadero(self):
        return self.prepEmpanadero
    
    def getPreparadorPizzero(self):
        return self.prepPizzero
        
        
fi=open("datos.txt", 'rb')        
sis = Sistema(f=fi)