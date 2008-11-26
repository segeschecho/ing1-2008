import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

import com.sun.org.apache.bcel.internal.generic.UnconditionalBranch;


public class Inicializador {

	/**
	 * @param args
	 * @throws ExcepcionProductoInsat
	 * @throws ClienteNuloTelefono
	 * @throws ExcepcionOrigenDesconocido
	 * @throws PedidoNulo
	 * @throws ProductosVacios
	 */
	public static void main(String[] args) throws ProductosVacios, PedidoNulo, ExcepcionOrigenDesconocido, ClienteNuloTelefono, ExcepcionProductoInsat {
		TipoProducto pizza= new TipoProducto("pizza",true,true);
		TipoProducto empanada= new TipoProducto("empanada",true,true);
		TipoProducto coca= new TipoProducto("coca",false,false);
		TipoProducto birra= new TipoProducto("cerveza",false,false);
		Insumo bollo = new Insumo(10,3,"bollo");
		Insumo muzza = new Insumo(13,2,"muzza");
		Insumo tapa = new Insumo(15,3,"tapa");
		Insumo carne = new Insumo(34,5,"carne");
		Insumo quilmes = new Insumo(23,3,"quilmes");
		Insumo pepsi = new Insumo(123,23,"pepsi");
		List<Insumo> insumosMuzza = new LinkedList<Insumo>();
		insumosMuzza.add(bollo);
		insumosMuzza.add(muzza);
		Producto pizzMuzza = new Producto("pizzaMuzza",10,13.3,2.3,pizza,insumosMuzza);
		System.out.println(Producto.allInstances().toString());

		//ahora vamos a armar un fraccionador
		Map<TipoProducto,Integer> t = new TreeMap<TipoProducto,Integer>();
		t.put(pizza, 1);
		t.put(empanada, 4);
		FraccionadorDeHorno frPizzero = new FraccionadorDeHorno(t);
		FraccionadorDeHorno frEmpanadero = new FraccionadorDeHorno(t);
		//armamos 2 hornos
		Horno hpizzero = new Horno(10,frPizzero);
		Horno hempanadero = new Horno(10,frEmpanadero);
		// armamos los avisos
		AvisoEmpanadero avE = new AvisoEmpanadero(null);
		AvisoPizzero avP = new AvisoPizzero(null);
		//ahora los preparadores
		PreparadorEspecializado prepPizzero= new PreparadorEspecializado(avP);
		PreparadorEspecializado prepEmpanadero= new PreparadorEspecializado(avE);
		//coordinadorDeCocina
		DespachadorDePreparacion dep=null;
		CoordinadorDeCocina coordC = new CoordinadorDeCocina(null,null,null);
		//Despachador
		dep = new DespachadorDePreparacionStandard(prepPizzero,prepEmpanadero,coordC,pizza,empanada);
		coordC.setDespachadorDePreparacion(dep);
		//controladorDeIngreso
        ControladorDeIngreso contIng = new ControladorDeIngresoStandard(coordC);
        coordC.setControladorDeIngreso(contIng);
        //controladorDelistos
        ControladorDeListos contList = new ControladorDeListos();
        //CoordinadorDePedidos
        CoordinadorDePedidos coordP = new CoordinadorDePedidos(null,null,contList);
        coordC.setCoordinadorDePedidos(coordP);
        //controladorDePreIngreso
        ControladorDePreIngreso contPreIng = new ControladorDePreIngreso(coordP,contIng);
        coordP.setControladorDePreIngreso(contPreIng);
        //CalculadorDePrecios
        CalculadorDePrecios calcP = new CalculadorDePreciosStandard();
        //AsignadorDeHorno
        AsignadorDeHorno asigH = new AsignadorDeHornoStandard(hpizzero,hempanadero,pizza,empanada);
        //EstimadorDeTiempos
        EstimadorDeTiempos estT = new EstimadorStandard(pizza,empanada);
        //ControladorDeStock
        ControladorDeStock contS = new ControladorDeStockStandard();
        //GenedarodDePedidos
        GeneradorDePedidos genP = new GeneradorDePedidosStandard(calcP,estT,contS,asigH);
        coordP.setGeneradorDePedidos(genP);
        List<Producto> lp= new LinkedList<Producto>();
        lp.add(pizzMuzza);
        lp.add(pizzMuzza);
        coordP.ingresarPedido(null, lp, "contado", "mostrador", 0);
        coordP.ingresarPedido(null, lp, "contado", "mostrador", 0);
        coordP.ingresarPedido(null, lp, "contado", "mostrador", 0);


	}

}
