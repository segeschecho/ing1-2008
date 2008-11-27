import java.util.Date;
import java.util.List;
import java.util.Date;
import java.text.DateFormat;
import java.text.SimpleDateFormat;


class ExcepcionOrigenDesconocido extends Exception{
	String origen;
	public ExcepcionOrigenDesconocido(String or){
		this.origen=or;
	}

}
class ClienteNuloTelefono extends Exception{}


/**
 * @author Federico
 * @version 1.0
 * @created 16-Nov-2008 22:40:45
 */
public class GeneradorDePedidosStandard extends GeneradorDePedidos {

	private int ultimoIdAsignado;

	public GeneradorDePedidosStandard(
			CalculadorDePrecios calculadorDePrecios,
			EstimadorDeTiempos estimadorDeTiempos,
			ControladorDeStock controladorDeStock,
			AsignadorDeHorno asignadorDeHorno){

		    super(calculadorDePrecios, estimadorDeTiempos,
	              controladorDeStock, asignadorDeHorno);
		    this.ultimoIdAsignado=0;

	}

	private String getDateTime() {
	    DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
	    Date date = new Date();
	    return dateFormat.format(date);
	}

	public void finalize() throws Throwable {
		super.finalize();
	}

	protected int generarId(){
		int res=this.ultimoIdAsignado;
		this.ultimoIdAsignado++;
		return res;
	}





	@Override
	public Pedido generarPedido(Cliente c, List<Producto> productos,
			String formaDePago, String origen,int mesa) throws ExcepcionOrigenDesconocido, ClienteNuloTelefono, ExcepcionProductoInsat {
		if(controladorDeStock.verificarEIngresar(productos)){
			String d=this.getDateTime();
			int ID = this.generarId();
			Pedido p;
			if(origen == "mostrador"){
				p=new PedidoMostrador(ID,c,productos,formaDePago,d);
			}
			else if(origen == "mesa"){
				p=new PedidoMesa(ID,c,productos,formaDePago,d,mesa);
			}
			else if(origen == "telefono"){
				if(c==null){
					throw new ClienteNuloTelefono();
				}
				p=new PedidoTelefono(ID,c,productos,formaDePago,d);
			}
			else{
				throw new ExcepcionOrigenDesconocido(origen);
			}
			this.asignadorDeHorno.asignarHorno(p);
			p.setTiempoEstimado(this.estimadorDeTiempos.estimarTiempo(p));
			p.setPrecio(this.calculadorDePrecios.calcularPrecio(p));
			return p;
		}
		return null;

	}

}