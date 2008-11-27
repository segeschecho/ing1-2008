


public class TipoProducto implements Comparable<TipoProducto> {

	private boolean cocinable;
	private String nombre;
	private boolean preparable;

	public TipoProducto(String nombre, boolean coc, boolean prep){
           this.nombre=nombre;
           this.cocinable=coc;
           this.preparable=prep;
	}


	public String getNombre() {
		return nombre;
	}

	public boolean getCocinable(){
		return this.cocinable;
	}
	public boolean getPreparable(){
		return this.preparable;

	}


	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((nombre == null) ? 0 : nombre.hashCode());
		return result;
	}


	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		final TipoProducto other = (TipoProducto) obj;
		if (nombre == null) {
			if (other.nombre != null)
				return false;
		} else if (!nombre.equals(other.nombre))
			return false;
		return true;
	}

//a negative integer, zero, or a positive integer as this object is less than, equal to, or greater than the specified object.*/
	public int compareTo(TipoProducto o) {
		return this.nombre.compareTo(o.nombre);
	}

}