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
from gui import lista_listos
from gui import lista_empanadero
from gui import lista_pizzero
from gui import nuevo_pedido

import inicializador
import creacion
import gestion
import cocina

#TODO: pop up para pedir el horno
#TODO: lista de pedidos preparados en cada horno (no esta implementado, hay que hacerlo filtrando)
#TODO: resolver el tema de ver el estado, no alcanza con listar los pedidos de cada cliente, porque hay pedidos sin clientes
#TODO: hacer que se puedan ingresar pedidos


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
            # Cuando se hace doble clic en uno de los productos posibles,
            # se incrementa en 1 la cantidad de este producto en el pedido.
            def productos_posibles_doubleclicked(treeview, path, view_column):
                tv = nuevop[PRODUCTOS_PEDIDO] 
                seleccion, iterador = tv.get_selection().get_selected()
                
                nombre_producto = seleccion.get_value(iterador, 0)
                nuevo_pedido.agregar_a_pedido(nuevop, nombre_producto)

            # Cuando se hace doble clic en uno de los productos del pedido,
            # se decrementa en 1 la cantidad de este producto en el pedido.
            def items_pedido_doubleclicked(treeview, path, view_column):
                tv = nuevop[ITEMS_PEDIDO]
                ls = tv.get_model()
                seleccion, iterador = tv.get_selection().get_selected()

                cant_producto = seleccion.get_value(iterador, 2)
                if cant_producto == 1:
                    ls.remove(iterador)
                else:
                    ls.set_value(iterador, 2, cant_producto - 1)

                nuevo_pedido.recalcular_total(nuevop)

            def tipo_pedido_changed(cb):
                cb = nuevop[NUEVO_PEDIDO_TIPO]
                num_mesa = nuevop[NUEVO_PEDIDO_MESA]


                if cb.get_active_text() != "Mesa":
                    num_mesa.set_text("")
                    num_mesa.set_sensitive(False)
                else:
                    num_mesa.set_sensitive(True)

        
        nuevop = WidgetsWrapper(NUEVO_PEDIDO_WINDOW, NuevoPedidoHandlers)
        wnd = nuevop[NUEVO_PEDIDO_WINDOW]
        wnd.hide()
        nuevo_pedido.iniciar(nuevop)
        nuevo_pedido.recargar(nuevop)
        wnd.run()
        wnd.hide()


    # ---------------------------------------------- #
    # Handlers para el listado de ingreso de pedidos #
    # ---------------------------------------------- #
    
    def lista_ingreso_cursor_changed(event):
        tv = widgets[LISTA_INGRESO] 
        seleccion, iterador = tv.get_selection().get_selected()
        
        if iterador is None:
            lista_ingreso.limpiar_datos(widgets)
        else:
            pedido_id = seleccion.get_value(iterador,0)
            lista_ingreso.limpiar_datos(widgets)
            lista_ingreso.cargar_datos(widgets, pedido_id)


    # ---------------------------------------------- #
    # Handlers para el listado de pedidos listos     #
    # ---------------------------------------------- #
    
    def lista_listos_cursor_changed(event):
        tv = widgets[LISTA_LISTOS] 
        seleccion, iterador = tv.get_selection().get_selected()
        
        if iterador is None:
            lista_listos.limpiar_datos(widgets)
        else:
            pedido_id = seleccion.get_value(iterador,0)
            lista_listos.limpiar_datos(widgets)
            lista_listos.cargar_datos(widgets, pedido_id)



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
            nombre_cliente = seleccion.get_value(iterador, 2)            
            lista_clientes.cargar_datos(widgets, nombre_cliente)


    # --------------------------------------------- #
    # Handlers para cargar y salvar estado          #
    # --------------------------------------------- #
    
    def archivo_nuevo_clicked(event):
        # TODO: cargar un sistema vacio
        pass

    def archivo_abrir_clicked(event):
        abrir = WidgetsWrapper(ABRIR_WINDOW)
        wnd = abrir[ABRIR_WINDOW]
        wnd.hide()
        res = wnd.run()
        wnd.hide()
        if res == gtk.RESPONSE_OK:
            fname = wnd.get_filename()
            # TODO: cargar el sistema desde el archivo
        elif res == gtk.RESPONSE_CANCEL or \
             res == gtk.RESPONSE_DELETE_EVENT:
            return
        else:
            raise ValueError("Respuesta no esperada al dialogo de abrir!")


    def archivo_guardar_como_clicked(event):
        guardar = WidgetsWrapper(GUARDAR_WINDOW)
        wnd = guardar[GUARDAR_WINDOW]
        wnd.hide()
        res = wnd.run()
        wnd.hide()
        if res == gtk.RESPONSE_OK:
            fname = wnd.get_filename()
            # TODO: guardar el sistema al archivo
        elif res == gtk.RESPONSE_CANCEL or \
             res == gtk.RESPONSE_DELETE_EVENT:
            return
        else:
            raise ValueError("Respuesta no esperada al dialogo de guardar!")


    # --------------------------------------------- #
    # Handlers para cerrar el programa              #
    # --------------------------------------------- #
    
    def ventana_cerrar_clicked(widget, event):
        gtk.main_quit()

    def archivo_salir_clicked(event):
        gtk.main_quit()

    # --------------------------------------------- #
    # Handlers para el boton de preparado pizzero   #
    # --------------------------------------------- #
 

    def pizzas_preparadas_clicked(event): 
        distribuidor.terminarPreparacionPizzas()
  


    # --------------------------------------------- #
    # Handlers para el boton de preparado pizzero   #
    # --------------------------------------------- #


    def empanadas_preparadas_clicked(event): 
        print "me apretaron"
        distribuidor.terminarPreparacionEmpanadas()

###################################################
# Main                                            #
###################################################
    
if __name__ == '__main__':
    
    f = open("datos.pyp", "rb")
    pizzeria = inicializador.Pizzeria(f)
    widgets = WidgetsWrapper(MAIN_WINDOW, MainHandlers)
    
    from gui import general
    general.iniciar(widgets)
    general.recargar(widgets)

    # Conecto observers y callbacks
    distribuidor = general.DistribuidorCallbacks(widgets,pizzeria)
    pizzeria.getContStock().suscribir(distribuidor.modifStock)
    pizzeria.getContListos().suscribir(distribuidor.modifListos)
    pizzeria.getContIng().suscribir(distribuidor.modifIngreso)
    pizzeria.getPreparadorEmpanadero().suscribir(distribuidor.prepararEmpanadas)
    pizzeria.getPreparadorPizzero().suscribir(distribuidor.prepararPizzas)
    pizzeria.getAsignador().asignarCallback(distribuidor.pedirHorno)
    # Hardcodeo un par de pedidos para probar si va funcionando
    pizzeria.getCoordP().ingresarPedido(None,[x for x in pizzeria.productos if x.getTipo() == pizzeria.coca][0:1],None,"mesa",2)
    pizzeria.getCoordP().ingresarPedido(pizzeria.clientes[0],[x for x in pizzeria.productos if x.getTipo() == pizzeria.birra][0:1],"efectivo","telefono",None)
    pizzeria.getCoordP().ingresarPedido(None,pizzeria.productos,"efectivo", "mostrador",None)
    pizzeria.getCoordP().ingresarPedido(None,pizzeria.productos,"efectivo", "mostrador",None)
    pizzeria.getCoordP().ingresarPedido(None,pizzeria.productos,"efectivo", "mostrador",None)
    pizzeria.getCoordP().ingresarPedido(None,pizzeria.productos,"efectivo", "mostrador",None)
    pizzeria.getCoordP().ingresarPedido(None,pizzeria.productos,"efectivo", "mostrador",None)
    pizzeria.getCoordP().ingresarPedido(None,pizzeria.productos,"efectivo", "mostrador",None)
    pizzeria.getCoordP().ingresarPedido(None,pizzeria.productos,"efectivo", "mostrador",None)
    pizzeria.getCoordP().ingresarPedido(None,pizzeria.productos,"efectivo", "mostrador",None)
    pizzeria.getCoordP().ingresarPedido(None,pizzeria.productos,"tarjeta", "mostrador",None)
    pizzeria.getCoordP().ingresarPedido(None,[x for x in pizzeria.productos if x.nombre == "Quilmes"],"efectivo", "mostrador",None)
    print [x.getId() for x in pizzeria.productos]
    
    #-------------------------------------------------------#

    gtk.main()
    