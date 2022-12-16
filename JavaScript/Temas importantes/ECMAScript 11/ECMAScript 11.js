
//Big Int

const aBigNumber = 9007199254740991n;
const anotherBigNumber = BigInt(9007199254740991);

console.log(aBigNumber);
console.log(anotherBigNumber);



//➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖


//Promises.allSettled

const promise1 = new Promise((resolve, reject) => reject("reject"));
const promise2 = new Promise((resolve, reject) => resolve("resolve"));
const promise3 = new Promise((resolve, reject) => resolve("resolve 1"));

Promise.allSettled([promise1, promise2, promise3]).then(response => console.log(response));


//➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖


//Nullish coalescing

const fooo = null ?? 'default string';
//const fooo = 'escribir un srting' ?? 'default string';
console.log(fooo);
//se usa para no romper tu codigo, es decir, cuando mandas a llamar a una variable, funcion u objeto y este no existe, tu pagina web no cargara, dara error y se ira todo a caño.
//usando "Nullish" solucionaras el hecho de tener un error, sera de alguna madera ignorado, adelante un ejemplo:
const user = {};
console.log(user.profile.email);//email no existe, asi que al correr esta linea de codigo se tendra un error diciendo que no se encuentra email, para "solucionar" esto usamos nullish.
//En su lugar escribamos esto:
console.log(user?.profile?.email);//de esta manera el compilador le dara un valor 'undifined', asi no rompera tu codigo, solo sera de un cierto modo ingnorado.


//➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

//Nullish coalescing

if(user?.profile?.email){ //recuerda que al no especificar "que quieres hacer" en los if, solo busca si lo que escribiste es "cierto" o "falso"
    console.log('email');
} else{
    console.log('fail');
}
// al correr este codigo, siempre dara falso, en este caso: fail