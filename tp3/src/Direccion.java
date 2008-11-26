

/**
 * @author Gonzalo
 * @version 1.0
 * @created 23-Nov-2008 13:06:09
 */
public class Direccion {

	private String Calle;
	private String Departamento;
	private String Localidad;
	private int Numero;



	public Direccion(String calle, String departamento, String localidad,
			int numero) {
		super();
		Calle = calle;
		Departamento = departamento;
		Localidad = localidad;
		Numero = numero;
	}

	public void finalize() throws Throwable {

	}

	public String getCalle() {
		return Calle;
	}

	public void setCalle(String calle) {
		Calle = calle;
	}

	public String getDepartamento() {
		return Departamento;
	}

	public void setDepartamento(String departamento) {
		Departamento = departamento;
	}

	public String getLocalidad() {
		return Localidad;
	}

	public void setLocalidad(String localidad) {
		Localidad = localidad;
	}

	public int getNumero() {
		return Numero;
	}

	public void setNumero(int numero) {
		Numero = numero;
	}


}