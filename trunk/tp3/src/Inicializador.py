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
        prepPizzero=  PreparadorEspecializado(avP)
        prepEmpanadero=  PreparadorEspecializado(avE)
        #coordinadorDeCocina
        dep=None
        coordC =  CoordinadorDeCocina(None,None,None)
        #Despachador
        dep =  DespachadorDePreparacionStandard(prepPizzero,prepEmpanadero,coordC,self.pizza,self.empanada)
        coordC.setDespachadorDePreparacion(dep)
        #controladorDeIngreso
        contIng =  ControladorDeIngresoStandard(coordC)
        coordC.setControladorDeIngreso(contIng)
        #controladorDelistos
        contList =  ControladorDeListos()
        #CoordinadorDePedidos
        coordP =  CoordinadorDePedidos(None,None,contList)
        coordC.setCoordinadorDePedidos(coordP)
        #controladorDePreIngreso
        contPreIng =  ControladorDePreIngreso(coordP,contIng)
        coordP.setControladorDePreIngreso(contPreIng)
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
        coordP.setGeneradorDePedidos(genP)
   
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
fi=open("datos.txt", 'rb')        
sis = Sistema(f=fi)