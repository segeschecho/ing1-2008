#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

import gobject
import gtk

import creacion
from config import *

from gui.helpers import WidgetsWrapper
from gui.helpers import mostrar_error

import sets
       
 # --------------------------------------------- #
 # Callback para hacer aviso de stock crítico    #
 # --------------------------------------------- #

def nuevosCriticos(contStock):
   criticos = contStock.getCriticos()
   if criticos != sets.Set([]):
       aviso = WidgetsWrapper(STOCK_CRITICO_WINDOW)
       for each in criticos:
          wnd = aviso[STOCK_CRITICO_WINDOW]
          wnd.hide()
          label = aviso['texto_critico']
          s = "<b>Atención</b>\n" + \
              "\nEl insumo <b>%s</b> (ID %s)" + \
              "\nestá por debajo del nivel crítico." + \
              "\n\nNivel Crítico: %s" 
          label.set_markup(s % (each.getNombre(), each.getId(), each.getCantCritica()))
          res = wnd.run()
          wnd.hide()


 # --------------------------------------------- #
 # Callback para pedir hornos de un pedido       #
 # --------------------------------------------- #

def pedirHorno(HornoP,HornoE):
    abrir = WidgetsWrapper(ELEGIR_HORNO_WINDOW)
    wnd = abrir[ELEGIR_HORNO_WINDOW]
    wnd.hide()
    res = wnd.run()
    
    # Esto previene que el usuario cierre la ventana
    # de seleccion con la cruz en lugar de cliquear OK.
    while res != gtk.RESPONSE_OK:
        res = wnd.run()
    wnd.hide()

    if abrir[RADIO_PIZZERO].get_active():
        return HornoP
    elif abrir[RADIO_EMPANADERO].get_active():
        return HornoE
    else:
        raise ValueError("Error inesperado: se esperaba uno de los 2 botones marcados")


 # --------------------------------------------- #
 # Funciones para ingreso de nuevo pedido        #
 # --------------------------------------------- #

class ErrorDeValidacion(Exception):
    pass


def validar_pedido(widgets):
    # obtengo el tipo de pedido
    tipo_t = widgets[NUEVO_PEDIDO_TIPO].get_active_text()
    try:
        tipo = {"Mostrador":"mostrador",
                "Teléfono":"telefono",
                "Mesa":"mesa"}[tipo_t]
    except KeyError:
        mostrar_error("Tipo inválido", "El tipo de pedido no es válido!")
        raise ErrorDeValidacion


    # obtengo el numero de mesa si corresponde
    if tipo == "mesa":
        try:
            mesa = int(widgets[NUEVO_PEDIDO_MESA].get_text())
        except ValueError:
            mostrar_error("Mesa inválida","El número de mesa no es válido!")
            raise ErrorDeValidacion
    else:
        mesa = None
            
    # obtengo la forma de pago si corresponde
    if tipo != "mesa":
        try:
            formapago_t = widgets[NUEVO_PEDIDO_FORMA_PAGO].get_active_text()
            formapago = {"Efectivo":"efectivo",
                         "Crédito":"tarjeta"}[formapago_t]
        except KeyError:
            mostrar_error("Forma de pago inválida", "La forma de pago no es válida!")
            raise ErrorDeValidacion
    else:
        formapago = None

    # obtengo el cliente
    tv = widgets[CLIENTES_PEDIDO]
    seleccion, iterador = tv.get_selection().get_selected()

    if iterador is None:
        if tipo == "telefono":
            mostrar_error("Cliente inválido", "Debe elegir un cliente para pedidos telefónicos!")
            raise ErrorDeValidacion
        else:
            cliente = None
    else:
        cliente = creacion.Cliente.getPorId(int(seleccion.get_value(iterador,0)))


    # obtengo los productos
    tv = widgets[ITEMS_PEDIDO]
    ls = tv.get_model()

    productos = []

    it = ls.get_iter_first()

    if it is None:
        mostrar_error("Pedido nulo", "Debe elegir productos para poder ingresar el pedido!")
        raise ErrorDeValidacion

    while it != None:
        prod_id = ls.get_value(it,4)
        cant = int(ls.get_value(it,2)) 
        prod = creacion.Producto.getPorId(prod_id)
        for i in range(cant):
            productos.append(prod)
        it = ls.iter_next(it) 


    return (cliente,
            productos,
            formapago,
            tipo,
            mesa)


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
        ls.set_value(it, 3, each.getId())


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
                       gobject.TYPE_FLOAT,
                       gobject.TYPE_INT,
                      )
    tv.set_model(ls)

    # Armo las columnas
    tv.append_column(gtk.TreeViewColumn("Nombre",       gtk.CellRendererText(),  text=0)                 )
    tv.append_column(gtk.TreeViewColumn("Tipo",         gtk.CellRendererText(),  text=1)                 )
    tv.append_column(gtk.TreeViewColumn("Cantidad",     gtk.CellRendererText(),  text=2)                 )


def recargar_items(widgets):
    recalcular_total(widgets)


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
            break
        i = ls.iter_next(i)
    
    if i == None:
        # Si no lo encontre en la lista, agrego una
        # nueva fila para este producto.
        i = ls.insert(0)
        ls.set_value(i, 0, prod.getNombre())
        ls.set_value(i, 1, prod.getTipo().getNombre())
        ls.set_value(i, 2, 1)
        ls.set_value(i, 3, prod.getPrecio())
        ls.set_value(i, 4, prod.getId())

    recalcular_total(widgets)

def recalcular_total(widgets):
    tv = widgets[ITEMS_PEDIDO]
    ltot = widgets[TOTAL_PEDIDO]

    total = 0
    ls = tv.get_model()
    i = ls.get_iter_first()
    while i != None:
        total += ls.get_value(i, 2) * ls.get_value(i, 3)
        i = ls.iter_next(i)

    ltot.set_markup("<b>Total:</b> $%s" % total)


 # --------------------------------------------- #
 # Funciones para los tipos de pedido            #
 # --------------------------------------------- #


def iniciar_tipos(widgets):
    pass

def recargar_tipos(widgets):
    cb = widgets[NUEVO_PEDIDO_TIPO]
    cb.set_active(0)

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
