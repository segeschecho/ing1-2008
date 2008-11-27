import java.util.Date;
import java.util.LinkedList;
import java.util.List;



/**
 * @author Federico
 * @version 1.0
 * @created 23-Nov-2008 12:29:05
 */
public class Pedido implements Comparable<Pedido> {
    static private List<Pedido> allInst=new LinkedList<Pedido>();
	protected Estado estadoP;
	protected String fechaIngreso;
	protected String formaDePago;
	protected Horno horno;
	protected int id;
	protected String razonCancelacion;
	protected Cliente cliente;
	protected List<Producto> productos;
	protected double tiempoEstimado;
	protected double precio;

	public Pedido(int id, Cliente cliente,List<Producto> productos,String formaDePago,String fechaIngreso){
          this.id=id;
          this.cliente=cliente;
          this.productos=productos;
          this.fechaIngreso=fechaIngreso;
          allInst.add(this);
	}

	public void finalize() throws Throwable {

	}

	public static List<Pedido> allInstances(){
		return allInst;
	}


    public static List<Pedido> getAllInst() {
		return allInst;
	}

	public static void setAllInst(List<Pedido> allInst) {
		Pedido.allInst = allInst;
	}

	public Estado getEstado() {
		return estadoP;
	}

	public void setEstado(Estado estadoP) {
		this.estadoP = estadoP;
	}

	public String getFechaIngreso() {
		return fechaIngreso;
	}

	public void setFechaIngreso(String fechaIngreso) {
		this.fechaIngreso = fechaIngreso;
	}

	public String getFormaDePago() {
		return formaDePago;
	}

	public void setFormaDePago(String formaDePago) {
		this.formaDePago = formaDePago;
	}

	public Horno getHorno() {
		return horno;
	}

	public void setHorno(Horno horno) {
		this.horno = horno;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getRazonCancelacion() {
		return razonCancelacion;
	}

	public void setRazonCancelacion(String razonCancelacion) {
		this.razonCancelacion = razonCancelacion;
	}

	public Cliente getCliente() {
		return cliente;
	}

	public void setCliente(Cliente cliente) {
		this.cliente = cliente;
	}

	public List<Producto> getProductos() {
		return productos;
	}

	public void setProductos(List<Producto> productos) {
		this.productos = productos;
	}

	public void setTiempoEstimado(double tiempoEstimado) {
		this.tiempoEstimado = tiempoEstimado;
	}
    public double getTiempoEstimado() {
		return tiempoEstimado;
	}

    public double getPrecio() {
		return precio;
	}
    public void setPrecio(double precio) {
		this.precio = precio;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + id;
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
		final Pedido other = (Pedido) obj;
		if (id != other.id)
			return false;
		return true;
	}

	public int compareTo(Pedido o) {
		// TODO Auto-generated method stub
		return this.id-o.id;
	}


}