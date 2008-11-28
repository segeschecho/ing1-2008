#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

import gtk.glade

from config import *

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



