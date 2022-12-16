class Pakiman
 {
   constructor(n, v, a) //el constructor es una funcion que crea una instancia de una clase llamada comunmente objeto.

   //Un constructor es llamado al momento que declaras un objeto usando la palabra "new", el proposito de una construccion
   //es crear un objeto y establecer sus propiedades (si es que los tiene).

   //si no declarro los parametros arriba con el constructor, tendre un error abajo cuando le doy propiedades a los
   //parametros que serian inexistentes.
   {
     this.nombre = n; //esta "n" es la misma que la "n" del constructor, es el primer parametro.

     this.tipo = "tierra"; // este es solo una propiedad generica, que aplicara a todos los objetos
     //Pakimans (los objetos de esta clase pertenece a la clase Pakiman), por ende no es necesario
     //declararle un parametro en el constructor.

     this.vida = v; // la "v" es el segundo parametro del constructor.
     this.ataque = a; // "a" es el tercer parametro del constructor.
   }
   hablar()
   {
     alert(this.nombre);
   }
 }

 var cauchin = new Pakiman("cauchin", 100, 30);
 var pocacho = new Pakiman("pocacho", 80, 50);
 var tocinauro = new Pakiman("tocinauro", 120, 40);
 //estas ultimas tres filas, contienen la palabra clave "new", la cual se usa para Iniciar una
 //Referencia al Objeto nuevo, el cual a su misma vez se convierte en una instancia (expresion
 //de una deteminada clase, enntidad o prototipo).

console.log(tocinauro);
console.log(cauchin);
console.log(pocacho);// para no escribir console.log varias veces solo separa los parametros con un coma,
//por ejemplo console.log(cauchin, pokacho, tocinauro);
