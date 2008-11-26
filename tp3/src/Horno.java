

/**
 * @author Gonzalo
 * @version 1.0
 * @created 16-Nov-2008 22:40:46
 */
public class Horno {

	private int cantModulos;
	private FraccionadorDeHorno fraccionadorDeHorno;

	public FraccionadorDeHorno getFraccionadorDeHorno() {
		return fraccionadorDeHorno;
	}

	public Horno(int cantModulos,FraccionadorDeHorno fraccionadorDeHorno){
		this.cantModulos=cantModulos;
		this.fraccionadorDeHorno=fraccionadorDeHorno;


	}

	public void finalize() throws Throwable {

	}

	public int getCantModulos(){
		return cantModulos;
	}

}