import java.util.List;
import java.util.ListIterator;



/**
 * @author Federico
 * @version 1.0
 * @created 16-Nov-2008 22:40:44
 */
public class EstimadorStandard extends EstimadorDeTiempos {

	public TipoProducto pizza;
	public TipoProducto empanada;

	public EstimadorStandard(TipoProducto pizza, TipoProducto empanada){
		super();
		this.pizza=pizza;
		this.empanada=empanada;

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

	/**
	 *
	 * @param Pedido
	 */
	public double estimarTiempo( Pedido pedido){
		double tiempoPreparacion=0;
		double tiempoCoccionPizzas=0;
		double tiempoCoccionEmpanadas=0;
		Horno h=pedido.getHorno();
		ListIterator<Pedido> it = Pedido.allInstances().listIterator();
		Pedido p;
		while(it.hasNext()){
			p=it.next();
			tiempoPreparacion+=this.estimarTiempoDePreparacion(p);
			tiempoCoccionPizzas+=this.estimarTiempoDeCoccionPizzas(p, h);
			tiempoCoccionEmpanadas+=this.estimarTiempoDeCoccionEmpanadas(p, h);
		}
		tiempoPreparacion+=estimarTiempoDePreparacionActual(pedido);
		tiempoCoccionPizzas+=estimarTiempoDeCoccionPizzasActual(pedido,h);
		tiempoCoccionEmpanadas+=estimarTiempoDeCoccionEmpanadasActual(pedido,h);
		int modulos = h.getCantModulos();
		FraccionadorDeHorno frac = h.getFraccionadorDeHorno();
		int cantEmpanadas = frac.getProductosPorModulo(this.empanada);
		int cantPizzas = frac.getProductosPorModulo(this.pizza);
		double res = tiempoPreparacion+(tiempoCoccionPizzas/(cantPizzas*modulos))+
		      (tiempoCoccionEmpanadas/(cantEmpanadas*modulos));
		return res;

	}

	private double estimarTiempoDeCoccionEmpanadasActual(Pedido pedido,Horno h) {
		ListIterator<Producto> it = pedido.getProductos().listIterator();
		double res= 0;
		Producto pr;
		while(it.hasNext()){
			pr=it.next();
			if(pr.getTipo().equals(this.pizza)){
				res+=pr.getTiempoCoccion();
			}
		}
		return res;
	}

	private double estimarTiempoDeCoccionPizzasActual(Pedido pedido,Horno h) {
		ListIterator<Producto> it = pedido.getProductos().listIterator();
		double res= 0;
		Producto pr;
		while(it.hasNext()){
			pr=it.next();
			if(pr.getTipo().equals(this.empanada)){
				res+=pr.getTiempoCoccion();
			}
		}
		return res;
	}

	private double estimarTiempoDePreparacionActual(Pedido pedido) {
		ListIterator<Producto> it = pedido.getProductos().listIterator();
		double res= 0;
		Producto pr;
		while(it.hasNext()){
			pr=it.next();
			res+=pr.getTiempoPreparacion();
		}
		return res;
	}

	/**
	 *
	 * @param Pedido
	 * @param Horno
	 */
	private double estimarTiempoDeCoccionEmpanadas(Pedido pedido, Horno horno){
		double res=0;
		if(pedido.getHorno() != horno){
			return res;
		}
		else if(pedido.getEstado()!= Estado.EnPreparacion && pedido.getEstado() != Estado.Ingresado && pedido.getEstado() != Estado.Preparado){
			return res;
		}
		else{
			return this.estimarTiempoDeCoccionEmpanadasActual(pedido,horno);
		}
	}


	/**
	 *
	 * @param Pedido
	 * @param Horno
	 */
	private double estimarTiempoDeCoccionPizzas(Pedido pedido,  Horno horno){
		double res=0;
		if(pedido.getHorno() != horno){
			return res;
		}
		else if(pedido.getEstado()!= Estado.EnPreparacion && pedido.getEstado() != Estado.Ingresado && pedido.getEstado() != Estado.Preparado){
			return res;
		}
		else{
			return this.estimarTiempoDeCoccionPizzasActual(pedido,horno);
		}
	}

	/**
	 *
	 * @param Pedido
	 * @param Horno
	 */
	private double estimarTiempoDePreparacion( Pedido pedido){
		double res=0;
		if(pedido.getEstado()!= Estado.Ingresado){
			return res;
		}
		else{
			return this.estimarTiempoDePreparacionActual(pedido);
		}
	}

}