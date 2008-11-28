#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

import gobject
import gtk
import creacion
from config import *

 
 # --------------------------------------------- #
 # Funciones para detalle de clientes            #
 # --------------------------------------------- #
def iniciar(widgets):
    tv = widgets[LISTA_CLIENTES]
    
    # Armo el ListStore (con los tipos de las columnas)
    ls = gtk.ListStore(gobject.TYPE_STRING,
                       gobject.TYPE_STRING,
                       gobject.TYPE_STRING,
                      )
    tv.set_model(ls)
    
    # Armo las columnas
    # FIXME: esto se puede refactorear en un loop
    render1 = gtk.CellRendererText()
    col1 = gtk.TreeViewColumn ("Apellido", render1, text=0)
    tv.append_column (col1)
    

    render2 = gtk.CellRendererText()
    col2 = gtk.TreeViewColumn ("Nombre", render2, text=1)
    tv.append_column (col2)   


    render3 = gtk.CellRendererText()
    col3 = gtk.TreeViewColumn ("ID", render3, text=2)
    tv.append_column (col3)   

def recargar(widgets):
    tv = widgets[LISTA_CLIENTES]
    ls = tv.get_model() 
    ls.clear()  
 
    clientes = creacion.Cliente.allInstances()[:]
    clientes.sort(lambda x,y: cmp(x.getApellido(),
                               y.getApellido()))
    
    for each in clientes:
        it = ls.insert(0)
        ls.set_value(it, 0, each.getApellido())
        ls.set_value(it, 1, each.getNombre())
        ls.set_value(it, 2, each.getId())

def limpiar(widgets):
    tv = widgets[LISTA_CLIENTES]
    ls = tv.get_model()
    ls.clear()
    
def formatear_datos(cliente):
    datos = ("<b>Cliente:</b>\n\n" + \
             "Id: %s\n" + \
             "Apellido y nombre: %s %s\n" + \
             "Teléfono: %s\n" + \
             "Celular: %s \n\n" + \
             "Localidad: %s\n" + \
             "Dirección: %s %s\n" + \
             "Departamento: %s\n" + \
             "Usuario web: %s\n\n") % (cliente.getId(),
                                       cliente.getApellido(),
                                       cliente.getNombre(),
                                       cliente.getTelefono(),
                                       cliente.getCelular(),
                                       cliente.getDireccion().getLocalidad(),
                                       cliente.getDireccion().getCalle(),
                                       cliente.getDireccion().getNumero(),
                                       cliente.getDireccion().getDepartamento(),
                                       cliente.getUsrWeb())
    datos +="\n<b>Pedidos</b>:\n"
    datos += '\n'.join([str(p.id)+" "+p.getEstado() for p in creacion.Pedido.allInstances() if p.cliente == cliente])
    return datos

def cargar_datos(widgets, id_cliente):
    tv = widgets[DATOS_CLIENTE]

    # FIXME: refactorear este papelon
    # busco el producto por nombre
    cliente = None
    for each in creacion.Cliente.allInstances():

        if str(each.getId()) == str(id_cliente):

            cliente = each
    if cliente == None:
        raise ValueError('No se encontró el cliente!')
    
    tv.set_markup(formatear_datos(cliente))

def limpiar_datos(widgets):
    tv = widgets[DATOS_CLIENTE]
    tv.set_markup("")
