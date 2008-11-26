#!/usr/bin/env python


GLADE_FILE = 'glade/pizza.glade'
import gtk
import gtk.glade

# Handlers de eventos :D
class MainHandlers:

    
    # Handlers para la ventana de "Acerca de..."
    def ayuda_acercade_clicked(event):
        
        ABOUT_WINDOW = 'acerca_de'

        class AboutHandlers:
            def acercade_close(event):
                about.get_widget(ABOUT_WINDOW).hide()
            def acercade_response(id, event):
                about.get_widget(ABOUT_WINDOW).hide()

        about = gtk.glade.XML(GLADE_FILE, ABOUT_WINDOW)
        about.get_widget(ABOUT_WINDOW).set_program_name('Pizzas & Pizzitas 1.0')
        about.signal_autoconnect(AboutHandlers.__dict__)


    # Handlers para cerrar el programa
    def ventana_cerrar_clicked(widget, event):
        gtk.main_quit()

    def archivo_salir_clicked(event):
        gtk.main_quit()


class WidgetsWrapper:
    def __init__(self, window_name):
        self.widgets = gtk.glade.XML(GLADE_FILE, window_name)
        self.widgets.signal_autoconnect(MainHandlers.__dict__)
        
    def __getitem__(self, key):
        return self.widgets.get_widget(key)


widgets = WidgetsWrapper('main_window')
gtk.main()

