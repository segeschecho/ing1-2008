


public abstract class CalculadorDePrecios {

	public CalculadorDePrecios(){

	}

	public void finalize() throws Throwable {

	}

	/**
	 *
	 * @param Pedido
	 */
	public abstract float calcularPrecio(Pedido pedido);

}