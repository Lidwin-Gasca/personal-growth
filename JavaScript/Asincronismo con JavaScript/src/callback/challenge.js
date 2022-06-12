// instanciamos el XML Sx: require('nombre_consola').nombre_archivo;
// guardo en la variable el valor del archivo XMLHttpRequest
let request = require("xmlhttprequest").XMLHttpRequest;

// API, guardamos la api en una variable 
const API = 'https://rickandmortyapi.com/api/character/';

// funcion que nos permite traer la informacion desde nuestra API, recibe un callback y desencadena los llamados que necesitamos.
function fetchData(url_api, callback) {
    // construimos la peticion por xmlhttprequest generando la referencia al objeto que necesito
    let datos = new request();
    // hacemos el llamado a una url 
    datos.open('GET', url_api, true); /* el true activa el asincronismo  */
    // escucho lo que hace la conexion 
    datos.onreadystatechange = function (e) {
        // validamos para saber si fue exitoso todo
        if (datos.readyState === 4) {
            // saber el status 
            if (datos.status === 200) {
                // regresamos el callback si todo sale bien, responseText me lo convierte de object a string
                callback(null, JSON.parse(datos.responseText));
            } else { /* si las cosas no salen bien le pasamos la url y el estado */
                const error = new Error('Error' + url_api + ' paso esto: ' + datos.status);
                // al final retornamos el callback con un msj de error y un null ya que no se desencadena nada 
                return callback(error, null);
            }
        }
    }
    // enviamos la solicitud con send().
    datos.send();
}


/*Creamos una instancia con el objeto XMLHttpRequest que incluye diversos metodos y atributos que nos permiten manejar la solicitud.
con el método object.open() inicializamos el pedido. Recibe los parametros (method, url, async, user, password).

object.onreadystatechange define una funcion que se ejecutará cada vez que el atributo readyState cambie.

los valores de readyState pueden ser los siguientes:

0: request no inicializado,
1: conexion con el servidor establecida,
2: solicitud recibida,
3: solicituid siendo procesada,
4: solicitud finalizada y respuesta lista.
Los atributos status y statusText llevan el stado de el objeto XMLHttpRequest.

200: “OK”
403: “Forbidden”
404: “Page not found”
Estos son los códigos más comunes.

El atributo responseText lleva la respuesta en al pedido como texto, en el caso de nuestra solicitud a la API debemos convertirla a un documento JSON para poder acceder a sus elementos usando `JSON.parse(object.responseText).

El método object.send() envia la solicitud.
*/



//otro ejemplo excactamente igual/////////////////////////////////////////////////////////////////////////////////////////////////
/* Instanciamos la dependencia con require() */
let XMLHttpRequest = require('xmlhttprequest').XMLHttpRequest;

function fetchData(url_api, callback) {
  let xhttp = new XMLHttpRequest(); // Referencia del objeto que necesitamos.
  /* Hacemos un llamado a una url */
  xhttp.open('GET', url_api, true) // El último parámetro hace referencia al asincronismo. Por defecto es true, pero lo ponemos para referencia.
  /* 'Escuchamos' lo que hará la conexión (Referente a los 5 estados que comenta el profesor) */
  xhttp.onreadystatechange = event => {
    if (xhttp.readyState === 4) { // Validar si la petición se completó. (Estado 5 pero contamos desde 0 como en un array)
      if (xhttp.status === 200) { // Validar el estado en el que se encuentra la petición. (200 = todo bien, 400 = no encontró algo, 500 = error en el servidor)
        /* Regresar el callback (primer valor que pasamos es el error y el segundo es el resultado del llamado a la API) */
        callback(null, JSON.parse(xhttp.responseText)) // Como el resultado viene en formato de texto de JSON, lo tenemos que convertir a un objeto para trabajar con él
      } else {
        /* Definimos y retornamos un error en caso de obtenerlo (buena práctica) */
        const error = new Error('Error ' + url_api)
        return callback(error, null)
      }
    }
  }
  xhttp.send(); // Enviamos la petición.
}


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////// continuacion de ambos codigos de arriba (cada uno es independiente).//////////////////////////////////



// importamos el modulo para hacer las peticiones
let XMLHttpRequest = require('xmlhttprequest').XMLHttpRequest;
// direccion de la API
let api = 'https://rickandmortyapi.com/api/character/';

// funcion principal
function fetchData(url_api, callback){
  // instanciamos la conexion
  let xhttp = new XMLHttpRequest();
  // abrir una conexion con el metodo, la ruta y si es asincrono
  xhttp.open('GET', url_api, true);
  // validacion del llamado
  xhttp.onreadystatechange = (event) => {
    // el state 4 es el ultimo de la peticion
    if(xhttp.readyState === 4){
      // verificamos que el status este en 200, que dice que todo bien, no un 400 o 500
      if(xhttp.status === 200){
        // el primer valor es el err, y el siguiente el resultado
        // ejecutamos el callback con el resultado
        callback(null, JSON.parse(xhttp.responseText));
      } else {
        // si no es 200
        let error = new Error('Error: ' + url_api);
        // matamos el proceso con un error
        return callback(error, null);
      }
    }
  }
  // por ultimo enviamos la peticion
  xhttp.send();
}

// primero buscamos la lista de personajes
fetchData(api, (error1, data1) => {
  // si error, matamos retornando un error
  if(error1) return console.error(error1);
  // luego buscamos en la api el id de Rick
  fetchData(api + data1.results[0].id, (error2, data2) => {
    // si error, matamos retornando un error
    if(error2) return console.error(error2);
    // por ultimo la consulta a la api que contiene su dimension
    fetchData(data2.origin.url, (error3, data3) => {
      // si error, matamos retornando un error
      if(error3) return console.error(error3);
      
      // mostramos los resultados :) 
      console.log(data1.info.count);
      console.log(data2.name);
      console.log(data3.dimension);
      
      // rutas de las peticiones en orden
      console.log(api);
      console.log(api + data1.results[0].id); 
      console.log(data2.origin.url); 
    
    });
  });
});