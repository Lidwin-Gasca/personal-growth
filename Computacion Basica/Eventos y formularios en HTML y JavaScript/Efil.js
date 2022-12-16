var texto = document.getElementById("caja_de_texto");
var boton = document.getElementById("boton_html");
var d = document.getElementById("Efil");
var linea = d.getContext("2d");
var ancho = d.width;

boton.addEventListener("click", dibujo_por_click);

function crearEfil(color, x_inicial, y_inicial, x_final, y_final)
{
  linea.beginPath();
  linea.strokeStyle = color;
  linea.moveTo(x_inicial, y_inicial);
  linea.lineTo(x_final, y_final);
  linea.stroke();
  linea.closePath();
}

function dibujo_por_click()
{
  var x = parseInt(texto.value);
  var lineas = x;
  var espacio = ancho / lineas;
  var l = 0;
  var yi, xf, inverso_xi, inverso_yi;
  var coloreado = "#faa"
  console.log(texto);
  console.log("el numero escrito es " + x);

  for(l = 0; l < lineas; l++)
  {
    yi = espacio * l;
    xi = espacio * l;
    xf = espacio * (l + 1);
    inverso_yi = 300 - yi;
    inverso_xi = 300 - xi;
    crearEfil(coloreado, 0, yi, xf, 300);
    //crearEfil(coloreado, 0, inverso_yi, xi, 0);
    //crearEfil(coloreado, xi, 300, 300, inverso_yi);
    //crearEfil(coloreado, inverso_xi, 0, 300, inverso_yi);
    console.log("Lineas Trazadas " + l);
  }
}
