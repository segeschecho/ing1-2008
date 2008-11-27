

/**
 * @author Administrador
 * @version 1.0
 * @created 16-Nov-2008 22:40:35
 */
public class AvisoPizzero extends Aviso {

	public AvisoPizzero(DespachadorDePreparacionStandard dest){
          super(dest);
	}

	public void finalize() throws Throwable {
		super.finalize();
	}

	public void avisar(){
		super.destinatario.pizzasTerminadas();
	}

}