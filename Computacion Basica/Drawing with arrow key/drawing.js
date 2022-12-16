
var teclas = {UP: 38, DOWN: 40, LEFT: 37, RIGHT: 39};
document.addEventListener("keydown", dibujarTeclado);
document.addEventListener("mousedown", deteccionDeMouse);
//pensaba usar esto pero ya no lo hice //--> window.onload = function(){}
function deteccionDeMouse(eventoMouse)
{
  console.log(eventoMouse);
}
console.log(teclas);
var cuadrito = document.getElementById("area_de_dibujo");
var papel = cuadrito.getContext("2d");
var x = 150;
var y = 150;

dibujarLinea("red", 149, 149, 151, 151, papel);

function dibujarLinea(color, x_inicial, y_inicial, x_final, y_final, lienzo)
{
  lienzo.beginPath();
  lienzo.strokeStyle = color;
  lienzo.lineWidth = 3;
  lienzo.moveTo(x_inicial, y_inicial);
  lienzo.lineTo(x_final, y_final);
  lienzo.stroke();
  lienzo.closePath();
}
function dibujarTeclado(evento)
{
  var colorcito = "orange";
  var movimiento = 1;
  // if(evento.keyCode == teclas.UP)
  // {
  //   console.log("vamos pa' arriba");
  // }
  // if(evento.keyCode == teclas.DOWN)
  // {
  //   console.log("vamos pa' abajo");
  // }
  // if(evento.keyCode == teclas.LEFT)
  // {
  //   console.log("vamos para la izquierda");
  // }
  // if(evento.keyCode == teclas.RIGHT)
  // {
  //   console.log("vamos para la derecha");
  // }

  switch(evento.keyCode)
  {
    case teclas.UP:
      dibujarLinea(colorcito, x, y, x, y - movimiento, papel);
      y = y - movimiento;
      break;
    case teclas.DOWN:
      dibujarLinea(colorcito, x, y, x, y + movimiento, papel);
      y = y + movimiento
      break;
    case teclas.LEFT:
      dibujarLinea(colorcito, x, y, x - movimiento, y, papel);
      x = x - movimiento;
      break;
    case teclas.RIGHT:
    dibujarLinea(colorcito, x, y, x + movimiento, y, papel);
    x = x + movimiento;
      break;

    default:

              // ya que esto es un switch para reemplazar los "if" y "else", la
              //palabra "case" abre el caso (case viene significando "if").
      console.log("has presionado una tecla random")
              //mientras que la palabra "break" los cierra, la palabra "default"
              //vendria significando "else", y se vuelve a usar "break" para
              //cerrar "default" tambien.
    break;
  }


}
