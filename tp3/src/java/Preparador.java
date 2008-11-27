import java.util.List;

//Antes era una interfaz pero no queremos atributos final tonces la hacemos clase abstracta
//en este caso no nos trae problemas

/**
 * @author Federico
 * @version 1.0
 * @created 23-Nov-2008 12:36:55
 */
public abstract class  Preparador {

	public boolean ocupado;
	public Aviso aviso;


    public Preparador(Aviso aviso){
    	this.aviso=aviso;
    	this.ocupado=false;
    }
	public abstract boolean getOcupado();

	/**
	 *
	 * @param productos
	 */
	public abstract void preparar(List<Producto> productos);

	public abstract void terminar();

}