var d = document.getElementById("dibujito");
var lienzo = d.getContext("2d");
var lineas = 30;
var l = 0;
var yi, xf, inverso_xi, inverso_yi;
var colorcito = "#faa";

dibujarLinea(colorcito, 1, 1, 1, 299);
dibujarLinea(colorcito, 1, 299, 299, 299);
dibujarLinea(colorcito, 1, 1, 299, 1);
dibujarLinea(colorcito, 299, 1, 299, 299);

for(l = 0; l < lineas; l++)
{
  yi = 10 * l;
  xi = 10 * l;
  xf = 10 * (l + 1);
  inverso_yi = 300 - yi;
  inverso_xi = 300 - xi;
  dibujarLinea(colorcito, 0, yi, xf, 300);
  dibujarLinea(colorcito, 0, inverso_yi, xi, 0);
  dibujarLinea(colorcito, xi, 300, 300, inverso_yi);
  dibujarLinea(colorcito, inverso_xi, 0, 300, inverso_yi);
  console.log("Linea " + l);
}
//var tareaPropia = document.getElementById("autoTarea");
//var mis_rayas = tareaPropia.getContext("2d");
//var rayas_500 = 20;
//var rayas_300 = 30;
//var r = 0;
//var r2 = 0;
//var color_de_rayas = "#03a14a";


//for(r = 0; r2 = 0; r++, r2++)
//{
//  for(r < 30; r2 < 50)
//  {
//    ceYi = 10 * r;
//    ceXi = 10 * r2;
//    ceYi_i = 300 - ceYi;
//    ceX_i = 500 - ceXi;
//    mi_autoTarea(color_de_rayas,0,ceYi_i, ceXi,0);
//    console.log("las lineas de mi auto Tarea " + r + "aun mas lineas " + r2);
//  }
//}



function dibujarLinea(color, x_inicial, y_inicial, x_final, y_final)
{
  lienzo.beginPath();
  lienzo.strokeStyle = color;
  lienzo.moveTo(x_inicial, y_inicial);
  lienzo.lineTo(x_final, y_final);
  lienzo.stroke();
  lienzo.closePath();
}
