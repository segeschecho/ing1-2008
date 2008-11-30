#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

import gtk.glade

from config import *

###################################################
# Helper para widgets GTK2                        #
###################################################

class WidgetsWrapper:
    def __init__(self, window_name, handlers=None):
        self.widgets = gtk.glade.XML(GLADE_FILE, window_name)
        self.window_name = window_name
        if not handlers is None:
            self.widgets.signal_autoconnect(handlers.__dict__)
        
    def __getitem__(self, key):
        return self.widgets.get_widget(key)



###################################################
# Helper para mostrar errores                     #
###################################################

def mostrar_error(titulo, texto):
    error = WidgetsWrapper(ERROR_WINDOW)
    wnd = error[ERROR_WINDOW]
    wnd.hide()
    error[ERROR_MSG].set_markup("<b>%s</b>\n%s" % (titulo, texto))
    wnd.run()
    wnd.destroy()

