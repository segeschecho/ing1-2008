import java.util.Date;
import java.util.List;



/**
 * @author Administrador
 * @version 1.0
 * @created 25-Nov-2008 09:52:10
 */
public class PedidoTelefono extends PedidoRemoto {

	public PedidoTelefono(int id, Cliente cliente,List<Producto> productos,String formaDePago,String fechaIngreso){
		super( id, cliente, productos, formaDePago, fechaIngreso);
	}


	public void finalize() throws Throwable {
		super.finalize();
	}

}