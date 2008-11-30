#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

import gobject
import gtk

import creacion
from config import *

 
 # --------------------------------------------- #
 # Funciones para lista de clientes              #
 # --------------------------------------------- #

def iniciar_clientes(widgets):
    tv = widgets[CLIENTES_PEDIDO]
    
    # Armo el ListStore (con los tipos de las columnas)
    ls = gtk.ListStore(gobject.TYPE_INT,
                       gobject.TYPE_STRING,
                       gobject.TYPE_STRING,
                       gobject.TYPE_STRING,
                      )
    tv.set_model(ls)
    
    # Armo las columnas
    tv.append_column(gtk.TreeViewColumn("ID",             gtk.CellRendererText(),  text=0)                 )
    tv.append_column(gtk.TreeViewColumn("Nombre",         gtk.CellRendererText(),  text=1)                 )
    tv.append_column(gtk.TreeViewColumn("Apellido",       gtk.CellRendererText(),  text=2)                 )
    tv.append_column(gtk.TreeViewColumn("Usuario",        gtk.CellRendererText(),  text=3)                 )


def recargar_clientes(widgets):
    tv = widgets[CLIENTES_PEDIDO]
    ls = tv.get_model() 
    ls.clear()
 
    clientes = creacion.Cliente.allInstances()[:]
    clientes.sort(lambda x,y: cmp(x.getApellido(),
                               y.getApellido()))
    
    for each in clientes:
        it = ls.insert(0)
        ls.set_value(it, 0, each.getId())
        ls.set_value(it, 1, each.getNombre())
        ls.set_value(it, 2, each.getApellido())
        ls.set_value(it, 3, each.getUsrWeb())


def limpiar_clientes(widgets):
    tv = widgets[CLIENTES_PEDIDO]
    ls = tv.get_model()
    ls.clear()

 # --------------------------------------------- #
 # Funciones para lista de productos             #
 # --------------------------------------------- #

def iniciar_productos(widgets):
    tv = widgets[PRODUCTOS_PEDIDO]
    
    # Armo el ListStore
    ls = gtk.ListStore(gobject.TYPE_STRING,
                       gobject.TYPE_STRING,
                       gobject.TYPE_INT,
                      )
    tv.set_model(ls)

    # Armo las columnas
    tv.append_column(gtk.TreeViewColumn("Nombre",       gtk.CellRendererText(),  text=0)                 )
    tv.append_column(gtk.TreeViewColumn("Tipo",         gtk.CellRendererText(),  text=1)                 )
    tv.append_column(gtk.TreeViewColumn("Precio",       gtk.CellRendererText(),  text=2)                 )


def recargar_productos(widgets):
    tv = widgets[PRODUCTOS_PEDIDO]
    ls = tv.get_model() 
    ls.clear()
 
    prods = creacion.Producto.allInstances()[:]
    prods.sort(lambda x,y: cmp(x.getTipo().getNombre(),
                               y.getTipo().getNombre()))
    
    for each in prods:
        it = ls.insert(0)
        ls.set_value(it, 0, each.getNombre())
        ls.set_value(it, 1, each.getTipo().getNombre())
        ls.set_value(it, 2, each.getPrecio())


def limpiar(widgets):    
    tv = widgets[PRODUCTOS_PEDIDO]
    ls = tv.get_model()
    ls.clear()


 # --------------------------------------------- #
 # Funciones para los tipos de pedido            #
 # --------------------------------------------- #

def iniciar_tipos(widgets):
    cb = widgets[NUEVO_PEDIDO_TIPO]
    
    # Armo el ListStore
    ls = gtk.ListStore(gobject.TYPE_STRING)
    ls.append(["Mesa"])
    ls.append(["Teléfono"])
    ls.append(["Mostrador"])

    cb.set_model(ls)
    cb.set_text_column(0)
    cb.set_active(0)


def recargar_tipos(widgets):
    pass

def limpiar_tipos(widgets):
    pass

 # --------------------------------------------- #
 # Funciones generales                           #
 # --------------------------------------------- #

def iniciar(widgets):
    iniciar_clientes(widgets)
    iniciar_productos(widgets)
    iniciar_tipos(widgets)

def recargar(widgets):
    recargar_clientes(widgets)
    recargar_productos(widgets)
    recargar_tipos(widgets)

def limpiar(widgets):
    limpiar_clientes(widgets)
    limpiar_productos(widgets)
    limpiar_tipos(widgets)
