import java.util.LinkedList;
import java.util.List;



/**
 * @author Federico
 * @version 1.0
 * @created 23-Nov-2008 13:00:09
 */
public abstract class ControladorDeIngreso {

	protected CoordinadorDeCocina coordinadorDeCocina;
	protected List<Pedido> listaIngreso;

	public ControladorDeIngreso(CoordinadorDeCocina coordinadorDeCocina){
		this.coordinadorDeCocina=coordinadorDeCocina;
		listaIngreso=new LinkedList<Pedido>(); 
	}

	public void finalize() throws Throwable {

	}

	/**
	 *
	 * @param p
	 */
	public abstract void encolarPedido(Pedido p);

	/**
	 *
	 * @param p
	 */
	public abstract void ingresar(Pedido p);

	public abstract List<Pedido> listarPedidos();
	/**
	 *
	 * @param tp
	 */
	public abstract Pedido proximoPedido(TipoProducto tp);


}