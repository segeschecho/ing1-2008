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
    


def recargar(widgets,contIng=None):
    tv = widgets[LISTA_INGRESO]
    ls = tv.get_model() 
    ls.clear() 
    if contIng != None:
       ingresados=contIng.getIngresados()   
       for each in ingresados:
        it = ls.insert(0)
        ls.set_value(it, 0, each.getId())
        #con esto se intenta evitar que te queden los datos de un pedido que se fue
    limpiar_datos(widgets)
        

def limpiar(widgets):
    tv = widgets[LISTA_INGRESO]
    ls = tv.get_model() 
    ls.clear() 


 # --------------------------------------------- #
 # Funciones para detalle de pedido ingresado    #
 # --------------------------------------------- #

def limpiar_datos(widgets):
    tv = widgets[DATOS_PEDIDO_INGRESO]
    tv.set_markup("")

def iniciar_datos(widgets):
    tv = widgets[DATOS_PEDIDO_INGRESO]
    
    # Armo el ListStore
    ls = gtk.ListStore(gobject.TYPE_STRING,
                       gobject.TYPE_STRING,
                      )
    tv.set_model(ls)
    
    # Armo las columnas
    #tv.append_column(gtk.TreeViewColumn("ID",           gtk.CellRendererText(),  text=0)                 )
    #tv.append_column(gtk.TreeViewColumn("Tito",         gtk.CellRendererText(),  text=1)                 )
    

def cargar_datos(widgets, pid):
    tv = widgets[DATOS_PEDIDO_INGRESO]
    ped = None
    print creacion.Pedido.allInstances()
    for each in creacion.Pedido.allInstances():
       print each.getId()
       print pid
       if str(each.getId()) == str(pid):
           ped = each
           break
    if ped == None:
       raise ValueError("Pedido no encontrado, no puedo mostrar datos")
    tv.set_markup(formatear_datos_ingreso(ped))




def formatear_datos_ingreso(ped):
    datos = ("<b>Pedido:</b>\n\n" + \
             "ID: %s\n" + \
             "Fecha de ingreso: %s\n" + \
             "Tiempo estimado: %s\n" + \
             "Precio: %s\n")% (ped.getId(),ped.getFechaIngreso(),ped.getTiempoEstimado(),ped.getPrecio())
    comoposicion = '\n'.join([x.getNombre() for x in ped.getProductos()])
    datos += "<b>Composicion</b>\n" + comoposicion
    if(ped.getCliente() != None):
       datos +="\n\nCliente:"+ped.getCliente().getApellido()+", "+ped.getCliente().getNombre()
    if(ped.getHorno() != None):
      datos +="\n\n<b>Horno asignado: </b>"+ped.getHorno().getDescripcion()
    return datos

