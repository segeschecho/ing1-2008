import java.util.ListIterator;



/**
 * @author Administrador
 * @version 1.0
 * @created 16-Nov-2008 22:40:36
 */
public class CalculadorDePreciosStandard extends CalculadorDePrecios {

	public CalculadorDePreciosStandard(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

	/**
	 *
	 * @param Pedido
	 */
	public float calcularPrecio(Pedido pedido){
		ListIterator<Producto> it = pedido.getProductos().listIterator();
		Producto pr;
		float precio=0;
		while(it.hasNext()){
			pr=it.next();
			precio+=pr.getPrecio();
		}
		return precio;

	}


}