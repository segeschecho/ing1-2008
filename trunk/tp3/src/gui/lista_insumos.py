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
    tv = widgets[LISTA_INSUMOS]
    
    # Armo el ListStore
    ls = gtk.ListStore(gobject.TYPE_STRING,
                       gobject.TYPE_INT,
                       gobject.TYPE_STRING,
                       gobject.TYPE_INT,
                       gobject.TYPE_INT,
                      )
    tv.set_model(ls)
    
    # Armo las columnas
    tv.append_column(gtk.TreeViewColumn("Nombre",       gtk.CellRendererText(),  text=0,    background=2))
    tv.append_column(gtk.TreeViewColumn("Stock",        gtk.CellRendererText(),  text=1)                 )
    tv.append_column(gtk.TreeViewColumn("Crítica",      gtk.CellRendererText(),  text=3)                 )
    

def recargar(widgets):
    tv = widgets[LISTA_INSUMOS]
    ls = tv.get_model() 
    ls.clear()  
 
    ins = creacion.Insumo.allInstances()[:]

    for each in ins:
        it = ls.insert(0)
        ls.set_value(it, 0, each.getNombre())
        ls.set_value(it, 1, each.getCant())
        ls.set_value(it, 3, each.getCantCritica())
        ls.set_value(it, 4, each.getId())

        # Si la cantidad es critica, pinto el fondo de rojo
        if each.getCant() < each.getCantCritica():
            ls.set_value(it, 2, "#FF9595")
        else:
            ls.set_value(it, 2, "#FFFFFF")
        

def limpiar(widgets):
    tv = widgets[LISTA_INSUMOS]
    ls = tv.get_model()
    ls.clear()

def formatear_datos_insumo(ins):
    datos = ("<b>%s</b>\n\n" + \
             "Cantidad en stock: %s\n" + \
             "Cantidad crítica: %s\n\n") % (ins.getNombre(),ins.getCant(),ins.getCantCritica())
    productos = '\n'.join([x.getNombre() for x in creacion.Producto.allInstances() if ins in x.getInsumos()])
    datos += "<b>Productos asociados</b>\n" + productos
    
    return datos

def cargar_datos(widgets, nombre_insumo):
    tv = widgets[DATOS_INSUMO]

    # FIXME: refactorear este papelon
    # busco el producto por nombre
    ins = None
    for each in creacion.Insumo.allInstances():
        if each.getNombre() == nombre_insumo:
            ins = each
    if ins is None:
        raise ValueError('No se encontró el insumo!')
    
    tv.set_markup(formatear_datos_insumo(ins))

def limpiar_datos(widgets):
    tv = widgets[DATOS_INSUMO]
    tv.set_markup("")


