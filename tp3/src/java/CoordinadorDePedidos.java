import java.util.List;
class PedidoNulo extends Exception {}
class ProductosVacios extends Exception {}

/**
 * @author Federico
 * @version 1.0
 * @created 23-Nov-2008 13:01:09
 */
public class CoordinadorDePedidos {

	private GeneradorDePedidos generadorDePedidos;
	private ControladorDePreIngreso controladorDePreIngreso;
    private ControladorDeListos controladorDeListos;
	public CoordinadorDePedidos(
			GeneradorDePedidos generadorDePedidos,
			ControladorDePreIngreso controladorDePreIngreso,
		    ControladorDeListos controladorDeListos){
		this.generadorDePedidos=generadorDePedidos;
		this.controladorDeListos=controladorDeListos;
		this.controladorDePreIngreso=controladorDePreIngreso;
	}

	public void finalize() throws Throwable {

	}

	/**
	 *
	 * @param p
	 */
	public void agregarPedidoListo(Pedido p){
           this.controladorDeListos.agregarPedidoListo(p);
	}


	/**
	 *
	 * @param c
	 * @param productos
	 * @param tipoOrigen
	 * @param formaDePago
	 * @param origen
	 * @param mesa
	 * @throws ProductosVacios
	 * @throws PedidoNulo
	 * @throws ClienteNuloTelefono
	 * @throws ExcepcionOrigenDesconocido
	 * @throws ExcepcionProductoInsat
	 */
	public void ingresarPedido(Cliente c, List<Producto> productos,String formaDePago, String origen, int mesa) throws ProductosVacios, PedidoNulo, ExcepcionOrigenDesconocido, ClienteNuloTelefono, ExcepcionProductoInsat{
         if(productos.isEmpty()){
        	 throw new ProductosVacios();
         }
		 Pedido p = this.generadorDePedidos.generarPedido(c, productos, formaDePago, origen,mesa);
         if(p != null){
        	 this.controladorDePreIngreso.ingresar(p);
         }
         else{
        	 throw new PedidoNulo();
         }

	}

	public GeneradorDePedidos getGeneradorDePedidos() {
		return generadorDePedidos;
	}

	public void setGeneradorDePedidos(GeneradorDePedidos generadorDePedidos) {
		this.generadorDePedidos = generadorDePedidos;
	}

	public ControladorDePreIngreso getControladorDePreIngreso() {
		return controladorDePreIngreso;
	}

	public void setControladorDePreIngreso(
			ControladorDePreIngreso controladorDePreIngreso) {
		this.controladorDePreIngreso = controladorDePreIngreso;
	}

	public ControladorDeListos getControladorDeListos() {
		return controladorDeListos;
	}

	public void setControladorDeListos(ControladorDeListos controladorDeListos) {
		this.controladorDeListos = controladorDeListos;
	}







}