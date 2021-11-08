var imagenes = [];
imagenes["cauchin"] = "vaca.png";
imagenes["pokacho"] = "pollo.png";
imagenes["tocinauro"] = "cerdo.png";

var cauchin = new Pakiman("cauchin", 100, 30);
var pokacho = new Pakiman("pokacho", 80, 50);
var tocinauro = new Pakiman("tocinauro", 120, 40);


cauchin.mostrar();
pokacho.mostrar();
tocinauro.mostrar();


// var coleccion = [];
// coleccion.push(cauchin);
// coleccion.push(pokacho);
// coleccion.push(tocinauro);
//
// for (var pakimanes in coleccion)
// {
//   console.log(coleccion[pakimanes]);
//   pakimanes.mostrar();
// }
