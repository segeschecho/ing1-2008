import java.util.ListIterator;




public class AsignadorDeHornoStandard extends AsignadorDeHorno {

	public AsignadorDeHornoStandard(Horno p, Horno e,TipoProducto Pizza, TipoProducto Empanada){
        super(p,e,Pizza,Empanada);
	}

	public void finalize() throws Throwable {
		super.finalize();
	}

	/**
	 *
	 * @param Pedido
	 */
	public void asignarHorno(Pedido pedido){
        boolean pizzas=false;
        boolean empanadas=false;
        ListIterator<Producto> it = pedido.getProductos().listIterator();
        Producto pr;
        Horno h = null;
        while(it.hasNext()){
        	pr=it.next();
        	pizzas = pizzas || pr.getTipo().equals(this.pizza);
        	empanadas = empanadas || pr.getTipo().equals(this.empanada);
        }
        if(pizzas && empanadas){
        	h=notificarHorno();
        }
        else if(pizzas){
        	h=this.hornoP;
        }
        else if(empanadas){
        	h=this.hornoE;
        }
        pedido.setHorno(h);
	}

	private Horno notificarHorno(){
		return null;
	}

}