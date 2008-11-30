from config import *
import gobject
import gtk
def iniciar(widgets):
    tv = widgets[LISTA_HORNO_EMPANADERO]
    
    # Armo el ListStore
    ls = gtk.ListStore(gobject.TYPE_INT,
                      )
    tv.set_model(ls)
    
    # Armo las columnas
    tv.append_column(gtk.TreeViewColumn("Id",       gtk.CellRendererText(),  text=0))
    

def recargar(widgets,despCocc=None):
    tv = widgets[LISTA_HORNO_EMPANADERO]
    ls = tv.get_model() 
    ls.clear()  
    if despCocc != None:
	    peds = despCocc.getColaEmp()

	    for each in peds:
		it = ls.insert(0)
		ls.set_value(it, 0, each.getId())
		
		

def limpiar(widgets):
    tv = widgets[LISTA_HORNO_EMPANADERO]
    ls = tv.get_model()
    ls.clear()
