#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

import gtk
import gtk.glade
import gobject

from config import *

import inicializador
import creacion
import gestion
import cocina

import humanize

###################################################
# Helper para widgets GTK2                        #
###################################################

class WidgetsWrapper:
    def __init__(self, window_name, handlers):
        self.widgets = gtk.glade.XML(GLADE_FILE, window_name)
        self.window_name = window_name
        self.widgets.signal_autoconnect(handlers.__dict__)
        
    def __getitem__(self, key):
        return self.widgets.get_widget(key)


###################################################
# Handlers                                        #
###################################################

class MainHandlers:

    # --------------------------------------------- #
    # Handlers para la ventana de "Acerca de..."    #
    # --------------------------------------------- #
    
    def ayuda_acercade_clicked(event):
        
        class AboutHandlers:
            def acercade_close(event):
                about[ABOUT_WINDOW].hide()
            def acercade_response(id, event):
                about[ABOUT_WINDOW].hide()

        about = WidgetsWrapper(ABOUT_WINDOW, AboutHandlers)
        
        # Esto por alguna razon no se setea bien en el Glade,
        # así que lo seteo de nuevo manualmente acá.
        about[ABOUT_WINDOW].set_program_name(PROGRAM_NAME)


    # --------------------------------------------- #
    # Handlers para el dialogo de "Nuevo Pedido"    #
    # ----------------------------------------------#

    def nuevo_pedido_clicked(id, event):
        
        class NuevoPedidoHandlers:
            def nuevo_pedido_close(event):
                nuevop[NUEVO_PEDIDO_WINDOW].hide()
            def nuevo_pedido_response(id, event):
                nuevop[NUEVO_PEDIDO_WINDOW].hide()
        
        nuevop = WidgetsWrapper(NUEVO_PEDIDO_WINDOW, NuevoPedidoHandlers)


    # --------------------------------------------- #
    # Handlers para el dialogo de "Nuevo Pedido"    #
    # ----------------------------------------------#
    
    def lista_ingreso_cursor_changed(event):
        tv = widgets[LISTA_INGRESO] 
        seleccion, iterador = tv.get_selection().get_selected()
        
        if iterador is None:
            limpiar_datos_pedido_ingreso()
        else:
            pedido_id = seleccion.get_value(iterador, 1)
            cargar_datos_pedido_ingreso(pedido_id)


    # --------------------------------------------- #
    # Handlers para el dialogo de "Nuevo Pedido"    #
    # ----------------------------------------------#
    
    def lista_productos_cursor_changed(event):    
        tv = widgets[LISTA_PRODUCTOS] 
        seleccion, iterador = tv.get_selection().get_selected()
        
        if iterador is None:
            limpiar_datos_producto()
        else:
            nombre_producto = seleccion.get_value(iterador, 0)
            cargar_datos_producto(nombre_producto)


    # --------------------------------------------- #
    # Handlers para cerrar el programa              #
    # --------------------------------------------- #
    
    def ventana_cerrar_clicked(widget, event):
        gtk.main_quit()

    def archivo_salir_clicked(event):
        gtk.main_quit()



###################################################
# Funciones auxiliares para los handlers          #
###################################################

 # --------------------------------------------- #
 # Funciones para la lista de pedidos ingresados #
 # ----------------------------------------------#
    
def iniciar_lista_ingreso():
    tv = widgets[LISTA_INGRESO]
    
    # Armo el ListStore (con los tipos de las columnas)
    ls = gtk.ListStore(gobject.TYPE_STRING,
                       gobject.TYPE_STRING,
                       gobject.TYPE_INT,
                      )
    tv.set_model(ls)
    
    # Armo las columnas
    render_id = gtk.CellRendererText()
    col_id = gtk.TreeViewColumn ("ID", render_id, text=0)
    tv.append_column (col_id)    
    
    render_2id = gtk.CellRendererText()
    col_2id = gtk.TreeViewColumn ("2*ID", render_2id, text=1)
    tv.append_column (col_2id)    

def recargar_lista_ingreso():
    tv = widgets[LISTA_INGRESO]
    ls = tv.get_model() 
    
    for i in range(5):
        it = ls.insert(0)
        ls.set_value(it, 0, i)
        ls.set_value(it, 1, 2*i)

def limpiar_lista_ingreso():
    tv = widgets[LISTA_INGRESO]
    ls = tv.get_model() 
    ls.clear() 


 # --------------------------------------------- #
 # Funciones para detalle de pedido ingresado -- #
 # ----------------------------------------------#


def iniciar_datos_pedido_ingreso():
    tv = widgets[DATOS_PEDIDO_INGRESO]
    
    # Armo el ListStore (con los tipos de las columnas)
    ls = gtk.ListStore(gobject.TYPE_STRING,
                       gobject.TYPE_STRING,
                      )
    tv.set_model(ls)
    
    # Armo las columnas
    render_id = gtk.CellRendererText()
    col_id = gtk.TreeViewColumn ("ID", render_id, text=0)
    tv.append_column (col_id)    
    
    render_2id = gtk.CellRendererText()
    col_2id = gtk.TreeViewColumn ("Tito", render_2id, text=1)
    tv.append_column (col_2id)    
    

def cargar_datos_pedido_ingreso(pid):
    tv = widgets[DATOS_PEDIDO_INGRESO]
    ls = tv.get_model() 
    ls.clear()  
 
    it = ls.insert(0)
    ls.set_value(it, 0, pid)
    ls.set_value(it, 1, "tito") 

def limpiar_datos_pedido_ingreso():
    tv = widgets[DATOS_PEDIDO_INGRESO]
    ls = tv.get_model()
    ls.clear()


 # --------------------------------------------- #
 # Funciones para detalle de productos --------- #
 # ----------------------------------------------#


def iniciar_lista_productos():
    tv = widgets[LISTA_PRODUCTOS]
    
    # Armo el ListStore (con los tipos de las columnas)
    ls = gtk.ListStore(gobject.TYPE_STRING,
                       gobject.TYPE_STRING,
                       gobject.TYPE_INT,
                      )
    tv.set_model(ls)
    
    # Armo las columnas
    render_id = gtk.CellRendererText()
    col_id = gtk.TreeViewColumn ("Nombre", render_id, text=0)
    tv.append_column (col_id)    
    

    render_2id = gtk.CellRendererText()
    col_2id = gtk.TreeViewColumn ("Tipo", render_2id, text=1)
    tv.append_column (col_2id)   


    render_3id = gtk.CellRendererText()
    col_3id = gtk.TreeViewColumn ("Precio", render_3id, text=2)
    tv.append_column (col_3id)   

def recargar_lista_productos():
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


def limpiar_lista_productos():    
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
                                       humanize.bool2hum(prod.getPreparable()),
                                       humanize.sec2hum(prod.getTiempoPreparacion()),
                                       humanize.bool2hum(prod.getCocinable()),
                                       humanize.sec2hum(prod.getTiempoCoccion()))
    
    insumos = '\n'.join([x.getNombre() for x in prod.getInsumos()])
    datos += "<b>Insumos</b>\n" + insumos
    
    return datos

def cargar_datos_producto(nombre_producto):
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

def limpiar_datos_producto():
    tv = widgets[DATOS_PRODUCTO]
    tv.set_markup("")


###################################################
# Main                                            #
###################################################

if __name__ == '__main__':
    
    f = open("datos.pyp", "rb")
    pizzeria = inicializador.Pizzeria(f)    


    widgets = WidgetsWrapper(MAIN_WINDOW, MainHandlers)
    iniciar_lista_ingreso()
    recargar_lista_ingreso()

    iniciar_datos_pedido_ingreso()

    iniciar_lista_productos()
    recargar_lista_productos()

    gtk.main()
