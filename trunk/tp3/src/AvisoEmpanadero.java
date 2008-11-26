

/**
 * @author Administrador
 * @version 1.0
 * @created 16-Nov-2008 22:40:34
 */
public class AvisoEmpanadero extends Aviso {

	public AvisoEmpanadero(DespachadorDePreparacionStandard dest){
		super(dest);
	}

	public void finalize() throws Throwable {
		super.finalize();
	}

	public void avisar(){
         super.destinatario.empanadasTerminadas();
	}

}