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


def limpiar_productos(widgets):    
    tv = widgets[PRODUCTOS_PEDIDO]
    ls = tv.get_model()
    ls.clear()


 # --------------------------------------------- #
 # Funciones para los items de un pedido         #
 # --------------------------------------------- #

def iniciar_items(widgets):
    tv = widgets[ITEMS_PEDIDO]
    
    # Armo el ListStore
    ls = gtk.ListStore(gobject.TYPE_STRING,
                       gobject.TYPE_STRING,
                       gobject.TYPE_INT,
                      )
    tv.set_model(ls)

    # Armo las columnas
    tv.append_column(gtk.TreeViewColumn("Nombre",       gtk.CellRendererText(),  text=0)                 )
    tv.append_column(gtk.TreeViewColumn("Tipo",         gtk.CellRendererText(),  text=1)                 )
    tv.append_column(gtk.TreeViewColumn("Cantidad",     gtk.CellRendererText(),  text=2)                 )


def recargar_items(widgets):
    pass


def limpiar_items(widgets):    
    tv = widgets[ITEMS_PEDIDO]
    ls = tv.get_model()
    ls.clear()


def agregar_a_pedido(widgets, nombre_producto):
    tv = widgets[ITEMS_PEDIDO]

    # FIXME: refactorear este papelon
    # busco el producto por nombre
    prod = None
    for each in creacion.Producto.allInstances():
        if each.getNombre() == nombre_producto:
            prod = each
            break
    if prod is None:
        raise ValueError('No se encontró el producto!')

    # Recorro la lista actual de items del pedido
    # y agrego el nuevo producto según corresponda.    
    ls = tv.get_model()
    i = ls.get_iter_first()
    while i != None:
        if ls.get_value(i, 0) == prod.getNombre():
            cant = ls.get_value(i, 2)
            ls.set_value(i, 2, cant + 1)
            return
        i = ls.iter_next(i)
    
    # Si no lo encontre en la lista, agrego una
    # nueva fila para este producto.
    i = ls.insert(0)
    ls.set_value(i, 0, prod.getNombre())
    ls.set_value(i, 1, prod.getTipo().getNombre())
    ls.set_value(i, 2, 1)


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
    iniciar_items(widgets)
    iniciar_tipos(widgets)

def recargar(widgets):
    recargar_clientes(widgets)
    recargar_productos(widgets)
    recargar_items(widgets)
    recargar_tipos(widgets)

def limpiar(widgets):
    limpiar_clientes(widgets)
    limpiar_productos(widgets)
    limpiar_items(widgets)
    limpiar_tipos(widgets)
