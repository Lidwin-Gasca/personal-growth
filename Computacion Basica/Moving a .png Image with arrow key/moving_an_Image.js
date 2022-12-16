
var teclas = {UP: 38, DOWN: 40, LEFT: 37, RIGHT: 39};
document.addEventListener("keydown", moverVacaConTeclado);

console.log(teclas);
var cuadrito = document.getElementById("area_de_dibujo");
var papel = cuadrito.getContext("2d");
var vaca = { url: "vaca.png", cargaOK: false};
var fondo = { url: "tile.png", cargaOK: false};
var x;
var y;

fondo.objetoImagen = new Image();
fondo.objetoImagen.src = fondo.url;
fondo.objetoImagen.addEventListener("load", cargarFondo);

vaca.objetoImagen = new Image();
vaca.objetoImagen.src = vaca.url;
vaca.objetoImagen.addEventListener("load", cargarVacas);

function cargarFondo()
{
  fondo.cargaOK = true;
  dibujarVaca();
}

function cargarVacas()
{
  vaca.cargaOK = true;
  dibujarVaca();
}

function dibujarVaca()
{
  if(fondo.cargaOK == true)
  {
    papel.drawImage(fondo.objetoImagen, 0, 0);
  }
  if(vaca.cargaOK)
  {
    var xv = aleatorio(0, 420);
    var yv = aleatorio(0, 420);
    papel.drawImage(vaca.objetoImagen, xv, yv);
    x = xv;
    y = yv;
  }
}

function aleatorio(min, maxi)
{
  var resultado;
  resultado = Math.floor(Math.random() * (maxi - min + 1)) + min;
  return resultado;
}


function moverVacaConTeclado(evento)
{

  var imagen = vaca.objetoImagen;
  var movimiento = 10;

  switch(evento.keyCode)
  {
    case teclas.UP:
      papel.drawImage(fondo.objetoImagen, 0, 0);
      papel.drawImage(vaca.objetoImagen, x, y - movimiento);
      y = y - movimiento;
      break;
    case teclas.DOWN:
      papel.drawImage(fondo.objetoImagen, 0, 0);
      papel.drawImage(vaca.objetoImagen, x, y + movimiento);
      y = y + movimiento
      break;
    case teclas.LEFT:
      papel.drawImage(fondo.objetoImagen, 0, 0);
      papel.drawImage(vaca.objetoImagen, x - movimiento, y);
      x = x - movimiento;
      break;
    case teclas.RIGHT:
      papel.drawImage(fondo.objetoImagen, 0, 0);
      papel.drawImage(vaca.objetoImagen, x + movimiento, y);
      x = x + movimiento;
      break;
    default:
      console.log("has presionado una tecla random")
    break;
  }
}
