
for(var i=0; i<10; i++)
{
  var z = aleatorio(10,20);
  document.write(z + ", ");
}

document.write(z);

function aleatorio(min, maxi)
{
  var resultado;
  resultado = Math.floor(Math.random() * (maxi - min + 1)) + min;
  return resultado;
}