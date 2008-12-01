#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

import gobject
import gtk

from config import *


 # --------------------------------------------------#
 # Funciones para preparacion pizzera ----------- #
 # --------------------------------------------------#

def iniciar(widgets):
    tv = widgets[LISTA_PIZZERO]
    
    # Armo el ListStore
    ls = gtk.ListStore(gobject.TYPE_STRING,)
    tv.set_model(ls)
    
    render1 = gtk.CellRendererText()
    col1 = gtk.TreeViewColumn ("Producto", render1, text=0)
    tv.append_column (col1)
    



    

def recargar(widgets,prepPiz=None):
    tv = widgets[LISTA_PIZZERO]
    ls = tv.get_model() 
    ls.clear()  
    if prepPiz!=None:
        prep = prepPiz.getPreparar()

        for each in prep:
            it = ls.insert(0)
            ls.set_value(it, 0, each.getNombre())

        if prep == []:
           bp = widgets["pizzas_preparadas"]
           bp.set_sensitive(False)
        else:
           bp = widgets["pizzas_preparadas"]
           bp.set_sensitive(True)
 
    else:
           bp = widgets["pizzas_preparadas"]
           bp.set_sensitive(False)

        

def limpiar(widgets):
    tv = widgets[LISTA_PIZZERO]
    ls = tv.get_model()
    ls.clear()




