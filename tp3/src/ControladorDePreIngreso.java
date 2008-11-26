import java.util.Iterator;
import java.util.List;



/**
 * @author Federico
 * @version 1.0
 * @created 16-Nov-2008 22:40:43
 */
public class ControladorDePreIngreso {

	private ControladorDeIngreso controladorDeIngreso;
	private CoordinadorDePedidos coordinadorDePedidos;
	public ControladorDePreIngreso(CoordinadorDePedidos coordinadorDePedidos,
			ControladorDeIngreso controladorDeIngreso){
		this.controladorDeIngreso=controladorDeIngreso;
		this.coordinadorDePedidos=coordinadorDePedidos;
	}

	public void finalize() throws Throwable {

	}

	/**
	 *
	 * @param p
	 */
	public boolean determinarCocinable(Pedido p){
		List<Producto> productos = p.getProductos();
        Iterator<Producto> it=productos.iterator();
        boolean res= false;
        Producto pr;
        TipoProducto tp;
        while(it.hasNext()&& ! res){
        	pr=it.next();
        	tp=pr.getTipo();
        	res=res || tp.getCocinable();
        }
        return res;
	}

	/**
	 *
	 * @param p
	 */
	public boolean determinarPreparable(Pedido p){
		List<Producto> productos = p.getProductos();
        Iterator<Producto> it=productos.iterator();
        boolean res= false;
        Producto pr;
        TipoProducto tp;
        while(it.hasNext()&& ! res){
        	pr=it.next();
        	tp=pr.getTipo();
        	res=res || tp.getPreparable();
        }
        return res;
	}

	/**
	 *
	 * @param p
	 */
	public void ingresar(Pedido p){
          if(this.determinarPreparable(p) || this.determinarCocinable(p)){
        	  this.controladorDeIngreso.ingresar(p);

          }
          else{
        	  this.coordinadorDePedidos.agregarPedidoListo(p);
          }

	}

}