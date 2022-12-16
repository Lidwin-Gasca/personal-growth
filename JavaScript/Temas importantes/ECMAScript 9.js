//Spread Operator
const obj = {
    name: 'oscar',
    age: 32,
    country: 'MX'
};
let { county, ...all } = obj;   //operador de Reposo
console.log(all);


//➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
//Porpagation Properties
const obj = {
    name: 'oscar',
    age: 32
};
const obj1 = {
    ...obj,     // es para unir dos objetos en uno/
    country: 'MX'
};
console.log(obj1);

//➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
//PROMISE: Finally
const helloWorld = () => {
    return new Promise((resolve, reject) => {
        (true)
        ? setTimeout(() => resolve('Hello World'), 3000)   // ? resolve('Hello World')
        : reject(new Error('Test Error'))
    });
};

helloWorld()
    .then(response => console.log(response))
    .catch(error => console.log(error))
    .finally(() => console.log('Finalizo')) //Este ".finally" es lo nuevo en ECMAScript
    // Dentro de ".finally" pondras lo que quieras que suceda al finalizar una promesa, sea cumplida o no. 

//➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
//AGRUPAR BLOQUE DE REGEX       // "regexData" va a ser la constitucion
const regexData = /([0-9]{4})-([0-9]{2})-([0-9]{2})/;   //lo que  hacemos aqui es establecer una regla "/" con los bloques ordenados para 'año', 'mes', y 'dia'.       //en corchertes se especifica los 'numeros' permitidos para usar, en este caso del cero al nueve "[0-9]", seguido de cuantas veces de pueden usar, en este caso fueron cuatro "{4}" para el año, dos para el mes y dia "{2}".
const match = regexData.exec('2018-14-20'); // el 'match' que nos va a dejar saber a nosotros si estan establecido los datos sobre este regex.
const year = match[1];
const month = match[2];
const day = match[3];

console.log(year, month, day);

//The exec() method executes a search for a match in a specified string. Returns a result array, or null.

//➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
