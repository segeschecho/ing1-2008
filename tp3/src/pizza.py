#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

import gtk

from gui.config import *
from gui.helpers import WidgetsWrapper

from gui import lista_ingreso
from gui import lista_insumos
from gui import lista_clientes
from gui import lista_productos
from gui import lista_ingreso

import inicializador
import creacion
import gestion
import cocina

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
    # --------------------------------------------- #

    def nuevo_pedido_clicked(id, event):
        
        class NuevoPedidoHandlers:
            def nuevo_pedido_close(event):
                nuevop[NUEVO_PEDIDO_WINDOW].hide()
            def nuevo_pedido_response(id, event):
                nuevop[NUEVO_PEDIDO_WINDOW].hide()
        
        nuevop = WidgetsWrapper(NUEVO_PEDIDO_WINDOW, NuevoPedidoHandlers)


    # ---------------------------------------------- #
    # Handlers para el listado de ingreso de pedidos #
    # ---------------------------------------------- #
    
    def lista_ingreso_cursor_changed(event):
        tv = widgets[LISTA_INGRESO] 
        seleccion, iterador = tv.get_selection().get_selected()
        
        if iterador is None:
            lista_ingreso.limpiar_datos(widgets)
        else:
            pedido_id = seleccion.get_value(iterador, 1)
            lista_ingreso.cargar_datos(widgets, pedido_id)


    # --------------------------------------------- #
    # Handlers para el listado de productos         #
    # --------------------------------------------- #
    
    def lista_productos_cursor_changed(event):    
        tv = widgets[LISTA_PRODUCTOS] 
        seleccion, iterador = tv.get_selection().get_selected()
        
        if iterador is None:
            lista_productos.limpiar_datos(widgets)
        else:
            nombre_producto = seleccion.get_value(iterador, 0)
            lista_productos.cargar_datos(widgets, nombre_producto)


    # --------------------------------------------- #
    # Handlers para el listado de insumos           #
    # --------------------------------------------- #

    def lista_insumos_cursor_changed(event):    
        tv = widgets[LISTA_INSUMOS] 
        seleccion, iterador = tv.get_selection().get_selected()
        
        if iterador is None:
            lista_insumos.limpiar_datos(widgets)
        else:
            nombre_insumo = seleccion.get_value(iterador, 0)
            lista_insumos.cargar_datos(widgets, nombre_insumo)


    # --------------------------------------------- #
    # Handlers para el listado de clientes          #
    # --------------------------------------------- #

    def lista_clientes_cursor_changed(event):    
        tv = widgets[LISTA_CLIENTES] 
        seleccion, iterador = tv.get_selection().get_selected()
        
        if iterador is None:
            lista_clientes.limpiar_datos(widgets)
        else:
            nombre_cliente = seleccion.get_value(iterador, 0)
            lista_clientes.cargar_datos(widgets, nombre_cliente)


    # --------------------------------------------- #
    # Handlers para cerrar el programa              #
    # --------------------------------------------- #
    
    def ventana_cerrar_clicked(widget, event):
        gtk.main_quit()

    def archivo_salir_clicked(event):
        gtk.main_quit()



###################################################
# Main                                            #
###################################################

if __name__ == '__main__':
    
    f = open("datos.pyp", "rb")
    
    pizzeria = inicializador.Pizzeria(f)

    widgets = WidgetsWrapper(MAIN_WINDOW, MainHandlers)
    
    lista_ingreso.iniciar(widgets)
    lista_ingreso.recargar(widgets)
    lista_ingreso.iniciar_datos(widgets)

    lista_productos.iniciar(widgets)
    lista_productos.recargar(widgets)
    
    lista_insumos.iniciar(widgets)
    lista_insumos.recargar(widgets)

    gtk.main()
