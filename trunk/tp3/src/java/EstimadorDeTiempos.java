

/**
 * @author Federico
 * @version 1.0
 * @created 23-Nov-2008 13:11:34
 */
public abstract  class EstimadorDeTiempos {

	public EstimadorDeTiempos(){

	}

	public void finalize() throws Throwable {

	}

	/**
	 *
	 * @param Pedido
	 */
	public abstract double estimarTiempo(Pedido pedido );

}