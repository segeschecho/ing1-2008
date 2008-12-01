#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

import gobject
import gtk

from config import *


 # --------------------------------------------------#
 # Funciones para preparacion empanadera ----------- #
 # --------------------------------------------------#

def iniciar(widgets):
    tv = widgets[LISTA_EMPANADERO]
    
    # Armo el ListStore
    ls = gtk.ListStore(gobject.TYPE_STRING,)
    tv.set_model(ls)
    
    # Armo las columnas
    tv.append_column(gtk.TreeViewColumn("Producto",        gtk.CellRendererText(),  text=0)                 )


    

def recargar(widgets,prepEmp=None):
    tv = widgets[LISTA_EMPANADERO]
    ls = tv.get_model() 
    ls.clear()  
    if prepEmp!=None:
        prep = prepEmp.getPreparar()

        for each in prep:
            it = ls.insert(0)
            ls.set_value(it, 0, each.getNombre())
        if prep == []:
           bp = widgets["empanadas_preparadas"]
           bp.set_sensitive(False)
        else:
           bp = widgets["empanadas_preparadas"]
           bp.set_sensitive(True)
 
    else:
           bp = widgets["empanadas_preparadas"]
           bp.set_sensitive(False)


        

def limpiar(widgets):
    tv = widgets[LISTA_EMPANADERO]
    ls = tv.get_model()
    ls.clear()




