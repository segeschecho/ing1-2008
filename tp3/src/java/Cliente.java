import java.util.LinkedList;
import java.util.List;



/**
 * @author Federico
 * @version 1.0
 * @created 23-Nov-2008 13:05:59
 */
public class Cliente {

	static List<Cliente> allInst = new LinkedList<Cliente>();
	private Direccion dir;
	private String apellido;
	private String celular;
	private String id;
	private String nombre;
	private String passWeb;
	private String telefono;
	private String usrweb;
	public Cliente(String apel,String celular,String id, String nombre,
			String passWeb,String telefono,String web,Direccion dir){
        this.apellido=apel;
        this.celular=celular;
        this.id=id;
        this.nombre=nombre;
        this.passWeb=passWeb;
        this.telefono=telefono;
        this.usrweb=web;
        this.dir=dir;
        allInst.add(this);
	}

	public static List<Cliente> getAllInst() {
		return allInst;
	}

	public String getApellido() {
		return apellido;
	}

	public String getNombre() {
		return nombre;
	}

	public String getId() {
		return id;
	}

	public String getPassWeb() {
		return passWeb;
	}

	public String getCelular() {
		return celular;
	}

	public Direccion getDir() {
		return dir;
	}

	public String getTelefono() {
		return telefono;
	}

	public String getUsrweb() {
		return usrweb;
	}






}