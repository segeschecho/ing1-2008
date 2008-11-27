import java.util.LinkedList;
import java.util.List;



/**
 * @author Federico
 * @version 1.0
 * @created 16-Nov-2008 22:40:46
 */
public class Insumo {

	private static List<Insumo> allInst = new LinkedList<Insumo>();
	private int cant;
	private int cantCritica;
	private String nombre;

	public Insumo(int cant,int cantCritica,String nombre){
		this.cant=cant;
		this.cantCritica=cantCritica;
		this.nombre=nombre;
		allInst.add(this);

	}

	public void finalize() throws Throwable {

	}


	public int getCant() {
		return cant;
	}

	public int getCantCritica() {
		return cantCritica;
	}


	/**
	 *
	 * @param cant
	 */
	public void setCant(int cant){
        this.cant = cant;
	}

	public static List<Insumo> allInstances() {
		return allInst;
	}


	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public void setCantCritica(int cantCritica) {
		this.cantCritica = cantCritica;
	}

}