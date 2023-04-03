document.addEventListener("mousedown", mouseDown);
document.addEventListener("mouseup", mouseUp);
document.addEventListener("mousemove", mouseMove);
let aDD = document.getElementById("areaDeDibujo");
let papel = aDD.getContext("2d");
let click;
let x;
let y;
function mouseDown(evento){
  click = true;

  console.log("esto si funciona");
}
function mouseUp(){
  click = false;

  console.log("esto megafunciona");
}
function mouseMove(evento){
  console.log("el ratton se mueve stisfactoriamente" + evento.layerX + "," + evento.layerY);
  if (click == true){
    dibujarLinea("orange", x, y, evento.layerX, evento.layerY, papel)
  }
  x = evento.layerX;
  y = evento.layerY;
}
function dibujarLinea(color, x_inicial, y_inicial, x_final, y_final, lienzo)
{
  lienzo.beginPath();
  lienzo.strokeStyle = color;
  lienzo.lineWidth = 10;
  lienzo.moveTo(x_inicial, y_inicial);
  lienzo.lineTo(x_final, y_final);
  lienzo.stroke();
  lienzo.closePath();
}

dibujarLinea("black", 1, 1, 300, 1, papel);
dibujarLinea("black", 1, 299, 299, 299, papel);
dibujarLinea("black", 1, 1, 1, 299, papel);
dibujarLinea("black", 299, 1, 299, 299, papel);
