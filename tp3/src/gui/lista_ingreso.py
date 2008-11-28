#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

import gobject
import gtk

from config import *
import creacion

 # --------------------------------------------- #
 # Funciones para la lista de pedidos ingresados #
 # ----------------------------------------------#
    
def iniciar(widgets):
    tv = widgets[LISTA_INGRESO]
    
    # Armo el ListStore
    ls = gtk.ListStore(gobject.TYPE_STRING,
                       gobject.TYPE_STRING,
                       gobject.TYPE_INT,
                      )
    tv.set_model(ls)
    
    # Armo las columnas
    tv.append_column(gtk.TreeViewColumn("ID",           gtk.CellRendererText(),  text=0)                 )
    tv.append_column(gtk.TreeViewColumn("2*ID",         gtk.CellRendererText(),  text=1)                 )


def recargar(widgets):
    tv = widgets[LISTA_INGRESO]
    ls = tv.get_model() 
    
    for i in range(5):
        it = ls.insert(0)
        ls.set_value(it, 0, i)
        ls.set_value(it, 1, 2*i)

def limpiar(widgets):
    tv = widgets[LISTA_INGRESO]
    ls = tv.get_model() 
    ls.clear() 


 # --------------------------------------------- #
 # Funciones para detalle de pedido ingresado    #
 # --------------------------------------------- #



def iniciar_datos(widgets):
    tv = widgets[DATOS_PEDIDO_INGRESO]
    
    # Armo el ListStore
    ls = gtk.ListStore(gobject.TYPE_STRING,
                       gobject.TYPE_STRING,
                      )
    tv.set_model(ls)
    
    # Armo las columnas
    tv.append_column(gtk.TreeViewColumn("ID",           gtk.CellRendererText(),  text=0)                 )
    tv.append_column(gtk.TreeViewColumn("Tito",         gtk.CellRendererText(),  text=1)                 )
    

def cargar_datos(widgets, pid):
    tv = widgets[DATOS_PEDIDO_INGRESO]
    ls = tv.get_model() 
    ls.clear()  
 
    it = ls.insert(0)
    ls.set_value(it, 0, pid)
    ls.set_value(it, 1, "tito") 

def limpiar_datos(widgets):
    tv = widgets[DATOS_PEDIDO_INGRESO]
    ls = tv.get_model()
    ls.clear()



