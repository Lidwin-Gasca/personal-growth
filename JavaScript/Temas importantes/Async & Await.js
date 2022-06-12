const helloWorld = () => {  //creamos una constante/variable llamada "helloWorld", la cual definimos como una funcion flecha (lo cual viene siendo una funcion anonima).
    return new Promise((resolve, reject) => { //dentro de esta funcion anonima pedimos que nos regrese una "nueva Promesa", la cual a su vez crea otra funcion flecha, una funcion anonima que tiene como parametros "resolve" y "reject", que significa cierto y falso, cumplido y no cumplido. 
        (true) ? setTimeout(() => resolve('Hello World'), 3000) : reject(new Error('Test Error')) //dentro de esta nueva funcion flecha (funcion anonima) introducimos un OPERADOR Ternario (es una especie de "if" pero que solo ocupa una linea de codigo), el cual constituye de tres partes, la primera es CONDICION, seguido por un signo de interrogacion "?" ahora la segunda parte es lo que sucedera si se cumple la CONDICION de la primera parte, se usa el simbolo dos puntos ":" para separarlo de la tercera parte que es lo falso, o sea lo que sucedera si la CONDICION no se cumple.    💢 En esta linea de codigo, dentro de la segunda parte del operador Ternario(la parte 'true') se crea otra funcion flecha, dentro de la cual se declara que se activara la promesa en modo su resuelto ('resolve').   💢Dentro de la tercera parte, se encuentra 'reject' y como su parametro (no se dice parametro en este caso, pero no se como llamarlo) todo lo que sucedera cuando la promesa sea rechazada.
    }) // cerramos el bloque de la funcion flecha y tambien el parentesis de la "nueva Promesa".
}; // cerramos el bloque que es el valor de la variable constante llamado helloWorld.

const helloAsync = async () => {// se crea una constante llamada 'helloAsync' y dentro de ella, es decir su valor, es una palabra reservada llamada 'async' que signifca asincronismo, la cual parece tener la habilidad funcionar como una funcion (con la ayufa de funcion flecha claro).
    const hello = await helloWorld(); // dentro de este bloque se creo la constante 'hello' cuyo valor tiene 'await' seguido de el llamado a una constante que tiene como valor una funcion, 'helloWorld' pero para llamarlo como tal, es necesario añadirle los parentesis: helloWorld();
    console.log(hello);  // se llama la constante recien creada 'hello', lo que en efecto cadena llamara a 'helloworld', el cual nos regresa a la promesa.
};

helloAsync();


//💢💦 A CONTINUACION LA FORMA CORRECTA DE USAR EL ASYNC & AWAIT.
const anotherFuntion = async () => { // esta constante vendria reemplazando a 'helloAsync'
    try { //aun no se que significa 'try'
        const hello = await helloWorld();
        console.log(hello);
    } catch (error) { // aun no se que significa 'catch'
        console.log(error);
    }
};

anotherFuntion();