
var divisible = false; //este comentario es una alternativa a resolver este problema de examen

for (var i = 1; i <= 100; i ++)
{
  function esDivisible(num, divisor)
  {
    if (num % divisor == 0)
    {
      return true;
    }
    else
    {
      return false;
    }
  }
  // divisible = false; //este comentario es una alternativa a resolver este problema de examen
  if (esDivisible(i, 3))
  {
    document.write("Fizz");
    // divisible = true; //este comentario es una alternativa a resolver este problema de examen
  }

  if (esDivisible(i, 5))
  {
    document.write("Buzz");
    // divisible = true; //este comentario es una alternativa a resolver este problema de examen
  }

  // if (!divisible) // este comentario es una alternativa a resolver este problema de examen
  if (!esDivisible(i, 3) && !esDivisible(i, 5))
  {
    document.write(i);
  }
  document.write("<br />");
}
