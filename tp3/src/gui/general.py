#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

import lista_ingreso
import lista_insumos
import lista_clientes
import lista_productos
import lista_ingreso
import lista_listos
import lista_empanadero
import lista_pizzero

class DistribuidorCallbacks:
    def __init__(self,widgets,pizzeria):
        self.widgets = widgets
        self.pizzeria = pizzeria

    def terminarPreparacionPizzas(self):
        self.pizzeria.getPreparadorPizzero().terminar()
          
    def terminarPreparacionEmpanadas(self):
        self.pizzeria.getPreparadorEmpanadero().terminar()
 
    def modifStock(self):
        lista_insumos.recargar(self.widgets)
   
    def modifListos(self):
        lista_listos.recargar(self.widgets,self.pizzeria.getContListos())

    def modifIngreso(self):
        lista_ingreso.recargar(self.widgets,self.pizzeria.getContIng())
  
    def prepararEmpanadas(self):
        lista_empanadero.recargar(self.widgets,self.pizzeria.getPreparadorEmpanadero())
   
    def prepararPizzas(self):
        lista_pizzero.recargar(self.widgets,self.pizzeria.getPreparadorPizzero())


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
    
def recargar(widgets):
    lista_ingreso.recargar(widgets)
    lista_productos.recargar(widgets)
    lista_insumos.recargar(widgets)
    lista_clientes.recargar(widgets)
    lista_listos.recargar(widgets)
    lista_empanadero.recargar(widgets)
    lista_pizzero.recargar(widgets)
