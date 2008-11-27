import java.util.LinkedList;
import java.util.List;
import java.util.ListIterator;

class ExcepcionProductoInsat extends Exception{
	Producto insat;
	public ExcepcionProductoInsat(Producto pr){
		insat=pr;
	}
	public Producto getInsat() {
		return insat;
	}
}

/**
 * @author Federico
 * @version 1.0
 * @created 23-Nov-2008 13:13:19
 */
public class ControladorDeStockStandard implements ControladorDeStock {
    List<Insumo> criticos;
	public ControladorDeStockStandard(){
            this.criticos = new LinkedList<Insumo>();
	}
    public List<Insumo> getCriticos() {
		return criticos;
	}

	public boolean ingresar(Producto producto) {
		ListIterator<Insumo> it = producto.getInsumos().listIterator();
		List<Insumo> yaDeCrementados = new LinkedList<Insumo>();
		Insumo in;
		int cant;
		while(it.hasNext()){
			in=it.next();
			cant=in.getCant();
			if(cant > 0){
				in.setCant(cant-1);
				yaDeCrementados.add(in);
			}
			else{
				reestablecerStockInsumos(yaDeCrementados);
                return false;
			}
		}
		return true;
	}
    /* notifica que insumos que estaban en algun producto de los que se ingresaron esta
     * ahora en stock critico(non-Javadoc)
     * @see ControladorDeStock#obtenerCriticos(java.util.List)
     */
	public void obtenerCriticos(List<Producto> productos) {
		this.criticos=new LinkedList<Insumo>();
		ListIterator<Producto> it = productos.listIterator();
		Producto pr;
		while(it.hasNext()){
			pr=it.next();
			ListIterator<Insumo> it2 = pr.getInsumos().listIterator();
			Insumo in;
			while(it2.hasNext()){
				in=it2.next();
				if(in.getCant() <= in.getCantCritica()){
					criticos.add(in);
				}
			}
		}


	}

	public void reestablecerStock(List<Producto> productos) {
		ListIterator<Producto> it = productos.listIterator();
		Producto pr;
		while(it.hasNext()){
			pr=it.next();
			reestablecerStockInsumos(pr.getInsumos());
		}

	}

	public void reestablecerStockInsumos(List<Insumo> insumos) {
		ListIterator<Insumo> it = insumos.listIterator();
		Insumo in;
		while(it.hasNext()){
			in=it.next();
			in.setCant(in.getCant()+1);
		}
	}

	public boolean verificarEIngresar(List<Producto> productos) throws ExcepcionProductoInsat {
		ListIterator<Producto> it = productos.listIterator();
		Producto pr;
		boolean posible;
		List<Producto> yaDecrementados = new LinkedList<Producto>();
		while(it.hasNext()){
			pr=it.next();
			posible=this.ingresar(pr);
			if(!posible){
				reestablecerStock(yaDecrementados);
				throw new ExcepcionProductoInsat(pr);
			}
			else{
				yaDecrementados.add(pr);
			}
			obtenerCriticos(productos);
			if(!this.criticos.isEmpty()){
				System.out.println("notificar productos con stock critico");
				//TODO:hacer la parte de los notify
			}
		}
		return true;

	}


}