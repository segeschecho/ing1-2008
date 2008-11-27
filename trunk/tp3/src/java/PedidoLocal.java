import java.util.Date;
import java.util.List;



/**
 * @author Federico
 * @version 1.0
 * @created 25-Nov-2008 09:52:47
 */
public class PedidoLocal extends Pedido {

	public PedidoLocal(int id, Cliente cliente,List<Producto> productos,String formaDePago,String fechaIngreso){
		super( id, cliente, productos, formaDePago, fechaIngreso);


	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}