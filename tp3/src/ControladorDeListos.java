import java.util.LinkedList;
import java.util.List;



/**
 * @author Administrador
 * @version 1.0
 * @created 25-Nov-2008 09:50:55
 */
public class ControladorDeListos {

	private List<Pedido> listos;

	public ControladorDeListos(){
           listos = new LinkedList<Pedido>();
	}

	public void finalize() throws Throwable {

	}

	/**
	 *
	 * @param p
	 */
	public void agregarPedidoListo(Pedido p){
            listos.add(p);
            System.out.println("notificar pedido listo");
            //TODO: aca hay q ue avisar que hay un pedido listo nuevo
	}


	/**
	 *
	 * @param p
	 */
	public void despacharPedido(PedidoRemoto p){

	}

	/**
	 *
	 * @param p
	 */
	public void despacharPedido(PedidoMostrador p){

	}

	/**
	 *
	 * @param p
	 */
	public void despacharPedido(PedidoMesa p){

	}



}