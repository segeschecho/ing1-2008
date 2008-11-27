import java.util.List;
import java.util.ListIterator;



/**
 * @author Federico
 * @version 1.0
 * @created 23-Nov-2008 12:59:49
 */
public class ControladorDeIngresoStandard extends ControladorDeIngreso {


	public ControladorDeIngresoStandard(CoordinadorDeCocina coordinadorDeCocina){
              super(coordinadorDeCocina);
	}

	public void finalize() throws Throwable {
		super.finalize();
	}


	/**
	 *
	 * @param p
	 */
	public void encolarPedido(Pedido p){
		this.listaIngreso.add(p);
	}

	/**
	 *
	 * @param p
	 */
	public void ingresar(Pedido p){
      boolean res=this.coordinadorDeCocina.prepararPedido(p);
      if(! res){
    	  p.setEstado(Estado.Ingresado);
    	  this.encolarPedido(p);
    	  System.out.println("Aca hay que hacer un notify de ingreso");
    	  //TODO: hacer la parte del observer
      }

	}

	public List<Pedido> listarPedidos(){
		return this.listaIngreso;
	}

	/**
	 *
	 * @param tp
	 */
	public Pedido proximoPedido(TipoProducto tp){
		ListIterator<Pedido> it = this.listaIngreso.listIterator();
		Pedido ped=null;
		Pedido pedActual;
		boolean sirve;
		while(it.hasNext() && ped==null){
			pedActual = it.next();
			sirve=this.tieneTipo(pedActual, tp);
			if(sirve){
				it.remove();
				ped=pedActual;
				System.out.println("ACA hay que hacer un notify");
				//TODO: hacer un notify
			}

		}
		return ped;
	}


	/**
	 *
	 * @param p
	 * @param tp
	 */
	private boolean tieneTipo(Pedido p, TipoProducto tp){
		ListIterator<Producto> it = p.getProductos().listIterator();
		boolean res=false;
		Producto pr;
		while(it.hasNext() && res==false){
			pr=it.next();
			res=pr.getTipo().equals(tp);
		}
		return res;
	}

}