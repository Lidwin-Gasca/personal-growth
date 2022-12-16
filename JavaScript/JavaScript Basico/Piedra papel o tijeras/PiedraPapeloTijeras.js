class estadoDeMano
{
  constructor (p)
  {
    this.imagen = new Image();
    this.pocision = p;
    this.imagen.src = imagenes[this.pocision];
  }
  mostrar()
  {
    document.body.appendChild(this.imagen);
  }
}
//document.addEventListener("mouseclick", mouseClick);
var imagenes = [];
imagenes["Piedra"] = "rock.png";
imagenes["Papel"] = "paper.png";
imagenes["Tijeras"] = "scissors.png";
var rock = new estadoDeMano("Piedra");
var paper = new estadoDeMano("Papel");
var scissors = new estadoDeMano("Tijeras");
var seleccionCPU = aleatorio(1,3);
var seleccionHumano;
//var seleccionHumano = parseInt(prompt("Elige tu planeta, \nnumero 1 para Piedra \nnumero 2 para Papel \nnumero 3 para Tijeras"));


function aleatorio(min,max)
{
  var resultado;
  resultado = Math.floor(Math.random() * (max - min + 1)) + min;
  return resultado;
}

function pelea(){
if (seleccionHumano == seleccionCPU)
{
  document.write("<h1>empate</h1><br />")
}
else if (seleccionHumano == 1 && seleccionCPU == 3)
{
  document.write("<h1>ganaste piedra contra tijeras</h1><br />");
}
else if (seleccionHumano == 2 && seleccionCPU == 1)
{
  document.write("<h1>ganaste papel contra piedra</h1><br />");
}
else if (seleccionHumano == 3 && seleccionCPU == 2)
{
  document.write("<h1>ganaste tijeras contra papel</h1><br />");
}
else if (seleccionHumano == 3 && seleccionCPU == 1)
{
  document.write("<h1>perdiste tijeras contra piedra</h1><br />");
}
else if (seleccionHumano == 1 && seleccionCPU == 2)
{
  document.write("<h1>perdiste piedra contra papel</h1><br />");
}
else if (seleccionHumano == 2 && seleccionCPU == 3)
{
  document.write("<h1>perdiste papel contra tijeras</h1><br />");
}
console.log(seleccionHumano, seleccionCPU);
}


rock.mostrar();
paper.mostrar();
scissors.mostrar();
