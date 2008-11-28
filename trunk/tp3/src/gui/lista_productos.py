#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

import gobject
import gtk

from config import *
import creacion


 # --------------------------------------------- #
 # Funciones para detalle de productos --------- #
 # ----------------------------------------------#


def iniciar(widgets):
    tv = widgets[LISTA_PRODUCTOS]
    
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


def recargar(widgets):
    tv = widgets[LISTA_PRODUCTOS]
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
    tv = widgets[LISTA_PRODUCTOS]
    ls = tv.get_model()
    ls.clear()

def formatear_datos_producto(prod):
    datos = ("<b>%s</b>\n\n" + \
             "Tipo: %s\n" + \
             "Precio: $%s\n\n" + \
             "Preparable: %s\n" + \
             "Tiempo de preparación: %s \n" + \
             "Cocinable: %s\n" + \
             "Tiempo de cocción: %s\n\n") % (prod.getNombre(),
                                       prod.getTipo().getNombre(),
                                       prod.getPrecio(),
                                       prod.getPreparable(),#humanize.bool2hum(prod.getPreparable()),
                                       prod.getCocinable(),#humanize.sec2hum(prod.getCocinable()),
                                       prod.getCocinable(),#humanize.bool2hum(prod.getCocinable()),
                                       prod.getTiempoCoccion())#humanize.sec2hum(prod.getTiempoCoccion()))
    
    insumos = '\n'.join([x.getNombre() for x in prod.getInsumos()])
    datos += "<b>Insumos</b>\n" + insumos
    
    return datos


def cargar_datos(widgets, nombre_producto):
    tv = widgets[DATOS_PRODUCTO]

    # FIXME: refactorear este papelon
    # busco el producto por nombre
    prod = None
    for each in creacion.Producto.allInstances():
        if each.getNombre() == nombre_producto:
            prod = each
    if prod is None:
        raise ValueError('No se encontró el producto!')
    
    tv.set_markup(formatear_datos_producto(prod))


def limpiar_datos(widgets):
    tv = widgets[DATOS_PRODUCTO]
    tv.set_markup("")

