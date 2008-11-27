import java.util.LinkedList;
import java.util.List;


public class PreparadorEspecializado extends Preparador {
    List<Producto> productosAPreparar;

    public PreparadorEspecializado(Aviso aviso) {
    	super(aviso);
		productosAPreparar = new LinkedList<Producto>();
	}

	@Override
	public boolean getOcupado() {
		// TODO Auto-generated method stub
		return this.ocupado;
	}

	@Override
	public void preparar(List<Producto> productos) {
		ocupado=true;
		productosAPreparar=productos;
		System.out.println("notificar que hay que preparar");
		//TODO: la parte del notify

	}

	@Override
	public void terminar() {
		ocupado=false;
		productosAPreparar = new LinkedList<Producto>();
		this.aviso.avisar();



	}

}
