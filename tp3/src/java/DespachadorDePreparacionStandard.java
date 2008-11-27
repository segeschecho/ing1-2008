import java.util.LinkedList;
import java.util.List;
import java.util.ListIterator;
import java.util.Map;
import java.util.TreeMap;



/**
 * @author Federico
 * @version 1.0
 * @created 23-Nov-2008 12:30:53
 */
public class DespachadorDePreparacionStandard extends DespachadorDePreparacion {

	public Pedido pedidoPizzeroActual;
	public Pedido pedidoEmpanaderoActual;
	private List<Pedido> colaEmp;
	private List<Pedido> colaPiz;
	private Map<Pedido,Integer> partesAPreparar;
	private TipoProducto pizza;
	private TipoProducto empanada;



	public DespachadorDePreparacionStandard(Preparador prePizzero, Preparador prepEmPanadero,
            CoordinadorDeCocina coordinador,TipoProducto pizza, TipoProducto empanada){
		super(prePizzero,prepEmPanadero,coordinador);
		this.pizza=pizza;
		this.empanada=empanada;
		partesAPreparar=new TreeMap<Pedido, Integer>();
		colaEmp=new LinkedList<Pedido>();
		colaPiz=new LinkedList<Pedido>();

	}

	public void finalize() throws Throwable {
		super.finalize();
	}



	/**
	 *
	 * @param p
	 */
	private boolean asignableEmpanadero(Pedido p){
		boolean res=esEmpanadero(p) && !prepEmpanadero.getOcupado();
		if(res){
			if(esPizzero(p)){
				partesAPreparar.put(p, 2);
				if(!prepPizzero.getOcupado()){
					pedidoPizzeroActual=p;
					prepPizzero.preparar(getSubpedidoPizzero(p));
				}
				else{
					colaPiz.add(p);
				}

			}
			else{
				partesAPreparar.put(p, 1);
			}
			pedidoEmpanaderoActual=p;
			p.setEstado(Estado.EnPreparacion);
			prepEmpanadero.preparar(getSubpedidoEmpanadero(p));
		}
		return res;
	}

	/**
	 *
	 * @param p
	 */
	private boolean asignablePizzero(Pedido p){
		System.out.println(esPizzero(p));
		System.out.println(!prepPizzero.getOcupado());
		boolean res=esPizzero(p) && !prepPizzero.getOcupado();
		if(res){
			if(esEmpanadero(p)){
				partesAPreparar.put(p, 2);
				colaEmp.add(p);
			}
			else{
				partesAPreparar.put(p, 1);
			}
			pedidoPizzeroActual=p;
			prepPizzero.preparar(getSubpedidoPizzero(p));
			p.setEstado(Estado.EnPreparacion);
		}
		return res;
	}


	public void empanadasTerminadas(){
		Pedido p = this.pedidoEmpanaderoActual;
		Integer partes =partesAPreparar.get(p);
		partes=partes-1;
		partesAPreparar.put(p, partes);
		if(partes == 0){
			coordinador.cocinar(p);
			partesAPreparar.remove(p);
			pedidoPizzeroActual=null;
		}
		if(!colaEmp.isEmpty()){
			p=colaEmp.get(0);
			colaEmp.remove(0);
		}
		else{
			p=coordinador.conseguirPedido(empanada);
		}
		if(p!= null){
			prepEmpanadero.preparar(getSubpedidoPizzero(p));
		}


   }

	/**
	 *
	 * @param p
	 */
	private boolean esEmpanadero(Pedido p){
		ListIterator<Producto> it = p.getProductos().listIterator();
		Producto pr;
		while(it.hasNext()){
			pr=it.next();
			if(pr.getTipo().equals(empanada)){
				return true;
			}

		}
		return false;
	}

	/**
	 *
	 * @param p
	 */
	private boolean esPizzero(Pedido p){
		ListIterator<Producto> it = p.getProductos().listIterator();
		Producto pr;
		while(it.hasNext()){
			pr=it.next();
			if(pr.getTipo().equals(pizza)){
				return true;
			}

		}
		return false;
	}

	/**
	 *
	 * @param p
	 */
	private List<Producto> getSubpedidoEmpanadero(Pedido p){
		ListIterator<Producto> it = p.getProductos().listIterator();
		Producto pr;
		List<Producto> res = new LinkedList<Producto>();
		while(it.hasNext()){
			pr=it.next();
			if(pr.getTipo().equals(empanada)){
				res.add(pr);
			}
		}
		return res;
	}

	/**
	 *
	 * @param p
	 */
	private List<Producto> getSubpedidoPizzero(Pedido p){
		ListIterator<Producto> it = p.getProductos().listIterator();
		Producto pr;
		List<Producto> res = new LinkedList<Producto>();
		while(it.hasNext()){
			pr=it.next();
			if(pr.getTipo().equals(pizza)){
				res.add(pr);
			}
		}
		return res;
	}

	public void pizzasTerminadas(){
		Pedido p = this.pedidoPizzeroActual;
		Integer partes =partesAPreparar.get(p);
		partes=partes-1;
		partesAPreparar.put(p, partes);
		if(partes == 0){
			coordinador.cocinar(p);
			partesAPreparar.remove(p);
			pedidoPizzeroActual=null;
		}
		if(!colaPiz.isEmpty()){
			p=colaPiz.get(0);
			colaPiz.remove(0);
		}
		else{
			p=coordinador.conseguirPedido(pizza);
		}
		if(p!= null){
			prepPizzero.preparar(getSubpedidoPizzero(p));
		}


	}

	/**
	 *
	 * @param p
	 */
	public boolean prepararPedido(Pedido p){
		if(asignableEmpanadero(p)){
			return true;
		}
		else{
			return asignablePizzero(p);
		}
	}


}