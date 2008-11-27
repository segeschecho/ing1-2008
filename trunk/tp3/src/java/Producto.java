import java.util.LinkedList;
import java.util.List;



/**
 * @author Federico
 * @version 1.0
 * @created 23-Nov-2008 13:10:01
 */
public class Producto {

	private static List<Producto> allInst = new LinkedList<Producto>();
	private String nombre;
	private float precio;
	private double tiempoCoccion;
	private double tiempoPreparacion;
	private TipoProducto tipoProducto;
	private List<Insumo> insumos;


	public Producto(String nombre,float precio, double tiempoCoccion,
			double tiempoPreparacion,TipoProducto tipoProducto,List<Insumo> insumos){
		this.nombre =nombre;
		this.insumos=insumos;
		this.precio=precio;
		this.tiempoCoccion=tiempoCoccion;
		this.tiempoPreparacion=tiempoPreparacion;
		this.tipoProducto=tipoProducto;
		allInst.add(this);

	}

	public void finalize() throws Throwable {

	}
    public static List<Producto> allInstances(){
    	return allInst;
    }
	public String getNombre() {
		return nombre;
	}

	public List<Insumo> getInsumos(){
		return this.insumos;
	}

	public float getPrecio(){
		return this.precio;
	}

	public boolean getPreparable(){
		return this.tipoProducto.getPreparable();
	}

	public double getTiempoCoccion(){
		return this.tiempoCoccion;
	}

	public double getTiempoPreparacion(){
		return this.tiempoPreparacion;
	}

	public TipoProducto getTipo(){
		return this.tipoProducto;
	}

	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return nombre;
	}

}