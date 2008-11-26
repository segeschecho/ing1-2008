

/**
 * @author Administrador
 * @version 1.0
 * @created 16-Nov-2008 22:40:44
 */
public class CoordinadorDeCocina {

	private ControladorDeIngreso controladorDeIngreso;
	private CoordinadorDePedidos coordinadorDePedidos;
	private DespachadorDePreparacion despachadorDePreparacion;

	public CoordinadorDeCocina(ControladorDeIngreso controladorDeIngreso,
			CoordinadorDePedidos coordinadorDePedidos,
			DespachadorDePreparacion despachadorDePreparacion){
		this.controladorDeIngreso=controladorDeIngreso;
		this.coordinadorDePedidos=coordinadorDePedidos;
		this.despachadorDePreparacion=despachadorDePreparacion;
	}

	public void finalize() throws Throwable {

	}

	/**
	 *
	 * @param p
	 */
	public void cocinar(Pedido p){
              p.setEstado(Estado.Preparado);
	}

	/**
	 *
	 * @param tp
	 */
	public Pedido conseguirPedido(TipoProducto tp){
		return this.controladorDeIngreso.proximoPedido(tp);
	}

	/**
	 *
	 * @param p
	 */
	public void pedidoListo(Pedido p){

	}

	/**
	 *
	 * @param p
	 */
	public boolean prepararPedido(Pedido p){
		return despachadorDePreparacion.prepararPedido(p);
	}



	public void setControladorDeIngreso(ControladorDeIngreso controladorDeIngreso) {
		this.controladorDeIngreso = controladorDeIngreso;
	}



	public void setCoordinadorDePedidos(CoordinadorDePedidos coordinadorDePedidos) {
		this.coordinadorDePedidos = coordinadorDePedidos;
	}


	public void setDespachadorDePreparacion(
			DespachadorDePreparacion despachadorDePreparacion) {
		this.despachadorDePreparacion = despachadorDePreparacion;
	}

}