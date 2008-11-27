import java.util.List;
import java.util.Map;

/**
 * @author Administrador
 * @version 1.0
 * @created 16-Nov-2008 22:40:45
 */
public class FraccionadorDeHorno {

	private Map<TipoProducto,Integer> prodsXModulo;

	public FraccionadorDeHorno(Map<TipoProducto,Integer> prodsXModulo){
		this.prodsXModulo=prodsXModulo;
	}

	public void finalize() throws Throwable {

	}

	/**
	 *
	 * @param TipoProducto
	 */
	public int getProductosPorModulo(TipoProducto tipoProducto ){
		return prodsXModulo.get(tipoProducto);
	}

	/**
	 *
	 * @param producto
	 */

	/**
	 *
	 * @param p
	 */
	public List< List<Producto> > partirPedido(Pedido p){
		return null;
	}

}