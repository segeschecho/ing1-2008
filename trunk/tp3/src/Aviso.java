

/**
 * @author Federico
 * @version 1.0
 * @created 16-Nov-2008 22:40:34
 */
public abstract class Aviso {

	protected DespachadorDePreparacionStandard destinatario;

	public Aviso(DespachadorDePreparacionStandard dest){
         this.destinatario = dest;
	}

	public void finalize() throws Throwable {

	}

	public abstract void avisar();

	public DespachadorDePreparacionStandard getDestinatario() {
		return destinatario;
	}

	public void setDestinatario(DespachadorDePreparacionStandard destinatario) {
		this.destinatario = destinatario;
	}


}