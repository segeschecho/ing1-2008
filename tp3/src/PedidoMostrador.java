import java.util.Date;
import java.util.List;


/**
 * @author Administrador
 * @version 1.0
 * @created 16-Nov-2008 22:40:49
 */
public class PedidoMostrador extends PedidoLocal {

	public PedidoMostrador(int id, Cliente cliente,List<Producto> productos,String formaDePago,String fechaIngreso){

		super( id, cliente, productos, formaDePago, fechaIngreso);
	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}