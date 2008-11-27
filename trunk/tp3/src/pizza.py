#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

import gtk
import gtk.glade
import gobject

from config import *

from inicializador import Pizzeria

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
        tv = widgets['lista_ingreso']
        seleccion, iterador = tv.get_selection().get_selected()
        
        if iterador is None:
            limpiar_datos_pedido_ingreso()
        else:
            pedido_id = seleccion.get_value(iterador, 1)
            cargar_datos_pedido_ingreso(pedido_id)


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

def iniciar_lista_ingreso():
    tv = widgets['lista_ingreso']
    
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
    tv = widgets['lista_ingreso']
    ls = tv.get_model() 
    
    for i in range(5):
        it = ls.insert(0)
        ls.set_value(it, 0, i)
        ls.set_value(it, 1, 2*i)

def limpiar_lista_ingreso():
    tv = widgets['lista_ingreso']
    ls = tv.get_model() 
    ls.clear() 



def iniciar_datos_pedido_ingreso():
    tv = widgets['datos_pedido_ingreso']
    
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
    tv = widgets['datos_pedido_ingreso']
    ls = tv.get_model() 
    ls.clear()  
 
    it = ls.insert(0)
    ls.set_value(it, 0, pid)
    ls.set_value(it, 1, "tito") 

def limpiar_datos_pedido_ingreso():
    tv = widgets['datos_pedido_ingreso']
    ls = tv.get_model()
    ls.clear()

    

###################################################
# Main                                            #
###################################################

if __name__ == '__main__':
    
    f = open("datos.pyp", "rb")
    s = Pizzeria(f)    


    widgets = WidgetsWrapper(MAIN_WINDOW, MainHandlers)
    iniciar_lista_ingreso()
    recargar_lista_ingreso()

    iniciar_datos_pedido_ingreso()

    gtk.main()
