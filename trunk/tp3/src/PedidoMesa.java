import java.util.Date;
import java.util.List;



/**
 * @author Administrador
 * @version 1.0
 * @created 25-Nov-2008 09:52:16
 */
public class PedidoMesa extends PedidoLocal {

	private int mesa;

	public PedidoMesa(int id, Cliente cliente,List<Producto> productos,
			          String formaDePago,String fechaIngreso,int mesa){
		super( id, cliente, productos, formaDePago, fechaIngreso);
		this.mesa=mesa;
	}

	public void finalize() throws Throwable {
		super.finalize();
	}

	public int getMesa(){
		return this.mesa;
	}

	/**
	 *
	 * @param formaDePago
	 */
	public void setFormaDePago(String formaDePago){

	}

}