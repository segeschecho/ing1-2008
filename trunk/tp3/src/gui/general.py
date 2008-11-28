#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

from gui import lista_ingreso
from gui import lista_insumos
from gui import lista_clientes
from gui import lista_productos
from gui import lista_ingreso


 # --------------------------------------------- #
 # Funciones para iniciar y limpiar toda la GUI  #
 # ----------------------------------------------#

def iniciar(widgets):
        
    lista_ingreso.iniciar(widgets)
    lista_ingreso.iniciar_datos(widgets)
    lista_productos.iniciar(widgets)
    lista_insumos.iniciar(widgets)

def limpiar(widgets):
    lista_ingreso.limpiar(widgets)
    lista_ingreso.limpiar_datos(widgets)
    lista_productos.limpiar(widgets)
    lista_productos.limpiar_datos(widgets)
    lista_insumos.limpiar(widgets)
    lista_insumos.limpiar_datos(widgets)
    
def recargar(widgets):
    lista_ingreso.recargar(widgets)
    lista_productos.recargar(widgets)
    lista_insumos.recargar(widgets)

