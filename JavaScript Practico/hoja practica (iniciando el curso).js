//Que es una variable y para que sirve???
////////////una variable es un espacio guardado en memoria

//cual es la diferencia entre declarar e inicializar una variable?
//////////declarar es: var edad    (es cuando adviertes que existe variables y cuales son).
/////////inicializar es: var edad = x_valor    (es cuando no solo declaras si no ademas das un valor a la variable).

//cual es la diferencia ente sumar numeros y concatenar strings?
//// cuando sumas numeros haces una operacion, pero cuando concatenas strings, estas llamando el valor de alguna variable a una oracion visible por el usuario.

//cual operador te permite sumar o concatenar?
///////el oprador es: +      ///////el concatenador es ${dejaAquiTuVariable}

//Traduce a codigo de JavaScript las siguientes variables:
//   Nombre,  Apellido, Nombre de usuario en Platzi, Edad, Correo electronico, Mayor de edad, Dinero ahorrado, Deudas
//Despues calcula e imprime las siguientes variables a partir de las variables anteriores:
//   Nombre completo (nombre y apellido)
//   Dinero real (dinero ahorrado menos deudas)

var nombre = "Lidwin";
var apellido = "Gasca";
var nombreDeUsuarioEnPlatzi = "Lidwin_n"
var correoElectronico = "memitogasca@gmail.com";
var mayorDeEdad = true;
var dineroAhorrado = 300;
var deudas = 3000;

var variablesYoperaciones = function varYope(){
  document.write("Nombre completo del usuario: <br />" + nombre + " " + apellido + "<br /><br />");
}

var dineroReal = function dineroR(){
  var respuestaDineroReal = dineroAhorrado - deudas;
  document.write("Dinero disponible: <br />" + respuestaDineroReal + "<br /><br />");
}



//Que es una Funcion?
/////un bloque de codigo que hace uno o varios procedimientos.

//Cuando me sirve usar una funcion en mi codigo?
////Cuando quieras llevar acabo un procedimento en algun tiempo en especifico, no nesesariamente al cargar la pagina.

//Cual es la diferencia entre los parametros y los argumentos de una funcion?
////Parametro es una variable que está en la definición de una función, argumento son los datos que se le pasan a los parametros de una función

//Convierte el siguiente código en una función, pero, cambiando cuando sea necesario las variables constantes por parámetros y argumentos en una función:
const name = "Juan David";
const lastname = "Castro Gallego";
const completeName = name + lastname;
const nickname = "juandc";
console.log("Mi nombre es " + completeName + ", pero prefiero que me digas " + nickname + ".");
var selecionHumano = prompt("Te interesa saber quien es el maestro de JavaScript basico? \n escribe 1 para si \n escribe 2 para no");
var seleccion = parseInt(selecionHumano);
var resultadoDeSeleccion = seleccion === 1 ? document.write("<br /><strong>Bonus Extra</strong> <br />Mi nombre es " + completeName + ", pero prefiero que me digas " + nickname + ".") : document.write("<h1>no hay bonus para ti.</h1> <strong><br />Muahaha</strong>");


//¿Qué es una condicional?
////hay dos tipos de condicionales, es un codigo que activa una de dos comportamientos distintos, declaras una condision y si se cumple, el programa hara un comportamiento, en caso que no se cumpla la condicion, ocurre el comportamiento alterno deseado.

//¿Qué tipos de condicionales existen en JavaScript y cuáles son sus diferencias?
///hay dos tipos, una es usando el "if, else, if else" y el otro es un operador ternario/Ternary. Los "if, else, else if" son para bloques de codigos que contendran procedimientos y funciones a cumplir tanto si se da el caso o no.
///el segundo tipo, el Ternario/Ternary es para una condicional que requiera una sola linea de codigo.

//¿Puedo combinar funciones y condicionales?
///si, si puedes.

//Replica el comportamiento del siguiente código que usa la sentencia switch utilizando if, else y else if:
const tipoDeSuscripcion = "Basic";

switch (tipoDeSuscripcion) {
   case "Free":
       console.log("Solo puedes tomar los cursos gratis");
       break;
   case "Basic":
       console.log("Puedes tomar casi todos los cursos de Platzi durante un mes");
       break;
   case "Expert":
       console.log("Puedes tomar casi todos los cursos de Platzi durante un año");
       break;
   case "ExpertPlus":
       console.log("Tú y alguien más pueden tomar TODOS los cursos de Platzi durante un año");
       break;
}
if (tipoDeSuscripcion == "Free"){
  console.log("Solo puedes tomar los cursos gratis");}
  else if(tipoDeSuscripcion == "Basic"){
    console.log("Puedes tomar casi todos los cursos de Platzi durante un mes");}
    else if(tipoDeSuscripcion == "Expert"){
      console.log("Puedes tomar casi todos los cursos de Platzi durante un año");}
      else if(tipoDeSuscripcion == "ExpertPlus"){
        console.log("Tú y alguien más pueden tomar TODOS los cursos de Platzi durante un año");}
        else{
          console.log('incorrecto');
        }

//Replica el comportamiento de tu condicional anterior con if, else y else if, pero ahora solo con if (sin else ni else if).
if (tipoDeSuscripcion == 'free') {
	console.log('Solo puedes tomar los cursos gratis');
}
if (tipoDeSuscripcion == 'basic') {
	console.log('Puedes tomar casi todos los cursos de Platzi durante un mes');
}
if (tipoDeSuscripcion == 'expert') {
	console.log('Puedes tomar casi todos los cursos de Platzi durante un año');
}
if (tipoDeSuscripcion == 'expert+') {
	console.log(
		'Tú y alguien más pueden tomar TODOS los cursos de Platzi durante un año');
}

//Bonus: si ya eres una experta o experto en el lenguaje, te desafío a comentar cómo replicar este comportamiento con arrays y un solo condicional. 😏
//var array = [new Subscripcion("Free"), new Subscripcion("Basic"), new Subscripcion("Expert"), new Subscripcion("ExpertPlus")];
//lo intente pero no di

//¿Qué es un ciclo?
////Un ciclo, loop o bucle son un conjunto sentencia estructuradas que permite la ejecución de código de forma repetitiva.

//¿Qué tipos de ciclos existen en JavaScript?
////Existe los siguiente ciclos: For, For…of, while, do …while

//¿Qué es un ciclo infinito y por qué es un problema?
////Es cuando no pones un limite al ciclo como un tope o un break y puede llegar a crashear el navegador o incluso el dispositivo en el que se esta ejecutando el ciclo.
////Es un ciclo que nunca se va a detener, puede causar que nuestro ordenador se apague por exceso consumo de memoria en el navegador

//¿Puedo mezclar ciclos y condicionales?
////si

//Replica el comportamiento de los siguientes ciclos for utilizando ciclos while:
for (let i = 0; i < 5; i++) {
    console.log("El valor de i es: " + i);
}
for (let i = 10; i >= 2; i--) {
    console.log("El valor de i es: " + i);
}
////
let i = 0;
while( i < 5 ) {
  console.log("El valor de i es: ", i);
  i++;
}
i = 10;
while (i >= 2) {
  console.log(`El valor de i es: ${i}.`);
  i--;
}

//¿Qué es un array?
////es una esructura de objetos (lo podrias visualizar como una lista de objetos).

//¿Qué es un objeto?
////In JavaScript, an object is a standalone entity, with properties and type/es una entidad por si propia, con propiedades y tipo.

//¿Cuándo es mejor usar objetos o arrays?
////cuando trabajes con enlistado, o varios objetos que forman parte de algo general.

//¿Puedo mezclar arrays con objetos o incluso objetos con arrays?
////Claro que si!!!

//Crea una función que pueda recibir cualquier array como parámetro e imprima su primer elemento.
let frutas = ["papaya", "uva", "fresa"];
function comerFruta(fruta){
  document.write('<br /> Pero Que rica ' + frutas[0] + "🤭");
}
 if (seleccion === 3){
   comerFruta();
 }

 //Crea una función que pueda recibir cualquier array como parámetro e imprima todos sus elementos uno por uno (no se vale imprimir el array completo).
function cualquierArray(fruta){
  document.write("<br />que rica " + fruta);
}
for (let i = 0; i < frutas.length; i ++){
  cualquierArray(frutas[i]);
}

//4️⃣ Crea una función que pueda recibir cualquier objeto como parámetro e imprima todos sus elementos uno por uno (no se vale imprimir el objeto completo).
////

let obj = [];
function imprimir(objetos){
  console.log("objeto: " + objetos + " agregado")}
function presioname(){obj.push(prompt("Agrega un Objeto\nLo que tu quieras..."));
for(let o = 0; o < obj.length; o ++){
  imprimir(obj[o]);
}
}
