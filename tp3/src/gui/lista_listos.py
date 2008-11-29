#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

import gobject
import gtk

from config import *
import humanize
import creacion


 # --------------------------------------------- #
 # Funciones para lista de pedidos listos        #
 # ----------------------------------------------#

def iniciar(widgets):
    tv = widgets[LISTA_LISTOS]

    
    # Armo el ListStore
    tv.set_model(gtk.ListStore(gobject.TYPE_INT,
                               gobject.TYPE_STRING
                              )
                )
    
    # Armo las columnas
    tv.append_column(gtk.TreeViewColumn("ID",           gtk.CellRendererText(),  text=0)                 )
    tv.append_column(gtk.TreeViewColumn("Destino",      gtk.CellRendererText(),  text=1)                 )
 

def recargar(widgets, contListos=None):
    tv = widgets[LISTA_LISTOS]
    ls = tv.get_model() 
    ls.clear()

    if contListos!=None:
        listos = contListos.getListos()
        for each in listos:
            it = ls.insert(0)
            ls.set_value(it, 0, each.getId())
            ls.set_value(it, 1, each.getDestino())

    # FIXME: esto evita que queden a la vista datos de un
    #        pedido que se fue de la cola (no es lo ideal, habría
    #        que recargar si sale de la cola únicamente, pero funciona)
    limpiar_datos(widgets)

        

def limpiar(widgets):
    tv = widgets[LISTA_LISTOS]
    ls = tv.get_model()
    ls.clear()


 # --------------------------------------------- #
 # Funciones para detalle de pedido listo        #
 # --------------------------------------------- #

def limpiar_datos(widgets):
    tv = widgets[PRODUCTOS_AGREGAR]
    tv.get_model().clear()
    det = widgets[DATOS_PEDIDO_LISTO]
    det.set_markup("")

def iniciar_datos(widgets):
    tv = widgets[PRODUCTOS_AGREGAR]
        
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
    det = widgets[DATOS_PEDIDO_LISTO]
    det.set_markup(formatear_datos_listo(pedido))
    
    # cargo el listado de productos del pedido
    tv = widgets[PRODUCTOS_AGREGAR]
    ls = tv.get_model()
    agregar = [p for p in pedido.getProductos() if not (p.getCocinable() or p.getPreparable())]
    contados = humanize.set2bag([(p.getNombre(), p.getTipo().getNombre()) for p in agregar])
    
    for i in contados:     
        nombre = i[0]
        tipo = i[1]
        cant = contados[i]
        it = ls.insert(0)

        ls.set_value(it, 0, cant)
        ls.set_value(it, 1, nombre)
        ls.set_value(it, 2, tipo)

# FIXME: esto se podría refactorear como método de pedido,
#        pero teniendo en cuenta que esto por cohesión debería
#        ir en un visitor, creo que es razonable hacerlo acá
#        (Visitor en Python implica "romper" OCP)
def formatear_datos_listo(ped):
    if ped.getDestino() == "Mesa":
        return "<b>Mesa</b>: %s" % ped.getMesa()
    elif ped.getDestino() == "Delivery":
        return ("Entregar a <b>%s %s</b>\n\n" + \
               "<b>Dirección</b>\n" + \
               "Calle: %s\n" + \
               "Número: %s\n" + \
               "Departamento: %s\n" + \
               "Localidad: %s\n\n")  % (ped.getCliente().getNombre(),
                                       ped.getCliente().getApellido(),
                                       ped.getCliente().getDireccion().getCalle(),
                                       ped.getCliente().getDireccion().getNumero(),
                                       ped.getCliente().getDireccion().getDepartamento(),
                                       ped.getCliente().getDireccion().getLocalidad()
                                      )

    else:
        return ""
