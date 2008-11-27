import java.util.List;




public abstract class AsignadorDeHorno {

	protected Horno hornoP;
	protected Horno hornoE;
	protected TipoProducto pizza;
	protected TipoProducto empanada;

	public AsignadorDeHorno(Horno p, Horno e,TipoProducto Pizza, TipoProducto Empanada ){
          this.hornoP=p;
          this.hornoE=e;
          this.pizza=Pizza;
          this.empanada=Empanada;
	}

	public void finalize() throws Throwable {

	}

	/**
	 *
	 * @param Pedido
	 */
	public abstract void asignarHorno(Pedido pedido);

}