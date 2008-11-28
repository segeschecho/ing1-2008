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

#import humanize

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

    def lista_insumos_cursor_changed(event):    
        tv = widgets[LISTA_INSUMOS] 
        seleccion, iterador = tv.get_selection().get_selected()
        
        if iterador is None:
            limpiar_datos_insumo()
        else:
            nombre_insumo = seleccion.get_value(iterador, 0)
            cargar_datos_insumo(nombre_insumo)

    def lista_clientes_cursor_changed(event):    
        tv = widgets[LISTA_CLIENTES] 
        seleccion, iterador = tv.get_selection().get_selected()
        
        if iterador is None:
            limpiar_datos_cliente()
        else:
            nombre_cliente = seleccion.get_value(iterador, 0)
            cargar_datos_insumo(nombre_cliente)


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
    # FIXME: esto se puede refactorear en un loop
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
 # Funciones para detalle de clientes ---------- #
 # ----------------------------------------------#

def iniciar_lista_clientes():
    pass

def recargar_lista_clientes():
    pass

def limpiar_lista_cliente():
    pass

def formatear_datos_cliente():
    pass

def cargar_datos_cliente():
    pass

def limpiar_datos_cliente():
    pass


 # --------------------------------------------- #
 # Funciones para detalle de insumo ------------ #
 # ----------------------------------------------#

def iniciar_lista_insumos():
    tv = widgets[LISTA_INSUMOS]
    
    # Armo el ListStore (con los tipos de las columnas)
    ls = gtk.ListStore(gobject.TYPE_STRING,)
    tv.set_model(ls)
    
    render1 = gtk.CellRendererText()
    col1 = gtk.TreeViewColumn ("Nombre", render1, text=0)
    tv.append_column (col1)
    

    #render2 = gtk.CellRendererText()
    #col2 = gtk.TreeViewColumn ("Cantidad", render2, text=1)
    #tv.append_column (col2)   


    #render3 = gtk.CellRendererText()
    #col3 = gtk.TreeViewColumn ("Cantidad Critica", render3, text=2)
    #tv.append_column (col3)  

def recargar_lista_insumos():
    tv = widgets[LISTA_INSUMOS]
    ls = tv.get_model() 
    ls.clear()  
 
    ins = creacion.Insumo.allInstances()[:]

    for each in ins:
        if each.getCant() < each.getCantCritica():
        	it = ls.insert(0)
        	ls.set_value(it, 0, each.getNombre()+"[CRITICO]")
        else:
                it = ls.insert(0)
        	ls.set_value(it, 0, each.getNombre())
        

def limpiar_lista_insumo():
    tv = widgets[LISTA_INSUMO]
    ls = tv.get_model()
    ls.clear()

def formatear_datos_insumo(ins):
    datos = ("<b>%s</b>\n\n" + \
             "Cantidad en stock: %s\n" + \
             "Cantidad critica: %s\n\n") % (ins.getNombre(),ins.getCant(),ins.getCantCritica())
    productos = '\n'.join([x.getNombre() for x in creacion.Producto.allInstances() if ins in x.getInsumos()])
    datos += "<b>Productos que lo usan</b>\n" + productos
    
    return datos

def cargar_datos_insumo(nombre_insumo):
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

def limpiar_datos_insumo():
    tv = widgets[DATOS_INSUMO]
    tv.set_markup("")


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
    # FIXME: esto se puede refactorear en un loop
    render1 = gtk.CellRendererText()
    col1 = gtk.TreeViewColumn ("Nombre", render1, text=0)
    tv.append_column (col1)
    

    render2 = gtk.CellRendererText()
    col2 = gtk.TreeViewColumn ("Tipo", render2, text=1)
    tv.append_column (col2)   


    render3 = gtk.CellRendererText()
    col3 = gtk.TreeViewColumn ("Precio", render3, text=2)
    tv.append_column (col3)   

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
                                       prod.getPreparable(),#humanize.bool2hum(prod.getPreparable()),
                                       prod.getCocinable(),#humanize.sec2hum(prod.getCocinable()),
                                       prod.getCocinable(),#humanize.bool2hum(prod.getCocinable()),
                                       prod.getTiempoCoccion())#humanize.sec2hum(prod.getTiempoCoccion()))
    
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
    
    iniciar_lista_insumos()
    recargar_lista_insumos()

    gtk.main()
