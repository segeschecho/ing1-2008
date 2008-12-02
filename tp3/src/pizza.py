#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

import gtk

from gui.config import *
from gui.helpers import WidgetsWrapper

from gui import lista_ingreso
from gui import lista_insumos
from gui import lista_clientes
from gui import lista_productos
from gui import lista_todos
from gui import lista_listos
from gui import lista_empanadero
from gui import lista_pizzero
from gui import lista_horno_empanadero
from gui import lista_horno_pizzero
from gui import nuevo_pedido
import pickle

import inicializador
import creacion
import gestion
import cocina

#TODO: #TODO: #TODO: resolver el tema de ver el estado, no alcanza con listar los pedidos de cada cliente, porque hay pedidos sin clientes



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

            # Este handler se encarga de deshabilitar el GtkEntry donde
            # se especifica el número de mesa y el de forma de pago si 
            # no corresponde (por ejemplo, si el pedido es delivery no tiene mesa)
            def tipo_pedido_changed(cb):
                cb = nuevop[NUEVO_PEDIDO_TIPO]
                num_mesa = nuevop[NUEVO_PEDIDO_MESA]
                forma_pedido = nuevop[NUEVO_PEDIDO_FORMA_PAGO]

                eleccion = cb.get_active_text()
                if eleccion != "Mesa":
                    # Deshabilito la entrada de número de mesa
                    num_mesa.set_sensitive(False)
                    num_mesa.set_active(-1)
                    
                    # Habilito la entrada de forma de pago
                    if eleccion == "Teléfono":
                        forma_pedido.set_sensitive(False)
                        forma_pedido.set_active(0)
                    elif eleccion == "Mostrador":
                        forma_pedido.set_sensitive(True)
                        forma_pedido.set_active(0)
                    
                else:
                    # Habilito la entrada de número de mesa
                    num_mesa.set_sensitive(True)
                    num_mesa.set_active(-1)
                    # Deshabilito la entrada de forma de pago
                    forma_pedido.set_sensitive(False)
                    forma_pedido.set_active(-1)


        
        nuevop = WidgetsWrapper(NUEVO_PEDIDO_WINDOW, NuevoPedidoHandlers)
        wnd = nuevop[NUEVO_PEDIDO_WINDOW]
        wnd.hide()
        nuevo_pedido.iniciar(nuevop)
        nuevo_pedido.recargar(nuevop)
        
        datos = None

        while True:
            res = wnd.run()
            if res == gtk.RESPONSE_DELETE_EVENT or \
               res == gtk.RESPONSE_CANCEL:
                break
            elif res == gtk.RESPONSE_OK:
                try:
                    datos = nuevo_pedido.validar_pedido(nuevop)
                    
                    # intento ingresar el pedido
                    try: 
                        pizzeria.getCoordP().ingresarPedido(*datos)
                    except creacion.ProductoInsatisfacible, e:
                        nuevo_pedido.mostrar_error("Producto Insatisfacible", str(e))
                        continue
                    
                    break
                
                except nuevo_pedido.ErrorDeValidacion:
                    pass
            else:
                raise ValueError("Salida inesperada del diálogo de nuevo pedido!")

        wnd.hide()

        if datos != None:
            lista_ingreso.recargar(widgets, pizzeria.getContIng())
            lista_insumos.recargar(widgets)


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


    # -------------------------------------------------------- #
    # Handlers para el listado de ingreso de todos los pedidos #
    # -------------------------------------------------------- #


    def lista_todos_cursor_changed(event):
        tv = widgets[LISTA_TODOS] 
        seleccion, iterador = tv.get_selection().get_selected()
        
        if iterador is None:
            lista_todos.limpiar_datos(widgets)
        else:
            pedido_id = seleccion.get_value(iterador,0)
            lista_todos.limpiar_datos(widgets)
            lista_todos.cargar_datos(widgets, pedido_id)

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
            
            try:
                 fi = open(fname, 'rb')
            except Exception, e:
                  nuevo_pedido.mostrar_error("Error al cargar", str(e))
                  return
                  

            #Hago un backup del estado actual por si hay un error al abrir el archivo
            (backUpPedido, backUpInsumo,backUpProducto,
            backUpTipoProducto, backUpCliente) = backUp()
            global pizzeria
            global distribuidor
            backUpPizzeroa = pizzeria
            try:
                pizzeria = pickle.load(fi)
            except:
                creacion.Pedido.setAllInstances(backUpPedido)
                creacion.Insumo.setAllInstances(backUpInsumo)
                creacion.Producto.setAllInstances(backUpProducto)
                creacion.TipoProducto.setAllInstances(backUpTipoProducto)
                creacion.Cliente.setAllInstances(backUpCliente)
                pizzeria = backUpPizzeria
            distribuidor = general.DistribuidorCallbacks(widgets,pizzeria)
            
            conectarCallbacks()
            general.recargar(widgets)
            distribuidor.actualizarGui()

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
            if not fname.endswith('.pyp'):
                fname += '.pyp'
            
            pizzeria.clearObservers()
            try:
                pickle.dump(pizzeria, open("fname", 'wb'))
            except:
                nuevo_pedido.mostrar_error("Error al cargar", str(e))
                return
            # TODO: mover esto a general.py y pasarle los parametros
            conectarCallbacks()

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

    # ----------------------------------------------- #
    # Handlers para los botones de fin de preparación #
    # ----------------------------------------------- #

    def pizzas_preparadas_clicked(event): 
        distribuidor.terminarPreparacionPizzas()
 

    def empanadas_preparadas_clicked(event): 
        distribuidor.terminarPreparacionEmpanadas()

    def cocinado_empanadero_clicked(event):
        distribuidor.cocinarEmpanadas()
    
    def cocinado_pizzero_clicked(event):
        print "me apretaron, pobre de mi"
        distribuidor.cocinarPizzas()

    

def backUp():
            backUpPedido = creacion.Pedido.allInstances()
            backUpInsumo = creacion.Insumo.allInstances()
            backUpProducto= creacion.Producto.allInstances()
            backUpTipoProducto = creacion.TipoProducto.allInstances()
            backUpCliente = creacion.Cliente.allInstances()
            creacion.Pedido.reinit()
            creacion.Insumo.reinit()
            creacion.Producto.reinit()
            creacion.TipoProducto.reinit()
            creacion.Cliente.reinit()    
            return (backUpPedido,backUpInsumo,backUpProducto,backUpTipoProducto,backUpCliente)

def conectarCallbacks(): 
    global pizzeria
    global distribuidor  
    pizzeria.getContStock().suscribir(distribuidor.modifStock)
    pizzeria.getContStock().suscribir(distribuidor.nuevosCriticos)
    pizzeria.getContListos().suscribir(distribuidor.modifListos)
    pizzeria.getContListos().suscribir(distribuidor.recargarClientes)
    pizzeria.getContIng().suscribir(distribuidor.modifIngreso)
    pizzeria.getContIng().suscribir(distribuidor.recargarClientes)
    pizzeria.getPreparadorEmpanadero().suscribir(distribuidor.prepararEmpanadas)
    pizzeria.getPreparadorPizzero().suscribir(distribuidor.prepararPizzas)
    pizzeria.getAsignador().asignarCallback(distribuidor.pedirHorno)
    pizzeria.getDespachadorDeCoccion().suscribir(distribuidor.modifHornoPizzero)
    pizzeria.getDespachadorDeCoccion().suscribir(distribuidor.recargarClientes)
    pizzeria.getDespachadorDeCoccion().suscribir(distribuidor.modifHornoEmpanadero)
    pizzeria.getDespachadorDeCoccion().suscribir(distribuidor.recargarClientes)

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
    distribuidor = general.DistribuidorCallbacks(widgets,pizzeria)
    # Conecto observers y callbacks
    conectarCallbacks()
     

    # Hardcodeo un par de pedidos para probar si va funcionando
    #pizzeria.getCoordP().ingresarPedido(None,[x for x in pizzeria.productos if x.getTipo() == pizzeria.coca][0:1],None,"mesa",2)
    #pizzeria.getCoordP().ingresarPedido(pizzeria.clientes[0],[x for x in pizzeria.productos if x.getTipo() == pizzeria.birra][0:1],"efectivo","telefono",None)
   # pizzeria.getCoordP().ingresarPedido(None,pizzeria.productos,"efectivo", "mostrador",None)
  #  pizzeria.getCoordP().ingresarPedido(None,pizzeria.productos,"efectivo", "mostrador",None)
 #   pizzeria.getCoordP().ingresarPedido(None,pizzeria.productos,"efectivo", "mostrador",None)
#    pizzeria.getCoordP().ingresarPedido(None,pizzeria.productos,"efectivo", "mostrador",None)
    #pizzeria.getCoordP().ingresarPedido(None,pizzeria.productos,"efectivo", "mostrador",None)
    #pizzeria.getCoordP().ingresarPedido(None,pizzeria.productos,"efectivo", "mostrador",None)
    #pizzeria.getCoordP().ingresarPedido(None,pizzeria.productos,"efectivo", "mostrador",None)
    #pizzeria.getCoordP().ingresarPedido(None,pizzeria.productos,"efectivo", "mostrador",None)
    #pizzeria.getCoordP().ingresarPedido(None,pizzeria.productos,"tarjeta", "mostrador",None)
    #pizzeria.getCoordP().ingresarPedido(None,[x for x in pizzeria.productos if x.nombre == "Quilmes"],"efectivo", "mostrador",None)


    # Loop principal
    gtk.main()
    
