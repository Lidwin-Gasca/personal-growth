

var vp = document.getElementById("villaplatzi");
var papel = vp.getContext("2d");

var vaca = { url: "vaca.png", cargaOK: false};

var fondo = { url: "tile.png", cargaOK: false};

var cerdo = { url: "cerdo.png", cargaOK: false};

var pollo = { url: "pollo.png", cargaOK: false};


fondo.objetoImagen = new Image();
fondo.objetoImagen.src = fondo.url;
fondo.objetoImagen.addEventListener("load", cargarFondo);

vaca.objetoImagen = new Image();
vaca.objetoImagen.src = vaca.url;
vaca.objetoImagen.addEventListener("load", cargarVacas);

cerdo.objetoImagen = new Image();
cerdo.objetoImagen.src = "cerdo.png";
cerdo.objetoImagen.addEventListener("load", cargarCerdos);

pollo.objetoImagen = new Image();
pollo.objetoImagen.src = "pollo.png";
pollo.objetoImagen.addEventListener("load", cargarPollos);

var cantidad = aleatorio(1, 50);
var cantidadDeCerdos = aleatorio(1, 20);

function cargarFondo()
{
  fondo.cargaOK = true;
  dibujarTodo();
}

function cargarVacas()
{
  vaca.cargaOK = true;
  dibujarTodo();
}

function cargarCerdos()
{
  cerdo.cargaOK = true;
  dibujarTodo();
}

function cargarPollos()
{
  pollo.cargaOK = true;
  dibujarTodo();
}

function dibujarTodo()
{
  if(fondo.cargaOK == true)
  {
    papel.drawImage(fondo.objetoImagen, 0, 0);
  }
  if(vaca.cargaOK)
  {
    var x = aleatorio(0, 420);
    var y = aleatorio(0, 420);
    papel.drawImage(vaca.objetoImagen, x, y);
  }
  if(cerdo.cargaOK)
  {
    console.log(cantidadDeCerdos);
    for (var c = 0; c < cantidadDeCerdos; c++)
    {
      var x = aleatorio(0, 7);
      var y = aleatorio(0, 8);
      var x = x * 60;
      var y = y * 40;
      papel.drawImage(cerdo.objetoImagen, x, y);
    }
  }
  if(pollo.cargaOK)
  {
    console.log(cantidad);
    for (var v = 0; v < cantidad; v++)
    {
      var x = aleatorio(0, 420);
      var y = aleatorio(0, 420);
      papel.drawImage(pollo.objetoImagen, x, y);
    }
  }
}



function aleatorio(min, maxi)
{
  var resultado;
  resultado = Math.floor(Math.random() * (maxi - min + 1)) + min;
  return resultado;
}
