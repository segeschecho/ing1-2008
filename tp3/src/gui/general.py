#!/usr/bin/env python
#! -*- encoding: utf-8 -*-
from config import *
import lista_ingreso
import lista_insumos
import lista_clientes
import lista_productos
import lista_ingreso
import lista_listos
import lista_empanadero
import lista_pizzero
import nuevo_pedido
import lista_horno_pizzero
import lista_horno_empanadero
import lista_todos

class DistribuidorCallbacks:
    def __init__(self,widgets,pizzeria):
        self.widgets = widgets
        self.pizzeria = pizzeria

    def terminarPreparacionPizzas(self):
        self.pizzeria.getPreparadorPizzero().terminar()
        lista_todos.recargar(self.widgets)
          
    def terminarPreparacionEmpanadas(self):
        self.pizzeria.getPreparadorEmpanadero().terminar()
        lista_todos.recargar(self.widgets)
 
    def modifStock(self):
        lista_insumos.recargar(self.widgets)
   
    def modifListos(self):
        print "se modifico la cola de listos"
        lista_listos.recargar(self.widgets,self.pizzeria.getContListos())
        lista_todos.recargar(self.widgets)
        print len(self.pizzeria.getContListos().observers)

    def modifIngreso(self):
        lista_ingreso.recargar(self.widgets,self.pizzeria.getContIng())
        lista_todos.recargar(self.widgets)
  
    def prepararEmpanadas(self):
        lista_empanadero.recargar(self.widgets,self.pizzeria.getPreparadorEmpanadero())
        lista_todos.recargar(self.widgets)
   
    def prepararPizzas(self):
        lista_pizzero.recargar(self.widgets,self.pizzeria.getPreparadorPizzero())
        lista_todos.recargar(self.widgets)

    def pedirHorno(self):
        return nuevo_pedido.pedirHorno(self.pizzeria.getHornoP(),self.pizzeria.getHornoE())
        
    def nuevosCriticos(self):
        nuevo_pedido.nuevosCriticos(self.pizzeria.getContStock())
  
    def modifHornoPizzero(self):
        lista_horno_pizzero.recargar(self.widgets,self.pizzeria.getDespachadorDeCoccion())

    def modifHornoEmpanadero(self):
        lista_horno_empanadero.recargar(self.widgets,self.pizzeria.getDespachadorDeCoccion())
 
    def cocinarEmpanadas(self):
        self.pizzeria.getDespachadorDeCoccion().terminarCoccionEmpanadera()
        lista_todos.recargar(self.widgets)
        
    def cocinarPizzas(self):
        self.pizzeria.getDespachadorDeCoccion().terminarCoccionPizzera()
        lista_todos.recargar(self.widgets)

    def recargarClientes(self):
        tv = self.widgets[LISTA_CLIENTES] 
        seleccion, iterador = tv.get_selection().get_selected()
        
        if iterador is None:
            lista_clientes.limpiar_datos(self.widgets)
        else:
            nombre_cliente = seleccion.get_value(iterador, 2)            
            lista_clientes.cargar_datos(self.widgets, nombre_cliente)

    def actualizarGui(self):
        self.modifStock()
        self.modifListos()
        self.modifIngreso()
        self.modifHornoPizzero()
        self.modifHornoEmpanadero()
        lista_pizzero.recargar(self.widgets,self.pizzeria.getPreparadorPizzero())
        lista_empanadero.recargar(self.widgets,self.pizzeria.getPreparadorEmpanadero())
        lista_todos.recargar(self.widgets)

 # --------------------------------------------- #
 # Funciones para iniciar y limpiar toda la GUI  #
 # ----------------------------------------------#

def iniciar(widgets):
        
    lista_ingreso.iniciar(widgets)
    lista_ingreso.iniciar_datos(widgets)
    lista_productos.iniciar(widgets)
    lista_insumos.iniciar(widgets)
    lista_clientes.iniciar(widgets)
    lista_listos.iniciar(widgets)
    lista_listos.iniciar_datos(widgets)
    lista_empanadero.iniciar(widgets)
    lista_pizzero.iniciar(widgets)
    lista_horno_empanadero.iniciar(widgets)
    lista_horno_pizzero.iniciar(widgets)
    lista_todos.iniciar(widgets)
    lista_todos.iniciar_datos(widgets)
 
def limpiar(widgets):
    lista_ingreso.limpiar(widgets)
    lista_ingreso.limpiar_datos(widgets)
    lista_productos.limpiar(widgets)
    lista_productos.limpiar_datos(widgets)
    lista_insumos.limpiar(widgets)
    lista_insumos.limpiar_datos(widgets)
    lista_listos.limpiar(widgets)
    lista_empanadero.limpiar(widgets)
    lista_pizzero.limpiar(widgets)
    lista_horno_empanadero.limpiar(widgets)
    lista_horno_pizzero.limpiar(widgets)
    lista_todos.limpiar(widgets)
    lista_todos.limpiar_datos(widgets)

def recargar(widgets):
    lista_ingreso.recargar(widgets)
    lista_productos.recargar(widgets)
    lista_insumos.recargar(widgets)
    lista_clientes.recargar(widgets)
    lista_listos.recargar(widgets)
    lista_empanadero.recargar(widgets)
    lista_pizzero.recargar(widgets)
    lista_horno_empanadero.recargar(widgets)
    lista_horno_pizzero.recargar(widgets)
    lista_todos.recargar(widgets)
