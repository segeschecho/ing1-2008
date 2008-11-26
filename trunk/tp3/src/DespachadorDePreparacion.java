

/**
 * @author Federico
 * @version 1.0
 * @created 23-Nov-2008 12:37:43
 */
public abstract class DespachadorDePreparacion {
    Preparador prepPizzero;
    Preparador prepEmpanadero;
    CoordinadorDeCocina coordinador;
	public DespachadorDePreparacion(Preparador prePizzero, Preparador prepEmPanadero,
			                        CoordinadorDeCocina coordinador){
		this.prepEmpanadero=prepEmPanadero;
		this.prepPizzero=prePizzero;
		this.coordinador=coordinador;

	}

	public void finalize() throws Throwable {

	}


	/**
	 *
	 * @param p
	 */
	public abstract boolean prepararPedido(Pedido p);

}