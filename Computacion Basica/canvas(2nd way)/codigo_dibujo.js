var d = document.getElementById("dibujito");
var lienzo = d.getContext("2d");

lienzo.beginPath();
lienzo.strokeStyle = "blue";
lienzo.moveTo(10,150);
lienzo.lineTo(20,300);
lienzo.stroke();
lienzo.closePath();

//Esto es un comentario.
//En el siguiente bloque de codigo se empleara una funtion,la cual haremos para no tener que hacer un bloque de codigo para que trazado de un canvas que queramos hacer, con esta funcion, solo tendriamos que unsar un solo bloque de codigo.

function dibujarLinea(color, x_inicial, y_inicial, x_final, y_final)
{
  lienzo.beginPath();
  lienzo.strokeStyle = color;
  lienzo.moveTo(x_inicial, y_inicial);
  lienzo.lineTo(x_final, y_final);
  lienzo.stroke();
  lienzo.closePath();
}

dibujarLinea("pink", 15, 15, 280, 280);
dibujarLinea("orange", 190, 10, 10, 190);
