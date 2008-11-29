#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

import gobject
import gtk

from config import *
import creacion


 # --------------------------------------------- #
 # Funciones para detalle de insumo ------------ #
 # ----------------------------------------------#

def iniciar(widgets):
    tv = widgets[LISTA_LISTOS]
    
    # Armo el ListStore
    ls = gtk.ListStore(gobject.TYPE_INT,gobject.TYPE_STRING)
    tv.set_model(ls)
    
    # Armo las columnas
    render1 = gtk.CellRendererText()
    col1 = gtk.TreeViewColumn ("ID", render1, text=0)
    tv.append_column (col1)
    

    render2 = gtk.CellRendererText()
    col2 = gtk.TreeViewColumn ("Productos a agregar", render2, text=1)
    tv.append_column (col2)  

    

def recargar(widgets,contListos=None):
    tv = widgets[LISTA_LISTOS]
    ls = tv.get_model() 
    ls.clear()
    if contListos!=None:
        listos = contListos.getListos()
        for each in listos:
            it = ls.insert(0)
            ls.set_value(it, 0, each.getId())
            ls.set_value(it,1," ".join([x.getNombre() for x in each.getProductos() if (not x.getPreparable() and not x.getCocinable())])) 


        

def limpiar(widgets):
    tv = widgets[LISTA_LISTOS]
    ls = tv.get_model()
    ls.clear()




