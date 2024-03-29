#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

import gobject
import gtk

from config import *
import humanize
import creacion

 # --------------------------------------------- #
 # Funciones para la lista de pedidos ingresados #
 # ----------------------------------------------#
    
def iniciar(widgets):
    tv = widgets[LISTA_TODOS]
    
    # Armo el ListStore
    ls = gtk.ListStore(gobject.TYPE_INT,
                       gobject.TYPE_STRING,
                       gobject.TYPE_STRING,
                       gobject.TYPE_STRING,
                       gobject.TYPE_STRING,
                       gobject.TYPE_STRING,
                      )
    tv.set_model(ls)
    
    # Armo las columnas
    tv.append_column(gtk.TreeViewColumn("ID",           gtk.CellRendererText(),  text=0)                 )
    tv.append_column(gtk.TreeViewColumn("Precio",       gtk.CellRendererText(),  text=1)                 )
    tv.append_column(gtk.TreeViewColumn("Tiempo Est.",  gtk.CellRendererText(),  text=2)                 )
    tv.append_column(gtk.TreeViewColumn("Horno",        gtk.CellRendererText(),  text=3)                 )
    tv.append_column(gtk.TreeViewColumn("Hora",         gtk.CellRendererText(),  text=4)                 )
    tv.append_column(gtk.TreeViewColumn("Fecha",        gtk.CellRendererText(),  text=5)                 )
    


def recargar(widgets):
    tv = widgets[LISTA_TODOS]
    ls = tv.get_model() 
    ls.clear() 
    todos = creacion.Pedido.allInstances()
    for each in todos:
            it = ls.insert(0)
            ls.set_value(it, 0, each.getId())
            ls.set_value(it, 1, "$%s" % each.getPrecio())
            ls.set_value(it, 2, humanize.sec2hum(each.getTiempoEstimado()))
            if each.getHorno() != None:
                ls.set_value(it, 3, each.getHorno().getDescripcion())
            else:
                ls.set_value(it, 3, "-")
            ls.set_value(it, 4, each.getFechaIngreso().strftime("%H:%M"))
            ls.set_value(it, 5, each.getFechaIngreso().strftime("%d/%m"))


    limpiar_datos(widgets)
        

def limpiar(widgets):
    tv = widgets[LISTA_TODOS]
    ls = tv.get_model() 
    ls.clear() 


 # --------------------------------------------- #
 # Funciones para detalle de pedido ingresado    #
 # --------------------------------------------- #

def limpiar_datos(widgets):
    tv = widgets[PRODUCTOS_PEDIDO_TODOS]
    tv.get_model().clear()
    det = widgets[DATOS_PEDIDO_TODOS]
    det.set_markup("")

def iniciar_datos(widgets):
    tv = widgets[PRODUCTOS_PEDIDO_TODOS]
    
    # Armo el ListStore
    ls = gtk.ListStore(gobject.TYPE_INT,
                       gobject.TYPE_STRING,
                       gobject.TYPE_STRING,
                      )
    tv.set_model(ls)
    
    # Armo las columnas
    tv.append_column(gtk.TreeViewColumn("Cantidad",     gtk.CellRendererText(),  text=0)                 )
    tv.append_column(gtk.TreeViewColumn("Producto",     gtk.CellRendererText(),  text=1)                 )
    tv.append_column(gtk.TreeViewColumn("Tipo"    ,     gtk.CellRendererText(),  text=2)                 )
    

def cargar_datos(widgets, pid):

    # FIXME: refactorear esta busqueda
    pedido = None
    for each in creacion.Pedido.allInstances():
        if each.getId() == pid:
            pedido = each
            break
    if pedido is None:
        raise ValueError("Pedido no encontrado!") 
    
    
    # cargo los detalles del pedido 
    det = widgets[DATOS_PEDIDO_TODOS]
    det.set_markup(formatear_datos_todos(pedido))
    
    # cargo el listado de productos del pedido
    tv = widgets[PRODUCTOS_PEDIDO_TODOS]
    ls = tv.get_model()
    contados = humanize.set2bag([(p.getNombre(), p.getTipo().getNombre()) for p in pedido.getProductos()])
    
    for i in contados:     
        nombre = i[0]
        tipo = i[1]
        cant = contados[i]
        it = ls.insert(0)

        ls.set_value(it, 0, cant)
        ls.set_value(it, 1, nombre)
        ls.set_value(it, 2, tipo)



def formatear_datos_todos(ped):
    datos = ("\n<b>ID:</b> %s\n" + \
             "Ingreso: %s\n" + \
             "Tiempo estimado: %s\n" + \
             "Precio: $%s\n" + \
             "Estado: %s\n") % (ped.getId(),
                                 ped.getFechaIngreso().strftime("%d/%m @ %H:%M:%S"),
                                 humanize.sec2hum(ped.getTiempoEstimado()),
                                 ped.getPrecio(), ped.getEstado())
    
    if(ped.getCliente() != None):
        datos +="\n\n<b>Cliente</b>: %s %s" % (ped.getCliente().getNombre(),
                                               ped.getCliente().getApellido()
                                              )
    
    if(ped.getHorno() != None):
        datos +="\n\n<b>Horno</b>: %s" % ped.getHorno().getDescripcion()
    
    return datos

