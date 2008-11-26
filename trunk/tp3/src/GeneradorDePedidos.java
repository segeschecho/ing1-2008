import java.util.List;



/**
 * @author Federico
 * @version 1.0
 * @created 23-Nov-2008 13:04:53
 */
public abstract class GeneradorDePedidos {

	protected CalculadorDePrecios calculadorDePrecios;
	protected EstimadorDeTiempos estimadorDeTiempos;
	protected ControladorDeStock controladorDeStock;
	protected AsignadorDeHorno asignadorDeHorno;

	public GeneradorDePedidos(CalculadorDePrecios calculadorDePrecios,
	EstimadorDeTiempos estimadorDeTiempos,
	ControladorDeStock controladorDeStock,
	AsignadorDeHorno asignadorDeHorno){
		this.asignadorDeHorno=asignadorDeHorno;
		this.calculadorDePrecios=calculadorDePrecios;
		this.controladorDeStock=controladorDeStock;
		this.estimadorDeTiempos=estimadorDeTiempos;

	}

	public void finalize() throws Throwable {

	}

	protected abstract int generarId();

	/**
	 *
	 * @param c
	 * @param m
	 * @param formaDePago
	 * @param origen
	 * @throws ExcepcionOrigenDesconocido
	 * @throws ClienteNuloTelefono
	 * @throws ExcepcionProductoInsat
	 */
	public abstract Pedido generarPedido(Cliente c, List<Producto> m, String formaDePago, String origen,int mesa) throws ExcepcionOrigenDesconocido, ClienteNuloTelefono, ExcepcionProductoInsat;

}