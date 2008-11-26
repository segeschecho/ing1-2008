import java.util.List;



/**
 * @author Gonzalo
 * @version 1.0
 * @created 23-Nov-2008 13:13:14
 */
public interface ControladorDeStock {

	/**
	 *
	 * @param producto
	 */
	public boolean ingresar(Producto producto);


	/**
	 *
	 * @param productos
	 */
	public void obtenerCriticos(List<Producto> productos);

	/**
	 *
	 * @param productos
	 */
	public void reestablecerStock(List<Producto> productos);

	public void reestablecerStockInsumos(List<Insumo> insumos);
	/**
	 *
	 * @param productos
	 * @throws ExcepcionProductoInsat
	 */
	public boolean verificarEIngresar(List<Producto> productos) throws ExcepcionProductoInsat;

}