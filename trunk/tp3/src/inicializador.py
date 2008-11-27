#!/usr/bin/python

from cocina import *
from gestion import *
from creacion import *

import pickle

class Pizzeria:
    def __init__(self, f=None):
        if not f is None:
            dic=self.cargarDiccionario(f)
            self.cargarInsumos(dic)
            self.cargarProductos(dic)
            self.cargarTipoProducto(dic)
            self.cargarClientes(dic)
        
        #ahora vamos a armar un fraccionador
        t = {}
        t[self.pizza]=1
        t[self.empanada]= 4
        frPizzero =  FraccionadorDeHorno(t)
        frEmpanadero =  FraccionadorDeHorno(t)
        #armamos 2 hornos
        self.hpizzero =  Horno(10,frPizzero)
        self.hempanadero =  Horno(10,frEmpanadero)
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
        asigH =  AsignadorDeHornoStandard(self.hpizzero,self.hempanadero,self.pizza,self.empanada)
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
        self.Clientes=dic["Clientes"]
        
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
        

if __name__ == '__main__':
            
    fi = open("datos.pyp", 'rb')        
    sis = Pizzeria(f=fi)
    print Producto.allInstances()
